"""Proglacial reservoir potential and sedimentation-driven volume loss.

Core module -- Steffen et al. (2022) for the lake-formation timeline,
Fabbri et al. (2021) for real Alpine sedimentation rates.
"""

from __future__ import annotations

from dataclasses import dataclass

from .constants import (
    BRIENZ_SEDIMENTATION_RATE_CM_PER_YR_AVG,
    POTENTIAL_LAKE_COUNT,
    POTENTIAL_LAKE_VOLUME_KM3,
    POTENTIAL_LAKE_VOLUME_KM3_RANGE,
    REALIZED_LAKE_VOLUME_FRACTION_BY_2050,
    REALIZED_LAKE_VOLUME_FRACTION_BY_2100,
    STEFFEN_2022_CITATION,
)


@dataclass(frozen=True)
class ProglacialLakePotential:
    """Swiss-Alps-wide proglacial lake potential per Steffen et al. (2022)."""

    count: int
    total_volume_km3: float
    total_volume_km3_range: tuple[float, float]
    realized_fraction_by_2050: float
    realized_fraction_by_2100: float
    citation: str


SWISS_ALPS_LAKE_POTENTIAL = ProglacialLakePotential(
    count=POTENTIAL_LAKE_COUNT,
    total_volume_km3=POTENTIAL_LAKE_VOLUME_KM3,
    total_volume_km3_range=POTENTIAL_LAKE_VOLUME_KM3_RANGE,
    realized_fraction_by_2050=REALIZED_LAKE_VOLUME_FRACTION_BY_2050,
    realized_fraction_by_2100=REALIZED_LAKE_VOLUME_FRACTION_BY_2100,
    citation=STEFFEN_2022_CITATION,
)


def volume_realized_km3(year: int) -> float:
    """Interpolate realized proglacial-lake volume for a target year.

    Piecewise-linear interpolation between Steffen et al. (2022)'s three
    documented anchor points (0% at 2022 baseline, 10% by 2050, 48% by
    2100) under their middle-of-the-road scenario. This is a simplifying
    interpolation for planning purposes, not a re-run of their glacier
    evolution model -- do not use it in place of the original study for
    a specific sub-basin.
    """
    if year < 2022:
        raise ValueError(f"year must be >= 2022 (study baseline), got {year}")
    anchors = (
        (2022, 0.0),
        (2050, REALIZED_LAKE_VOLUME_FRACTION_BY_2050),
        (2100, REALIZED_LAKE_VOLUME_FRACTION_BY_2100),
    )
    if year >= 2100:
        fraction = REALIZED_LAKE_VOLUME_FRACTION_BY_2100
    else:
        for (y0, f0), (y1, f1) in zip(anchors, anchors[1:], strict=True):
            if y0 <= year <= y1:
                fraction = f0 + (f1 - f0) * (year - y0) / (y1 - y0)
                break
    return fraction * POTENTIAL_LAKE_VOLUME_KM3


def sedimentation_volume_loss_m3(
    surface_area_m2: float,
    years: float,
    rate_cm_per_yr: float = BRIENZ_SEDIMENTATION_RATE_CM_PER_YR_AVG,
) -> float:
    """Cumulative reservoir volume lost to sedimentation over a period.

    Simple area x depth-rate x time model, calibrated with Lake Brienz's
    real basin-plain rate as the default. Real sedimentation is not
    linear (it depends on upstream sediment supply, which itself changes
    as a glacier retreats), so this is a first-order estimate, not a
    sediment-transport simulation.
    """
    if surface_area_m2 <= 0:
        raise ValueError(f"surface_area_m2 must be positive, got {surface_area_m2}")
    if years < 0:
        raise ValueError(f"years must be non-negative, got {years}")
    rate_m_per_yr = rate_cm_per_yr / 100.0
    return surface_area_m2 * rate_m_per_yr * years


def remaining_usable_volume_fraction(
    initial_volume_m3: float,
    surface_area_m2: float,
    years: float,
    rate_cm_per_yr: float = BRIENZ_SEDIMENTATION_RATE_CM_PER_YR_AVG,
) -> float:
    """Fraction of a reservoir's initial volume still usable after sedimentation.

    Clamped to [0, 1]: a reservoir cannot lose more than 100% of its
    volume to sedimentation in this simplified model (in reality it would
    be decommissioned well before that point).
    """
    if initial_volume_m3 <= 0:
        raise ValueError(f"initial_volume_m3 must be positive, got {initial_volume_m3}")
    lost = sedimentation_volume_loss_m3(surface_area_m2, years, rate_cm_per_yr)
    remaining = (initial_volume_m3 - lost) / initial_volume_m3
    return max(0.0, min(1.0, remaining))
