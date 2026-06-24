# CLEWs-C2070 FRESH Data

DataLad-backed data archive for the UBC FRESH forestry and forest-biomass
component of CLEWs-C2070.

This repository is intended to be linked into the parent source repository at
`data/`.

## Layout

- `raw/`: immutable source payloads exactly as acquired.
- `interim/`: extracted, normalized, or harmonized source products.
- `processed/`: modelling-ready products.
- `metadata/`: dataset metadata, checksums, and source manifests.
- `manifests/`: acquisition logs and generated file inventories.

Large data payloads are tracked by git-annex and stored in the configured
`arbutus-s3` special remote. Lightweight text metadata is tracked directly in
Git.

## Retrieval

From the parent repository:

```bash
git submodule update --init --recursive
git -C data annex enableremote arbutus-s3
datalad get data/metadata
```

Use selective `datalad get` commands for large payloads.
