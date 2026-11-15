# TSA 24 — Prince George WS4 instance

| Field | Value |
|---|---|
| TSA | 24 — Prince George |
| Instance | `data/derived/ws4/tsa24` |
| Compiled dataset | `/srv/shared-data/gep/ws4/femic/external/femic-tsa24-instance/build/compiled` |
| Dataset manifest SHA-256 | `c1304ed993814b1e4c049e98b53d197fc5218cda32d29d1cc01d2b8eda7a53eb` |
| Dataset files | 12 parquet tables + `manifest.json` (13 files, 12 MB) |
| Created (UTC) | 2026-11-15T09:37:17+00:00 |
| WS4 version | 0.2.0 |
| Lane | Minimal WS4 lane: validate → area control → simulate/report |

## 1. TSA identity

This instance is the Prince George Timber Supply Area (TSA 24). It is the
first pilot for the one-WS4-instance-per-TSA programme and the reference case
used by the WS4 area-control documentation.

## 2. Data sources and provenance

- Compiled dataset: `/srv/shared-data/gep/ws4/femic/external/femic-tsa24-instance/build/compiled`
- Dataset manifest: `dataset/manifest.json`
- Dataset shape: **458,708 fragments/blocks**, **72 tracks**, **48 treatments**,
  **99 accounts**
- FEMIC source bundle: `/srv/shared-data/gep/ws4/femic/external/femic-tsa24-instance`
- Recipe: `forestmodel.xml` generated from the FEMIC model-input bundle
  (`au`, `curve`, `curve_points` tables) and the full TSA24 stand table
- Fragment mapping assumption: `theme2 -> AU`, `age -> F_AGE`,
  `area -> AREA_HA`, and `theme1 == 1 -> IFM managed`; otherwise unmanaged.
  `ORIGIN=natural`, `SILV_STATE=baseline`.
- Build command: **not rerun in this pilot**. The compiled dataset was produced
  by WS4 on 2026-10-31 and passes `ws4 validate`.
- Rebuild status: **imported compiled dataset**, not a fresh FEMIC run.

The recipe was generated from the FEMIC bundle because the instance did not
contain a checked-in ForestModelXML. The THLB-to-IFM mapping above is an
explicit assumption, not a surveyed THLB.

## 3. AU definition

AU is the `AU(<id>)` token in `tracks.name`:

```yaml
au_regex: 'AU\(([^)]+)\)'
```

The dataset resolves to **24 AUs** (2401000–2401007, 2402000–2402007,
2403000–2403007). Every managed block maps to exactly one AU. The runner fails
if a block maps to more than one AU.

## 4. Growth model

The managed volume curve is:

```yaml
volume_label: feature.Yield.managed.Total
```

For each AU the runner builds the area-weighted managed volume curve, evaluates
`MAI(age) = volume(age) / age` at integer ages, and takes `R` at the maximum.
The land-base area-weighted curve gives:

- managed area `A`: **3,060,473.1 ha**
- area-weighted managed MAI maximum: **2.183 m³/ha/yr**
- rotation age `R`: **100 years**
- area quota `Q = A · P / R`: **306,047.3 ha per 10-year period**
- expected long-run volume: **66.8M m³/period**

These match the documented TSA24 reference. Per-AU rotations are also reported
in `schedules/diagnostics.csv`; they differ by AU (70–200 years) because the
area-weighted land-base curve is dominated by the large, productive AUs.

## 5. Landbase and THLB

- Managed area `A` is the sum of fragments on `IFM(managed)` tracks that carry
  the `CC` treatment: **3,060,473.1 ha**.
- Managed blocks: **208,255** of 458,708 total fragments/blocks.
- Unmanaged fragments remain in the dataset and grow, but are not harvestable
  in this lane.
- THLB mapping assumption: `theme1 == 1` in the FEMIC Patchworks export. The
  compiled dataset has no separate surveyed THLB layer; this is the explicit
  limitation of the pilot.

## 6. Account names

- Managed area: `feature.Area.managed`
- Managed volume: `feature.Yield.managed.Total`
- Harvested volume: `product.HarvestedVolume.managed.Total.CC`
- Treated area: `product.Treated.managed.CC`

The account vocabulary comes from the dataset manifest, not from the factory.

## 7. Treatments

```yaml
treatment: CC
managed_token: IFM(managed)
```

All 48 managed tracks have a `CC` treatment row. The natural managed tracks
carry `begin` 50–180 years; the planted tracks carry the corresponding
`cc_pl` state. Only the configured `CC` treatment is used to decide eligibility
and to write the schedule.

## 8. Area-control configuration

`config/area_control.yaml` declares:

```yaml
period_width: 10
horizon_years: 100
quota_factor: 1.0
min_age: null
quota_scope: global
eligibility: operable
```

