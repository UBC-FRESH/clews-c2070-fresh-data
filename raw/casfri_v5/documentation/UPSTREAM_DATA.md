# CASFRI v5 — Upstream Data Pointer

Recorded 2026-11-14. This file is a pointer and disambiguation note; it does **not** add any CASFRI database payload to the archive.

## Upstream entry points

| Resource | URL | Notes |
|----------|-----|-------|
| CASFRI project page | https://casfri.github.io/CASFRI/index.html | Project overview, publications, team, and framework description (HTTP 200 observed 2026-11-14) |
| CASFRI source repository | https://github.com/CASFRI/CASFRI | Conversion framework and PostgreSQL schema (GPL-3.0); the repository does **not** bundle the provincial/territorial source FRIs |
| Data dictionary / specifications | https://github.com/CASFRI/CASFRI/blob/master/documentation/specifications/README.md | Schema specification entry point (HTTP 200 observed 2026-11-14) |
| Local framework sidecar | `data/raw/casfri_v5/PROVENANCE.md` | Pins upstream tag `v5.3.1` (commit `c09a70cc1f90894a1d32c2f20606430b49ae274f`) and lists the curated translation-table/documentation subset |
| Local translation tables | `data/raw/casfri_v5/translation_tables/` | Per-jurisdiction CSV mappings used by the FRESH adapter |
| Local documentation subset | `data/raw/casfri_v5/documentation/` | Upstream README pointer, inventory list, release/update procedures |

## What CASFRI is — and is not

- **CASFRI is a polygon inventory harmonization framework.** It translates provincial/territorial Forest Resource Inventory (FRI) polygon layers into the common `casfri.cas`, `casfri.cst`, `casfri.geo`, and `casfri.nfl` PostgreSQL schema using per-jurisdiction translation tables.
- **CASFRI is not a plot remeasurement dataset.** It contains inventory polygons and their attributes (species composition, age, height, volume/biomass attributes where the source provides them), not tagged individual trees measured repeatedly through time. It cannot substitute for NFI ground plots, MAGPlot remeasurement records, or provincial PSP/PEP growth data in an FVS-CA calibration.
- **CASFRI complements SCANFI.** SCANFI is a wall-to-wall 30 m raster; CASFRI is a jurisdiction-specific vector polygon harmonization. Neither replaces the other.
- **The framework repository does not contain the source FRIs.** Acquiring CASFRI polygons means acquiring the underlying provincial/territorial inventories, each under its own licence and access route. The framework is GPL-3.0 code/schema; the data licences vary by jurisdiction.

## NRCan CKAN record: WMS/docs only

The NRCan/NFIS "CASFRIv5" Open Canada record (`https://open.canada.ca/data/en/dataset/0177f4ed-123c-43a8-83ed-44dc12e1af6e`) publishes two 50 m raster layers, `dominant_genus_casfri` and `tree_type_casfri`, derived from CASFRI v5. That record is **WMS-only**: it exposes map images and documentation, not an ingestible bulk payload, and no WFS or archive download is provided. The CKAN record therefore does **not** contain CASFRI polygon payloads.

This distinction is load-bearing: an Open Government Licence — Canada label does not imply that bulk data are downloadable. See `metadata/source-reviews/casfri_v5_schema.md` §2 in the parent repository for the four-artifact disambiguation table.

## Local archive boundary

The local CASFRI sidecar contains only:

- `translation_tables/` — curated per-jurisdiction CSV mappings and cross-jurisdiction species/attribute tables.
- `documentation/` — upstream specification pointer, inventory list, release procedure, inventory-update procedure, and this pointer.

It intentionally does **not** contain:

- The full CASFRI PostgreSQL database or any harmonized polygon dump.
- The 49 provincial/territorial source FRI payloads.
- The GPL-3.0 conversion/workflow source code.
- Any NRCan CASFRIv5 raster tiles.

**Do not download full CASFRI databases** without a separate scope decision and a jurisdiction-by-jurisdiction licence review. The current integration uses the translation tables at runtime and one open-jurisdiction diagnostic ingest (BC/QC) documented in the parent repository.

## Reproduction / verification

```bash
# Verify the project page and specification pointer are live:
curl -sSIL https://casfri.github.io/CASFRI/index.html
curl -sSIL https://github.com/CASFRI/CASFRI/blob/master/documentation/specifications/README.md

# The local sidecar's pinned upstream tag and commit:
grep -E 'Upstream tag|Upstream commit' data/raw/casfri_v5/PROVENANCE.md
```
