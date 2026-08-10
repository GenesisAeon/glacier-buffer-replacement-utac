"""Tests for glacier-buffer-replacement-utac."""

import pytest

from glacier_buffer_replacement_utac import (
    ALL_SCENARIOS,
    MAX_SUMMER_DEFICIT_MITIGATION_FRACTION,
    PACKAGE_ID,
    PEATLAND_WEAK_SOURCE_WARNING,
    RRF_NOT_PEER_REVIEWED_WARNING,
    SWISS_ALPS_LAKE_POTENTIAL,
    __version__,
    amuna_dry_season_flow_increase_pct_range,
    amuna_retention_days_mean,
    amuna_retention_days_range,
    aswan_case_study,
    drained_peatland_emissions_tco2_per_ha_per_yr_range,
    evaporation_reduction_pct_range,
    full_replacement_is_possible,
    irrecoverable_deficit_fraction,
    lima_catchment_baseflow_increase_pct,
    pv_yield_boost_pct_range,
    remaining_usable_volume_fraction,
    resilience_replacement_factor,
    restoration_cost_eur_per_ha_range,
    sedimentation_volume_loss_m3,
    sierra_nevada_recharge_increase_pct,
    storage_capacity_m3_per_ha_range,
    theoretical_mitigation_ceiling,
    volume_realized_km3,
)


def test_version():
    assert __version__ == "1.0.0"


def test_package_id():
    assert PACKAGE_ID == 100


# --- mass_balance.py (core) ---------------------------------------------


def test_full_replacement_is_never_possible():
    assert full_replacement_is_possible() is False


def test_theoretical_mitigation_ceiling():
    assert theoretical_mitigation_ceiling() == 0.65
    value, citation = theoretical_mitigation_ceiling(with_citation=True)
    assert value == 0.65
    assert "Farinotti" in citation


def test_irrecoverable_deficit_fraction():
    assert irrecoverable_deficit_fraction() == pytest.approx(0.35)
    assert irrecoverable_deficit_fraction() == pytest.approx(
        1.0 - MAX_SUMMER_DEFICIT_MITIGATION_FRACTION
    )


# --- reservoir.py (core) --------------------------------------------------


def test_swiss_alps_lake_potential():
    assert SWISS_ALPS_LAKE_POTENTIAL.count == 683
    assert SWISS_ALPS_LAKE_POTENTIAL.total_volume_km3 == pytest.approx(1.16)
    assert SWISS_ALPS_LAKE_POTENTIAL.realized_fraction_by_2050 == pytest.approx(0.10)
    assert SWISS_ALPS_LAKE_POTENTIAL.realized_fraction_by_2100 == pytest.approx(0.48)
    assert SWISS_ALPS_LAKE_POTENTIAL.citation


def test_volume_realized_km3_grows_over_time():
    early = volume_realized_km3(2030)
    mid = volume_realized_km3(2060)
    late = volume_realized_km3(2100)
    assert 0.0 <= early < mid < late
    assert late == pytest.approx(1.16 * 0.48)


def test_volume_realized_km3_rejects_pre_baseline_year():
    with pytest.raises(ValueError, match="2022"):
        volume_realized_km3(2000)


def test_volume_realized_km3_caps_after_2100():
    assert volume_realized_km3(2150) == volume_realized_km3(2100)


def test_sedimentation_volume_loss_scales_with_area_and_time():
    loss_10y = sedimentation_volume_loss_m3(surface_area_m2=1_000_000, years=10)
    loss_20y = sedimentation_volume_loss_m3(surface_area_m2=1_000_000, years=20)
    assert loss_20y == pytest.approx(2 * loss_10y)
    # 1 km^2 at Brienz's real 3.0 cm/yr (0.03 m/yr) average, 10 years -> 300,000 m^3
    assert loss_10y == pytest.approx(300_000.0)


def test_sedimentation_volume_loss_rejects_bad_input():
    with pytest.raises(ValueError, match="positive"):
        sedimentation_volume_loss_m3(surface_area_m2=0, years=10)
    with pytest.raises(ValueError, match="non-negative"):
        sedimentation_volume_loss_m3(surface_area_m2=1000, years=-1)


def test_remaining_usable_volume_fraction_clamped_to_zero():
    fraction = remaining_usable_volume_fraction(
        initial_volume_m3=1000,
        surface_area_m2=1_000_000_000,
        years=1000,
    )
    assert fraction == 0.0


