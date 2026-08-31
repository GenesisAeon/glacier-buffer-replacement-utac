"""glacier-buffer-replacement-utac -- Artificial Glacier Buffer Replacement (AGBR) science.

GenesisAeon Package 100. Companion to glacier-buffer-utac (P99, the loss
side); this package covers the replacement/mitigation side. Deliberately
has no UTAC/CREP/AFET bridge -- see DISCLAIMER.md.

Two explicit confidence tiers, kept separate in every module:
- CORE (reservoir, mar, evaporation, mass_balance): real, peer-reviewed
  findings independently re-verified 2026-08-10.
- OPTIONAL/SPECULATIVE (peatland, rrf): weakly sourced or literally
  unpublished metrics, always exposed with an explicit warning constant.
"""

from .constants import (
    ACEQUIAS_RECHARGE_INCREASE_PCT,
    ASWAN_EVAPORATION_REDUCTION_PCT_AT_90PCT_COVERAGE,
    FABBRI_2021_CITATION,
    FARINOTTI_2016_CITATION,
    JODAR_2022_CITATION,
    MAR_RETENTION_DAYS_MEAN,
    MAX_SUMMER_DEFICIT_MITIGATION_FRACTION,
    OCHOA_TOCACHI_2019_CITATION,
    PACKAGE_ID,
    POTENTIAL_LAKE_COUNT,
    POTENTIAL_LAKE_VOLUME_KM3,
    STEFFEN_2022_CITATION,
)
from .evaporation import (
    aswan_case_study,
    evaporation_reduction_pct_range,
    pv_yield_boost_pct_range,
)
from .mar import (
    amuna_dry_season_flow_increase_pct_range,
    amuna_retention_days_mean,
    amuna_retention_days_range,
    lima_catchment_baseflow_increase_pct,
    sierra_nevada_recharge_increase_pct,
)
from .mass_balance import (
    full_replacement_is_possible,
    irrecoverable_deficit_fraction,
    theoretical_mitigation_ceiling,
)
from .peatland import (
    WEAK_SOURCE_WARNING as PEATLAND_WEAK_SOURCE_WARNING,
)
from .peatland import (
    drained_peatland_emissions_tco2_per_ha_per_yr_range,
    restoration_cost_eur_per_ha_range,
    storage_capacity_m3_per_ha_range,
)
from .reservoir import (
    SWISS_ALPS_LAKE_POTENTIAL,
    ProglacialLakePotential,
    remaining_usable_volume_fraction,
    sediment_volume_loss_from_mass_input_m3,
    sedimentation_volume_loss_m3,
    volume_realized_km3,
)
from .rrf import (
    ALL_SCENARIOS,
    RRF_NOT_PEER_REVIEWED_WARNING,
    SCENARIO_I_LAISSEZ_FAIRE,
    SCENARIO_II_TECHNO_CENTRIC,
    SCENARIO_III_HYBRID_AGBR,
    ScenarioPreset,
    resilience_replacement_factor,
)

__version__ = "1.1.1"

__all__ = [
    "ACEQUIAS_RECHARGE_INCREASE_PCT",
    "ALL_SCENARIOS",
    "ASWAN_EVAPORATION_REDUCTION_PCT_AT_90PCT_COVERAGE",
    "FABBRI_2021_CITATION",
    "FARINOTTI_2016_CITATION",
    "JODAR_2022_CITATION",
    "MAR_RETENTION_DAYS_MEAN",
    "MAX_SUMMER_DEFICIT_MITIGATION_FRACTION",
    "OCHOA_TOCACHI_2019_CITATION",
    "PACKAGE_ID",
    "PEATLAND_WEAK_SOURCE_WARNING",
    "POTENTIAL_LAKE_COUNT",
    "POTENTIAL_LAKE_VOLUME_KM3",
    "RRF_NOT_PEER_REVIEWED_WARNING",
    "SCENARIO_I_LAISSEZ_FAIRE",
    "SCENARIO_II_TECHNO_CENTRIC",
    "SCENARIO_III_HYBRID_AGBR",
    "STEFFEN_2022_CITATION",
    "SWISS_ALPS_LAKE_POTENTIAL",
    "ProglacialLakePotential",
    "ScenarioPreset",
    "amuna_dry_season_flow_increase_pct_range",
    "amuna_retention_days_mean",
    "amuna_retention_days_range",
    "aswan_case_study",
    "drained_peatland_emissions_tco2_per_ha_per_yr_range",
    "evaporation_reduction_pct_range",
    "full_replacement_is_possible",
    "irrecoverable_deficit_fraction",
    "lima_catchment_baseflow_increase_pct",
    "pv_yield_boost_pct_range",
    "remaining_usable_volume_fraction",
    "resilience_replacement_factor",
    "restoration_cost_eur_per_ha_range",
    "sediment_volume_loss_from_mass_input_m3",
    "sedimentation_volume_loss_m3",
    "sierra_nevada_recharge_increase_pct",
    "storage_capacity_m3_per_ha_range",
    "theoretical_mitigation_ceiling",
    "volume_realized_km3",
]
