# glacier-buffer-replacement-utac

GenesisAeon Package 100 — companion to [glacier-buffer-utac](https://github.com/GenesisAeon/glacier-buffer-utac)
(P99, the loss side). This package covers the replacement/mitigation
side: **Artificial Glacier Buffer Replacement (AGBR)**. **Deliberately
has no UTAC/CREP/AFET bridge** — see [DISCLAIMER.md](DISCLAIMER.md).

## Two explicit confidence tiers

- **Core** (`reservoir`, `mar`, `evaporation`, `mass_balance`): real,
  peer-reviewed findings independently re-verified 2026-08-10 via direct
  paper/DOI lookup — not just copied from the originating DeepResearch
  report.
- **Optional / speculative** (`peatland`, `rrf`): weakly sourced or
  literally unpublished figures, kept because they were part of the
  original discussion. Always exposed with an explicit warning constant
  (`PEATLAND_WEAK_SOURCE_WARNING`, `RRF_NOT_PEER_REVIEWED_WARNING`).

## What's real here (core)

- Farinotti, Pistocchi & Huss (2016, *Environmental Research Letters*):
  an optimally sited dam/reservoir strategy could offset **up to 65%**
  of the projected end-of-century summer-runoff change in the European
  Alps — a real, verified ceiling, not a guarantee.
- Steffen et al. (2022, *Earth Surface Dynamics*): 683 potential new
  Swiss proglacial lakes, 1.16 km³ total potential volume — but only
  ~10% realized by 2050 and ~48% by 2100 under a middle-of-the-road
  scenario.
- Fabbri et al. (2021, *Swiss Journal of Geosciences*): real Lake Brienz
  sedimentation rates (3.0 cm/yr average, up to 4.7 cm/yr near deltas) —
  the physical limiter on how long a proglacial reservoir stays useful.
- Ochoa-Tocachi et al. (2019, *Nature Sustainability*) and Jodar et al.
  (2022, *Science of the Total Environment*): two real, operating
  Managed Aquifer Recharge systems (Peruvian amunas, Spanish acequias de
  careo) — 45-day mean retention, +92% aquifer recharge respectively.
- Jin et al. (2023, *Nature Sustainability*) and Ilgen et al. (2024,
  *Hydrological Sciences Journal*): floating-solar evaporation
  mitigation, up to 49.7% at the Aswan High Dam's 90%-coverage case
  study.
- The core mass-balance argument (`mass_balance.py`): **full
  replacement of a glacier's hydrological buffer is physically
  impossible** — a network can only redistribute existing water in
  time, never create new water. `full_replacement_is_possible()` always
  returns `False`.

## What's optional/speculative here

- `peatland.py`: a storage-capacity range that mixes a weak (legal
  document) citation with a non-Alpine (Brazilian tropical peat)
  measurement — flagged, not load-bearing.
- `rrf.py`: the "Resilience Replacement Factor" and its three named
  scenarios, inherited from the originating AI DeepResearch report with
  no primary citation for the formula itself. Every function carries
  `RRF_NOT_PEER_REVIEWED_WARNING`.

## Quickstart

```bash
pip install glacier-buffer-replacement-utac
```

```python
from glacier_buffer_replacement_utac import (
    theoretical_mitigation_ceiling,
    full_replacement_is_possible,
    SWISS_ALPS_LAKE_POTENTIAL,
    amuna_retention_days_mean,
    aswan_case_study,
    ALL_SCENARIOS,
    RRF_NOT_PEER_REVIEWED_WARNING,
)

print(theoretical_mitigation_ceiling())   # 0.65 -- Farinotti et al. 2016
print(full_replacement_is_possible())     # False, always
print(SWISS_ALPS_LAKE_POTENTIAL)
print(amuna_retention_days_mean())        # 45
print(aswan_case_study()["evaporation_reduction_pct"])  # 49.7

print(RRF_NOT_PEER_REVIEWED_WARNING)
for scenario in ALL_SCENARIOS:
    print(scenario.name, scenario.rrf_range)
```

## Development

```bash
pip install -e ".[dev]"
pre-commit install
ruff check src tests
mypy src
pytest
```

## Citation

See [CITATION.cff](CITATION.cff) and [.zenodo.json](.zenodo.json).
