"""Managed Aquifer Recharge (MAR) — Amuna and acequia-de-careo evidence.

Core module -- Ochoa-Tocachi et al. (2019) for the Peruvian amuna system,
Jodar et al. (2022) for the Sierra Nevada acequias de careo. Both are
real, independently operating pre-industrial infiltration systems, not
speculative proposals -- they are cited here as evidence that MAR at
this scale works, not as a direct Alpine calibration.
"""

from __future__ import annotations

from .constants import (
    ACEQUIAS_RECHARGE_INCREASE_PCT,
    JODAR_2022_CITATION,
    MAR_DRY_SEASON_FLOW_INCREASE_PCT_MAX,
    MAR_DRY_SEASON_FLOW_INCREASE_PCT_MIN,
    MAR_LIMA_BASEFLOW_INCREASE_PCT,
    MAR_RETENTION_DAYS_MAX,
    MAR_RETENTION_DAYS_MEAN,
    MAR_RETENTION_DAYS_MIN,
    OCHOA_TOCACHI_2019_CITATION,
)


def amuna_retention_days_range() -> tuple[int, int]:
    """Documented (min, max) water-tracer retention time through the amuna system, days."""
    return (MAR_RETENTION_DAYS_MIN, MAR_RETENTION_DAYS_MAX)


def amuna_retention_days_mean() -> int:
    """Documented mean water-tracer retention time through the amuna system, days."""
    return MAR_RETENTION_DAYS_MEAN


def amuna_dry_season_flow_increase_pct_range() -> tuple[float, float]:
    """Documented (min, max) modeled dry-season flow increase at the Huamantanga site.

    This is a real but extreme, site-specific range (small/near-dry
    tributaries at the high end) -- see MAR_NOTE in constants.py before
    using the upper bound for planning.
    """
    return (MAR_DRY_SEASON_FLOW_INCREASE_PCT_MIN, MAR_DRY_SEASON_FLOW_INCREASE_PCT_MAX)


def lima_catchment_baseflow_increase_pct() -> float:
    """Upscaled dry-season baseflow increase estimate for Lima's Rimac catchment, percent."""
    return MAR_LIMA_BASEFLOW_INCREASE_PCT


def sierra_nevada_recharge_increase_pct() -> float:
    """Aquifer recharge increase attributable to the acequia-de-careo system, percent.

    Jodar et al. (2022): the careo channel system increases total
    aquifer recharge by 92% relative to natural infiltration alone, in a
    semi-arid, high-mountain (Sierra Nevada, Spain) watershed -- the
    closest real-world MAR analogue to an Alpine setting in the
    literature surveyed here.
    """
    return ACEQUIAS_RECHARGE_INCREASE_PCT


MAR_EVIDENCE_CITATIONS = (OCHOA_TOCACHI_2019_CITATION, JODAR_2022_CITATION)