def test_remaining_usable_volume_fraction_rejects_bad_initial_volume():
    with pytest.raises(ValueError, match="positive"):
        remaining_usable_volume_fraction(initial_volume_m3=0, surface_area_m2=1000, years=1)


def test_remaining_usable_volume_fraction_at_zero_years():
    assert remaining_usable_volume_fraction(
        initial_volume_m3=1000, surface_area_m2=1_000_000, years=0
    ) == pytest.approx(1.0)


# --- mar.py (core) ---------------------------------------------------------


def test_amuna_retention_days():
    assert amuna_retention_days_range() == (14, 244)
    assert amuna_retention_days_mean() == 45


def test_amuna_dry_season_flow_increase_range():
    low, high = amuna_dry_season_flow_increase_pct_range()
    assert low == pytest.approx(3.0)
    assert high == pytest.approx(554.0)


def test_lima_catchment_baseflow_increase_pct():
    assert lima_catchment_baseflow_increase_pct() == pytest.approx(7.5)


def test_sierra_nevada_recharge_increase_pct():
    assert sierra_nevada_recharge_increase_pct() == pytest.approx(92.0)


# --- evaporation.py (core) --------------------------------------------------


def test_evaporation_reduction_pct_range():
    low, high = evaporation_reduction_pct_range()
    assert 0.0 < low < high < 100.0


def test_aswan_case_study():
    case = aswan_case_study()
    assert case["coverage_pct"] == 90.0
    assert case["evaporation_reduction_pct"] == pytest.approx(49.7)
    assert case["citation"]


def test_pv_yield_boost_pct_range():
    low, high = pv_yield_boost_pct_range()
    assert 0.0 < low < high


# --- peatland.py (optional / weakly sourced) --------------------------------


def test_peatland_weak_source_warning_present():
    assert "not" in PEATLAND_WEAK_SOURCE_WARNING.lower()
    assert "Alpine" in PEATLAND_WEAK_SOURCE_WARNING


def test_storage_capacity_m3_per_ha_range():
    low, high = storage_capacity_m3_per_ha_range()
    assert low == pytest.approx(650.0)
    assert high == pytest.approx(6092.0)


def test_drained_peatland_emissions_range():
    low, high = drained_peatland_emissions_tco2_per_ha_per_yr_range()
    assert low == pytest.approx(30.0)
    assert high == pytest.approx(40.0)


def test_restoration_cost_range():
    low, high = restoration_cost_eur_per_ha_range()
    assert low == pytest.approx(1000.0)
    assert high == pytest.approx(17000.0)


# --- rrf.py (speculative) ---------------------------------------------------


def test_rrf_warning_present_and_explicit():
    assert "NOT" in RRF_NOT_PEER_REVIEWED_WARNING
    assert "peer-reviewed" in RRF_NOT_PEER_REVIEWED_WARNING.lower()


def test_resilience_replacement_factor_basic():
    rrf = resilience_replacement_factor(volume_restored_km3=0.65, volume_lost_km3=1.0)
    assert rrf == pytest.approx(0.65)


def test_resilience_replacement_factor_applies_weights():
    full = resilience_replacement_factor(
        volume_restored_km3=1.0, volume_lost_km3=1.0, timing_weight=0.5, thermal_elasticity=0.5
    )
    assert full == pytest.approx(0.25)


def test_resilience_replacement_factor_rejects_zero_loss():
    with pytest.raises(ValueError, match="positive"):
        resilience_replacement_factor(volume_restored_km3=1.0, volume_lost_km3=0.0)


def test_resilience_replacement_factor_rejects_negative_restored():
    with pytest.raises(ValueError, match="non-negative"):
        resilience_replacement_factor(volume_restored_km3=-1.0, volume_lost_km3=1.0)


def test_all_scenarios_count_and_order():
    names = [s.name for s in ALL_SCENARIOS]
    assert len(ALL_SCENARIOS) == 3
    assert "Laissez-faire" in names[0]
    assert "Techno-centric" in names[1]
    assert "Hybrid" in names[2]


def test_all_scenarios_rrf_ranges_are_monotonically_increasing():
    lows = [s.rrf_range[0] for s in ALL_SCENARIOS]
    highs = [s.rrf_range[1] for s in ALL_SCENARIOS]
    assert lows == sorted(lows)
    assert highs == sorted(highs)


def test_all_scenarios_never_claim_full_replacement():
    for scenario in ALL_SCENARIOS:
        assert scenario.rrf_range[1] < 1.0, (
            f"{scenario.name} claims RRF >= 1.0, contradicting "
            "full_replacement_is_possible() == False"
        )
