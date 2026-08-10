"""Peatland/moor storage as an AGBR component.

OPTIONAL / WEAKLY SOURCED module -- see PEATLAND_STORAGE_NOTE in
constants.py. The storage-capacity range mixes a legal-document citation
with a non-Alpine (Brazilian tropical) peat measurement; the emissions
and cost ranges are order-of-magnitude figures from the source report,
not independently re-verified this session. Kept because peatland
restoration was part of the original discussion, not because the
numbers meet this package's core evidentiary bar -- see DISCLAIMER.md.
"""

from __future__ import annotations

from .constants import (
    DRAINED_PEATLAND_EMISSIONS_TCO2_PER_HA_PER_YR_RANGE,
    PEATLAND_RESTORATION_COST_EUR_PER_HA_RANGE,
    PEATLAND_STORAGE_M3_PER_HA_HIGH_NON_ALPINE,
    PEATLAND_STORAGE_M3_PER_HA_LOW_WEAK_SOURCE,
    PEATLAND_STORAGE_NOTE,
)

WEAK_SOURCE_WARNING = PEATLAND_STORAGE_NOTE


def storage_capacity_m3_per_ha_range() -> tuple[float, float]:
    """Weakly-sourced (650, 6092) m3/ha range -- see WEAK_SOURCE_WARNING before use."""
    return (
        PEATLAND_STORAGE_M3_PER_HA_LOW_WEAK_SOURCE,
        PEATLAND_STORAGE_M3_PER_HA_HIGH_NON_ALPINE,
    )


def drained_peatland_emissions_tco2_per_ha_per_yr_range() -> tuple[float, float]:
    """Order-of-magnitude CO2e emissions range for a drained, agriculturally-used peatland."""
    return DRAINED_PEATLAND_EMISSIONS_TCO2_PER_HA_PER_YR_RANGE


def restoration_cost_eur_per_ha_range() -> tuple[float, float]:
    """As-reported peatland restoration cost range, EUR/ha (not independently re-verified)."""
    return PEATLAND_RESTORATION_COST_EUR_PER_HA_RANGE
