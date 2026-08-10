"""Floating-solar evaporation mitigation for surface reservoirs.

Core module -- Jin et al. (2023) for the global picture, Ilgen et al.
(2024) for the Aswan High Dam case study (the highest-coverage,
best-documented single-site number found).
"""

from __future__ import annotations

from .constants import (
    ASWAN_EVAPORATION_REDUCTION_PCT_AT_90PCT_COVERAGE,
    ASWAN_WATER_SAVINGS_BILLION_M3_PER_YR,
    FLOATING_SOLAR_EVAPORATION_REDUCTION_PCT_RANGE,
    FLOATING_SOLAR_PV_YIELD_BOOST_PCT_RANGE,
    ILGEN_2024_CITATION,
    JIN_2023_CITATION,
)


def evaporation_reduction_pct_range() -> tuple[float, float]:
    """Documented general-literature range of evaporation reduction from floating PV, percent."""
    return FLOATING_SOLAR_EVAPORATION_REDUCTION_PCT_RANGE


def aswan_case_study() -> dict[str, float | str]:
    """The best-documented single-site floating-PV evaporation case study.

    Ilgen et al. (2024): at 90% floating-PV coverage of the Aswan High
    Dam Reservoir, modeled evaporation reduction is 49.7%, corresponding
    to up to 5.9 billion m3/year in water savings. Egypt's reservoir
    climate is hot and arid, not Alpine -- treat as an upper-bound
    demonstration of what high-coverage FPV can achieve, not an Alpine
    forecast.
    """
    return {
        "coverage_pct": 90.0,
        "evaporation_reduction_pct": ASWAN_EVAPORATION_REDUCTION_PCT_AT_90PCT_COVERAGE,
        "water_savings_billion_m3_per_yr": ASWAN_WATER_SAVINGS_BILLION_M3_PER_YR,
        "citation": ILGEN_2024_CITATION,
    }


def pv_yield_boost_pct_range() -> tuple[float, float]:
    """Documented range of PV energy-yield boost from water-surface cooling, percent."""
    return FLOATING_SOLAR_PV_YIELD_BOOST_PCT_RANGE


EVAPORATION_EVIDENCE_CITATIONS = (JIN_2023_CITATION, ILGEN_2024_CITATION)
