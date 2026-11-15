# FVSCA calibration v0 — harmonization review fixes

**Rebuild:** 2026-11-15T07:27:50Z
**Code at build:** parent commit `1ca5fec` (dirty worktree; fixes below)
**Supersedes:** data commits `0654864` (payload) and `e22dc2f` (QA/manifest refresh)

The previous v0 was **invalid**. Two unit/ordering defects changed the
calibration content, and several validation gaps allowed the defects to pass:
the Québec PEP `plot_area_ha` column was labelled hectares but stored square
metres (a 10,000x error), and MAGPlot visit ordering lost legitimate
consecutive-measurement intervals. The extract was rebuilt from the unchanged
archived raw payloads after correcting the code, tests, and hard checks.

## Findings and corrections

### Critical

1. **QC PEP plot area was 10,000x too large.**
   `workflows/national/plot_harmonization/qc_pep.py:56-64`
   (`plot_area_ha()`). The source `tige_ha` is **stems per hectare**, so one
   stem represents `1 / tige_ha` hectares. The old code used
   `10000.0 / expansion_factor`, treating `tige_ha` as m² per stem. A 25
   stems/ha plot was written as `400.0` "ha" instead of `0.04` ha.
   The function now returns `1.0 / positive(expansion_factor)`; no
   `10000.0 / expansion_factor` path remains. Covered by
   `tests/test_plot_harmonization.py::test_qc_plot_area_is_hectares`.

2. **MAGPlot intervals were lost by site-level visit ordering.**
   `workflows/national/plot_harmonization/magplot.py:188-196` (ZIP) and
   `magplot.py:477-481` (WFS). ZIP ordering ranked `meas_num` per `site_id`
   (including lexicographic/null-prone handling); WFS assigned one cumulative
   order per `site_id`, interleaving nested plots. A tree in plot P1 could
   receive orders 1 and 3 while P2 received 2 and 4, so the
   consecutive-visit test `order1 - order0 == 1` rejected valid intervals.
   Both paths now sort and `cumcount()` per `(site_id, plot_id)`, with
   `meas_num` parsed numerically before ordering. Covered by
   `test_magplot_zip_multi_plot_visits_keep_both_intervals` and
   `test_magplot_wfs_multi_plot_visits_keep_both_intervals`.

### Major

3. **Float-promoted status codes mapped to `missing`.**
   `workflows/national/plot_harmonization/common.py:114-122`. Codes such as
   `10.0` and `0.0` did not match the string lookup keys `"10"`/`"0"`.
   `map_status()` now strips a trailing `.0` before upper-casing and lookup.
   Covered by `test_map_status_strips_float_promotion`.

4. **Dead endpoints with null DBH were discarded.**
   `workflows/national/plot_harmonization/common.py:237-299`. The old interval
   filter required `dbh_cm.notna()` on every observation, so a tree recorded
   dead without a final DBH produced no interval. The builder now requires a
   known **start** DBH (`start_has_dbh`) and accepts a null end DBH only when
   `status_end == "dead"` (`end_has_dbh`). Live ends still require a measured
   DBH. Covered by `test_intervals_keep_dead_endpoint_without_dbh`.

5. **Interval rows lacked endpoint visit identifiers.**
   `workflows/national/plot_harmonization/schema.py:66-80` and
   `common.py:293-294`. `visit_id0`/`visit_id1` are now in
   `INTERVAL_COLUMNS` and are populated from the shifted visit IDs, making
   intervals joinable when one site has several plots in the same year.
   Covered by the MAGPlot ordering tests and the interval endpoint assertions.

6. **Reconciliation could be satisfied by any drop reason.**
   `workflows/national/plot_harmonization/validate.py:420-467`. The old check
   used `bool(dropped)`, so a null-only reason such as
   `tree_dbh_out_of_range` excused an arbitrary row-count delta. Validation
   now uses `manifest["sources"][source]["explained_drops"][table]`, requires
   it to be an exact integer row count, and requires the absolute delta to be
   less than or equal to that count. `build.py:179-182` and `build.py:547/572`
   populate it from the row-removing reasons only. Covered by
   `test_validate_rejects_explained_source_delta`,
   `test_validate_null_only_reason_does_not_explain_delta`, and
   `test_validate_accepts_explained_source_delta`.

7. **Manifest and output integrity checks were incomplete.**
   `workflows/national/plot_harmonization/validate.py:130-160`,
   `validate.py:480-530`, and `validate.py:534-560`. A missing
   `manifest.json` is now a single hard failure; empty required tables fail;
   every declared output is checked for bytes, SHA-256, and row count; the
   species crosswalk is checked for columns, non-emptiness, source coverage,
   and group domain. Covered by `test_validate_requires_manifest`,
   `test_validate_rejects_empty_required_frame`,
   `test_validate_detects_output_hash_mismatch`, and
   `test_validate_requires_species_crosswalk`.

8. **Build parameters did not consistently determine manifest inputs.**
   `workflows/national/plot_harmonization/build.py:145-151`,
   `build.py:185-197`, and `build.py:482-500`. The manifest now records only
   the labels implied by `--sources`, `--no-wfs`, and `--qc-gpkg`; a supplied
   GeoPackage is recorded as `qc_pep_gpkg` instead of a ZIP member. With
   `--max-sites`, `load_wfs` receives the full ZIP site-id set from
   `magplot.all_site_ids()` (`magplot.py:112-116`), not the truncated sample
   set, so WFS overlap exclusion is unchanged by sampling.

