# WS4 SCANFI/RSYC pilot — G2|BC|S32

This directory is a real, compiled WS4 pilot built from SCANFI 30-m
pixels and the parent RSYC tile production library. It is a
`model_estimate` / `sensitivity_only` pilot, not official OSeCAN and
not a chain v5.1 change.

## Identity

- Node: `G2|BC|S32` (parent `G2|BC`)
- Tile / row / col: `G2` / 3 / 2
- Centroid: 49.836521, -125.994053
- Allocated harvest: 228408.176800 m3
- Productive subcell area: 224737.998031 ha
- Forest fragments: 2446363
- Blocks: 932041
- Forest area: 220172.67 ha
- Resolution: 30 m (0.09 ha per fragment)

## WS4 provenance

- Executable: `/srv/shared-data/gep/jupyterhub16-projects/clews-c2070-fresh/.venv-ws4/bin/ws4`
- Editable source tree: `/srv/shared-data/gep/ws4/ws4-gpu`
- Version: `0.2.0`

## Schedule

- Rows: 89895
- Scheduled area: 17844.30 ha
- Eligible blocks (age class >= 40): 898942

The managed track uses the same RSYC curve as the natural track. This
pilot has no planting yield-response data; the managed track records
the management-state transition only.

See `inventory_summary.json` for exclusions, age distribution, curve
usage, clique sizes, validate output, and simulation totals.

## Simulation

- Harvested volume: 6547384.791 m3
- Treated/managed area: 17844.300 ha
- Final managed yield: 5915085.904 m3
