# Reproduce the headline from this bundle

Run from the repository root:

```bash
.venv/bin/python scripts/national/reproduce_open_data_net_value.py
```

The reproducer:

1. verifies the SHA-256 and row count of every file listed in
   `input_manifest.json`;
2. validates the zone/region mapping, source flags, price-panel flags and
   parameter references;
3. runs `workflows/national/harvest/open_data_net_value.py` with
   `inputs_dir` set to this bundle;
4. requires the exact headline:
   - median 48.84 CAD/m3;
   - range -23.38 to 86.85 CAD/m3;
   - 168 / 945 negative base rows;
   - South West ground 64.40 CAD/m3;
   - North West ground 57.76 CAD/m3;
   - QC cost spread 0.81 CAD/m3;
5. requires byte-identical core outputs versus the published model artifacts.

Any mismatch exits non-zero. To rebuild this bundle from the parent corpus:

```bash
.venv/bin/python scripts/national/build_open_data_model_inputs.py
```

To run the focused tests:

```bash
.venv/bin/python -m pytest -q tests/test_open_data_model_inputs_bundle.py
```

Raw report PDFs are not present in this bundle and are not needed to reproduce
the headline. They are cited in `sources.csv` for audit only.