### Minor

9. **NL FAL date/timezone and `PLOTSIZE` parsing.**
   `workflows/national/plot_harmonization/nl_fal.py:131-137` and
   `nl_fal.py:162-168`. `ORIGINAL_DATE` is epoch milliseconds converted to
   `America/St_Johns` before `.dt.year`; `PLOTSIZE` is parsed with
   `numeric()` before conversion/formatting, avoiding `Int64` cast failures
   on string or null values. The coordinate bounds and WFS EPSG:3978
   transformed coordinates are also range-checked (`magplot.py:362-363`).

10. **Documentation counts were stale.** `workflows/national/plot_harmonization/README.md`
    and the metadata registry now carry the rebuilt counts and hashes below.

## Old versus new counts

| source | sites | visits | trees | old intervals | new intervals | delta |
|---|---:|---:|---:|---:|---:|---:|
| faib_psp | 7,341 | 23,956 | 3,217,643 | 1,799,382 | 1,799,382 | 0 |
| faib_non_psp | 9,512 | 11,951 | 366,788 | 80,702 | 80,702 | 0 |
| magplot | 39,130 | 257,031 | 7,771,041 | 3,293,792 | 3,298,527 | +4,735 |
| magplot_wfs | 2,778 | 13,906 | 1,298,474 | 369,878 | 436,550 | +66,672 |
| qc_pep | 12,834 | 53,632 | 2,210,417 | 979,461 | 1,119,613 | +140,152 |
| nl_fal | 1,380 | 7,657 | 775,477 | 488,111 | 493,517 | +5,406 |
| **total** | **72,975** | **368,133** | **15,639,840** | **7,011,326** | **7,228,291** | **+216,965** |

Sites, visits, and trees are unchanged because the fixes correct units,
ordering, endpoint handling, and validation rather than selection. The QC
site-level `plot_area_ha` example is `400.0` → `0.04` ha for `tige_ha = 25`
(12,520 of 12,815 QC site rows carried the erroneous 400.0 value).

## Output hashes

| file | rows | old SHA-256 | new SHA-256 | bytes |
|---|---:|---|---|---:|
| `sites.csv` | 72,975 | `a88e68918266800c58ccf9d7699435dc7689db707a119a5675e375bcb128b6c8` | `7796f2c8f8b83284c3980333e1563de4bb409f10668f1bb32a5fca2bccf54de9` | 8,359,304 |
| `visits.csv` | 368,133 | `bd07dc1189d5feca8c04f3ad589a68f10f62115bb85007a8b2dcf2dcbb61534c` | same | 30,574,202 |
| `trees.csv.gz` | 15,639,840 | `a0b540f45d6f325792d3e56f36727018514336862077610ea0c34ba5de3afffe` | same | 103,812,857 |
| `intervals.csv.gz` | 7,228,291 | `bf2781a33d4e4c84eadb557c061ad747a6467187c426901f10388c24c87b4c10` | `b42845c5bab5732e0dc483119005b4fa48400a59b8c2e6892f8a7c92acdd3f9b` | 53,638,804 |
| `species_crosswalk.csv` | 355 | `4074882426dc3c73d24f32da7d23328a89a9dcd47f13d847445b6d36f182e35c` | same | 18,222 |
| `manifest.json` | — | `ffe8ea09d8ed313388da72aafe3f6373390f4eb1faab4c0fc0686051fe13879f` | `f49b1ec73b79e5b6201b08095b93288f65399debe3efa0738e23f6841bd63239` | 16,710 |
| `QA.md` | — | `0e293864c1928da6eec6fc8e5b336413c43599c7951160fc506aaf93ccd6bbf3` | `d6b1a354fa5ca0a883501e1639d75a0afd2baa5ae72e0763ac5c002b2327fe75` | 11,636 |
| `validation.json` | — | `cb3a9beae34d7fe0382cdeb42602f30b08c7bdeb162d5298a1df93792bd1eeeb` | `0b84d7cbcfb3fdb3021c528a751c69336ab4094992c9b29afb739d279e907150` | 9,894 |

`visits.csv` and `trees.csv.gz` are byte-identical to the previous v0 because
no selected row, value, or ordering changed; only `sites.csv` (QC units) and
`intervals.csv.gz` (retained dead-end/null-DBH intervals) changed.

## Validation

The rebuilt package passes **69 of 69** hard checks. The reconciliation table is
generated in `QA.md`; all source deltas are 0.0000% for sites and visits, and
tree deltas are covered by exact `explained_drops` counts:

- `faib_psp`: 5 blank-key tree rows;
- `faib_non_psp`: 308 blank-key tree rows;
- `magplot_wfs`: 10,699 duplicate NL WFS tree features;
- `nl_fal`: 3 duplicate tree rows, 1 height-99 sentinel, 168 unmatched
  tallies, and 2 absent-plot visits.

The tests in `tests/test_plot_harmonization.py` cover the QC area conversion,
MAGPlot multi-plot ordering for ZIP and WFS, dead endpoints with null DBH,
float status codes, reconciliation rejection for a 1% unexplained delta,
missing manifests, empty frames, output hash mismatches, and the species
crosswalk.
