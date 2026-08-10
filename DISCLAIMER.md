# DISCLAIMER — Two Confidence Tiers, No Framework Bridge

**Status: Core = real, independently re-verified science. Optional =
weakly sourced or literally unpublished, always flagged. NO UTAC/CREP/
AFET bridge.**

## Core tier — real, independently re-verified 2026-08-10

Every figure below was checked directly against the paper (DOI lookup,
publisher page, or a press summary from the publishing institution) on
2026-08-10 — not just copied from the GeminiDeepResearch report
(`Ersatz alpiner Gletscherpuffer.md`) this package originates from.

- **Farinotti, Pistocchi & Huss (2016)**, *Environmental Research
  Letters* 11(5), 054022: an optimally sited dam/reservoir strategy
  could offset up to **65%** of the projected end-of-century
  summer-runoff change in the European Alps. This is a **ceiling**, not
  an average or a guarantee — it assumes ideal siting and ignores the
  sedimentation/evaporation losses this package documents separately.
  The remaining **35%** is categorically unreachable by a
  redistribution-only strategy — see `mass_balance.py`.
- **Steffen, Huss, Estermann, Hodel & Farinotti (2022)**, *Earth
  Surface Dynamics* 10, 723-741: 683 potential new Swiss proglacial
  lakes totalling 1.16 [1.05, 1.32] km³ — but only ~10% of that volume
  is realized by 2050 and ~48% by 2100 under a middle-of-the-road
  scenario. The oft-quoted "1.16 km³" headline number overstates what's
  actually available at any given point in time.
- **Fabbri, Haas, Kremer, Motta, Girardclos & Anselmetti (2021)**,
  *Swiss Journal of Geosciences* 114, 22: real Lake Brienz sedimentation
  rates, 3.0 cm/yr basin-plain average (2003-2018), up to 4.7 cm/yr near
  deltas — an "extraordinarily high" rate even among Alpine lakes,
  partly inflated by the 2005 flood inside the measurement window. Not a
  universal constant; basin-specific sediment supply varies by orders
  of magnitude.
- **Ochoa-Tocachi et al. (2019)**, *Nature Sustainability* 2, 584-593:
  the real, still-operating pre-Inca "amuna" infiltration system near
  Lima, Peru — 14-244 day retention (mean 45 days), a huge and
  site-specific 3%-554% modeled dry-season flow increase at the study
  site, and a more representative 7.5% baseflow increase when upscaled
  to the whole Rímac catchment.
- **Jodar et al. (2022)**, *Science of the Total Environment* 825,
  153937: the real, still-operating "acequias de careo" system in
  Spain's Sierra Nevada — a semi-arid, high-mountain watershed, the
  closest real-world MAR analogue to an Alpine setting found in this
  survey — increases total aquifer recharge by 92%.
- **Jin, Hu, Ziegler et al. (2023)**, *Nature Sustainability* 6,
  865-874, and **Ilgen et al. (2024)**, *Hydrological Sciences Journal*
  69(6): floating-solar evaporation mitigation is real and documented
  (general literature range 28%-60%; Aswan High Dam's 90%-coverage case
  study reaches 49.7%, saving up to 5.9 billion m³/yr) — but highly
  coverage- and climate-dependent; there is no single universal
  percentage.
- **The mass-balance ceiling itself** (`mass_balance.py`): a redistribution
  network cannot create new water, only time-shift what already fell as
  precipitation upstream. `full_replacement_is_possible()` returns
  `False` unconditionally — this is a physical argument, not a modeling
  assumption that could be tuned away.

## Optional tier — weakly sourced or speculative, always flagged

- **`peatland.py`'s storage-capacity range (650-6092 m³/ha)** mixes a
  weak citation (a legal-decision document, not a primary hydrology
  study, for the 650 figure) with a real but non-Alpine measurement
  (Brazilian tropical peatland, for the 6092 figure). Neither number
  should be used to size a real Alpine peatland-restoration project.
  The emissions and cost ranges in the same module are order-of-magnitude
  figures carried over from the source report, not independently
  re-verified this session.
- **`rrf.py`'s "Resilience Replacement Factor" and its three named
  scenarios (I/II/III)** are **not a peer-reviewed metric**. They
  originate entirely from the AI DeepResearch report this package was
  built from; the formula's own figures in that report carry no primary
  citation, and the scenario RRF ranges (<0.1, 0.4-0.6, 0.7-0.85) are
  that report's own synthesis judgment, not a measurement. This mirrors
  how "CREP" started elsewhere in this ecosystem as an AI relabeling of
  existing concepts rather than an external validated metric — see this
  ecosystem's `feedback_utac_crep_prevalence_not_validation` note. Every
  function in `rrf.py` is exported alongside `RRF_NOT_PEER_REVIEWED_WARNING`.
  All three scenario presets are hard-constrained (tested) to never
  claim an RRF >= 1.0, consistent with `full_replacement_is_possible()`.

## What this is NOT

- **Not a claim that AGBR can fully replace a glacier.** The core tier's
  own headline number (65% ceiling, before sedimentation/evaporation
  losses) already rules that out — see `mass_balance.py` and Chapter 8
  of the source DeepResearch report ("Falsifikation der Ersatz-Hypothese").
- **No UTAC/CREP/AFET bridge.** This is a real, standalone hydrology and
  water-infrastructure topic; the cited papers already provide the
  relevant quantitative structure without this ecosystem's cross-domain
  vocabulary.

## References

- Farinotti, D., Pistocchi, A., Huss, M. (2016). *Environmental Research
  Letters*, 11(5), 054022. DOI: 10.1088/1748-9326/11/5/054022.
- Steffen, T., Huss, M., Estermann, R., Hodel, E., Farinotti, D. (2022).
  *Earth Surface Dynamics*, 10, 723-741. DOI: 10.5194/esurf-10-723-2022.
- Fabbri, S.C., Haas, I., Kremer, K., Motta, D., Girardclos, S.,
  Anselmetti, F.S. (2021). *Swiss Journal of Geosciences*, 114, 22. DOI:
  10.1186/s00015-021-00399-1.
- Ochoa-Tocachi, B.F., Bardales, J.D., Antiporta, J., Perez, K., Acosta,
  L., Mao, F., Zulkafli, Z., Gil-Rios, J., Angulo, O., Grainger, S.,
  Gammie, G., De Bievre, B., Buytaert, W. (2019). *Nature Sustainability*,
  2, 584-593. DOI: 10.1038/s41893-019-0307-1.
- Jodar, J., Zakaluk, T., Gonzalez-Ramon, A., Ruiz-Constan, A.,
  Marin-Lechado, C., Custodio, E., Urrutia, J., Herrera, C., Lamban, L.,
  Duran, J., Martos-Rosillo, S. (2022). *Science of the Total
  Environment*, 825, 153937. DOI: 10.1016/j.scitotenv.2022.153937.
- Jin, Y., Hu, S., Ziegler, A.D. et al. (2023). *Nature Sustainability*,
  6, 865-874. DOI: 10.1038/s41893-023-01089-6.
- Ilgen, K. et al. (2024). *Hydrological Sciences Journal*, 69(6). DOI:
  10.1080/02626667.2024.2332625.

Core-tier citations verified directly (2026-08-10) via WebSearch/WebFetch
against publisher pages, DOI records, or institutional press summaries.
Originating dialogue and report: `Großwasserbassins.txt` (Johann + Grok +
ChatGPT) and `Ersatz alpiner Gletscherpuffer.md` (GeminiDeepResearch).