`quota_scope: global` is the documented TSA24/TSA29 reference construction: one
land-base quota, oldest-first across all AUs. Per-AU `Q_AU` remains in the
diagnostics. `eligibility: operable` lets an unfilled block remain a candidate
in later periods; this is what carries the period-10 shortfall instead of
liquidating the land base in period 1.

## 9. Build commands

```bash
# Validate the compiled dataset.
ws4 validate --dataset data/derived/ws4/tsa24/dataset

# Build the area-control schedule.
python -m workflows.ws4_instances.area_control \
  --dataset data/derived/ws4/tsa24/dataset \
  --config data/derived/ws4/tsa24/config/area_control.yaml \
  --out data/derived/ws4/tsa24/schedules \
  --periods 10 \
  --schedule-name area_control.csv

# Replay the schedule.
ws4 simulate \
  --dataset data/derived/ws4/tsa24/dataset \
  --schedule data/derived/ws4/tsa24/schedules/area_control.csv \
  --years 100 \
  --out data/derived/ws4/tsa24/runs/area_control

# Diagnostic report against the 70M m3/period policy pull.
ws4 report \
  --run data/derived/ws4/tsa24/runs/area_control \
  --targets data/derived/ws4/tsa24/config/targets.yaml
```

## 10. Generated schedule and simulation

Schedule: **205,959 rows** (one first entry per scheduled block), `offset` 0–99.
The first-entry areas reproduce the documented reference:

| Period | Selected area (ha) | Blocks | Volume (M m³) | Shortfall vs Q (ha) |
|---:|---:|---:|---:|---:|
| 1 | 306,060.1 | 21,380 | 71.683 | 0.0 |
| 2 | 306,049.2 | 24,200 | 76.278 | 0.0 |
| 3 | 306,049.9 | 25,323 | 76.035 | 0.0 |
| 4 | 306,053.5 | 25,739 | 76.621 | 0.0 |
| 5 | 306,082.0 | 24,769 | 78.513 | 0.0 |
| 6 | 306,065.1 | 24,179 | 82.441 | 0.0 |
| 7 | 306,072.2 | 20,187 | 95.160 | 0.0 |
| 8 | 306,083.6 | 17,374 | 94.407 | 0.0 |
| 9 | 306,093.1 | 14,967 | 92.963 | 0.0 |
| 10 | 249,457.1 | 7,841 | 69.943 | 56,590.2 |
| **Total** | **3,004,065.8** | **205,959** | **814.044** | **56,590.2** |

The period-1 volume is **71.68M m³**, matching the documented **~71.7M m³**
reference. The 10-period total is **814.0M m³**; the reference seed's 10-period
total is higher because it adds multi-entry chains and delayed in-period
offsets. Per-period diagnostics are in `schedules/diagnostics.csv`;
`summary.json` carries A, R, Q, MAI(R), hashes, and warnings.

The target report meets the 70M m³/period floor in periods 1–9. Period 10 is
**69.94M m³**, just below the floor; that is a real area-control capacity
signal, not a schedule defect.

## 11. Limitations

- **Single-entry schedule.** One harvest entry per block. The reference seed
  contains second entries at `+100` years and later; this pilot does not.
- **No FEMIC rebuild.** The compiled dataset is imported; the recipe and THLB
  mapping are the FEMIC bundle's, not a new calibration.
- **THLB mapping assumption.** `theme1 == 1` is used as the managed flag; no
  independent THLB layer was supplied.
- **Global quota.** `Q_AU` is diagnostic; the schedule uses the land-base Q.
  This is deliberate to match the documented reference. Use
  `quota_scope: per_au` for an AU-capped variant.
- **Earliest in-period offset.** The reference assigns later offsets within a
  period (e.g. 16, 20, 32) and adds chains; this pilot assigns the earliest
  eligible year. That explains the lower volumes in periods 2–10.
- **Unscheduled area.** 56,407.3 ha of managed area is unscheduled because its
  earliest operable year is at or beyond the 100-year horizon or because the
  final quota shortfall is 56,590.2 ha.
- **No optimization.** The 70M m³ target is a policy pull; no WS4 optimize,
  FHOPS, or portal run is part of this instance.

## 12. Materialization

This directory lives in the `data` DataLad/git-annex submodule.

```bash
git -C data annex enableremote arbutus-s3
datalad get data/derived/ws4/tsa24/dataset
datalad get data/derived/ws4/tsa24/runs/area_control
```

Publish with `~/bin/git-annex-s3 copy --to arbutus-s3 data/derived/ws4/tsa24`
and verify with `git annex whereis` and
`git annex find --not --in arbutus-s3 data/derived/ws4/tsa24`.
