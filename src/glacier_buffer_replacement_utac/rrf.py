"""The 'Resilience Replacement Factor' (RRF) and its three scenarios.

SPECULATIVE module -- READ THIS BEFORE USING ANYTHING BELOW.

The RRF metric and the RRF ranges attached to the three named scenarios
(I/II/III) are NOT a peer-reviewed formula or literature-derived
statistic. They originate entirely from the GeminiDeepResearch report
"Ersatz alpiner Gletscherpuffer.md" that this package was built from --
the formula's own figures in that report carry no citation, and the
scenario RRF ranges are that report's own synthesis judgment, not a
measurement. This is analogous to how 'CREP' in other GenesisAeon
packages started as an AI relabeling of Johann's own concepts rather
than an established external metric -- see the ecosystem's
`feedback_utac_crep_prevalence_not_validation` note. Treat every
function in this module as an illustrative thought-experiment, not a
validated planning tool.
"""

from __future__ import annotations

from dataclasses import dataclass

RRF_NOT_PEER_REVIEWED_WARNING = (
    "The Resilience Replacement Factor (RRF) and the scenario RRF ranges "
    "below are this package's own construction, inherited from an AI "
    "DeepResearch report with no primary citation for the formula itself. "
    "They are NOT a peer-reviewed metric. Do not present RRF outputs as "
    "measured or literature-validated quantities."
)


def resilience_replacement_factor(
    volume_restored_km3: float,
    volume_lost_km3: float,
    timing_weight: float = 1.0,
    thermal_elasticity: float = 1.0,
) -> float:
    """Speculative RRF = (timing_weight * thermal_elasticity * volume_restored) / volume_lost.

    See RRF_NOT_PEER_REVIEWED_WARNING. `timing_weight` (how well a
    measure shifts water from spring into July-September) and
    `thermal_elasticity` (how reactive a measure is to a heat/drought
    anomaly) are both unitless illustrative multipliers in [0, 1] in the
    source report's own examples, not calibrated coefficients.
    """
    if volume_lost_km3 <= 0:
        raise ValueError(f"volume_lost_km3 must be positive, got {volume_lost_km3}")
    if volume_restored_km3 < 0:
        raise ValueError(f"volume_restored_km3 must be non-negative, got {volume_restored_km3}")
    return (timing_weight * thermal_elasticity * volume_restored_km3) / volume_lost_km3


@dataclass(frozen=True)
class ScenarioPreset:
    """One of the source report's three narrative AGBR scenarios (speculative)."""

    name: str
    climate_projection: str
    rrf_range: tuple[float, float]
    description: str


SCENARIO_I_LAISSEZ_FAIRE = ScenarioPreset(
    name="Laissez-faire / static infrastructure",
    climate_projection="RCP 8.5",
    rrf_range=(0.0, 0.1),
    description=(
        "No new storage, static rule curves, continued peatland "
        "degradation. Glacier volume down >90% by 2100 in this "
        "projection; summer runoff collapse after peak water."
    ),
)

SCENARIO_II_TECHNO_CENTRIC = ScenarioPreset(
    name="Techno-centric fixation / grey infrastructure",
    climate_projection="RCP 4.5",
    rrf_range=(0.4, 0.6),
    description=(
        "Maximal proglacial dam/reservoir build-out, no MAR or peatland "
        "measures. Sedimentation and evaporation losses drive a "
        "declining RRF over time even as built capacity grows."
    ),
)

SCENARIO_III_HYBRID_AGBR = ScenarioPreset(
    name="Hybrid system (AGBR concept)",
    climate_projection="RCP 2.6-4.5",
    rrf_range=(0.7, 0.85),
    description=(
        "Cascading network: selective proglacial reservoirs with "
        "floating solar, large-scale MAR, aggressive peatland "
        "rewetting, adaptive/algorithmic release control."
    ),
)

ALL_SCENARIOS: tuple[ScenarioPreset, ...] = (
    SCENARIO_I_LAISSEZ_FAIRE,
    SCENARIO_II_TECHNO_CENTRIC,
    SCENARIO_III_HYBRID_AGBR,
)
