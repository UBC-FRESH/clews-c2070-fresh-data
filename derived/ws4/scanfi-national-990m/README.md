# WS4 national forest estate — SCANFI 30 m to 990 m fragments

This directory is a compiled national WS4 forest-estate dataset built
from SCANFI 30-m age/landcover pixels and RSYC tile group curves. It is
`model_estimate` / `sensitivity_only`; it is not official OSeCAN, not a
policy-grade supply forecast, and does not change chain v5.1 or the UI.

## Resolution change

- `inventory_resolution=30m`: SCANFI age and landcover are read at 30 m.
- `ws4_fragment_resolution=990m`: one WS4 fragment per forest 33 x 33
  pixel block (maximum 98.01 ha). The 50-km supply nodes are inventory
  windows, not fragments.

## Counts

- Forest fragments: 6,807,192
- Blocks: 1,984,017
- Forest area: 411,250,630.32 ha
- Tracks: 2,799
- Used curves: 718
- Schedule rows: 33,284
- Scheduled area: 7,514,902.98 ha

## WS4

- Executable: `/srv/shared-data/gep/jupyterhub16-projects/clews-c2070-fresh/.venv-ws4/bin/ws4`
- Version: `0.2.0`

See `inventory_summary.json` for age/province/curve distributions,
clique sizes, exclusions, validation output, and simulation totals.

## Simulation

- Harvested volume: 968,900,774.756 m3
- Treated/managed area: 7,514,902.980 ha
- Final managed yield: 448,784,158.666 m3
