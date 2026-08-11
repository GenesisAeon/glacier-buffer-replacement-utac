"""Verified constants for artificial-glacier-buffer-replacement (AGBR) science.

Two confidence tiers, kept explicitly separate throughout this package:

- CORE: real, peer-reviewed findings independently re-verified via direct
  paper/DOI lookup on 2026-08-10 (not merely copied from the originating
  GeminiDeepResearch report "Ersatz alpiner Gletscherpuffer.md").
- OPTIONAL/SPECULATIVE (see peatland.py and rrf.py): weakly sourced or
  literally unpublished metrics, kept only because they were the object
  of the original discussion -- always exposed with an explicit warning.
"""

PACKAGE_ID = 100

# =====================================================================
# CORE -- independently re-verified 2026-08-10
# =====================================================================

# --- Farinotti, Pistocchi & Huss 2016: the ceiling on what reservoirs can do ---

FARINOTTI_2016_CITATION = (
    "Farinotti, D., Pistocchi, A., Huss, M. (2016). From dwindling ice to "
    "headwater lakes: could dams replace glaciers in the European Alps? "
    "Environmental Research Letters, 11(5), 054022. "
    "DOI: 10.1088/1748-9326/11/5/054022"
)
FARINOTTI_2016_DOI = "10.1088/1748-9326/11/5/054022"

# Fraction of the projected end-of-century summer-runoff change from
# presently glacierized surfaces that a dam/reservoir strategy could
# offset, per Farinotti et al. (2016). Verified directly against the
# paper's own press summary (WSL, 2026-08-10): "up to 65%".
MAX_SUMMER_DEFICIT_MITIGATION_FRACTION = 0.65

FARINOTTI_NOTE = (
    "Farinotti et al. (2016) is the peer-reviewed origin of the '65%' "
    "figure quoted throughout the AGBR discussion. It is a ceiling, not a "
    "guarantee: it assumes reservoirs are actually built at the right "
    "deglaciating sites and does not account for the sedimentation, "
    "evaporation and social-acceptance losses this package documents "
    "separately. It is also explicitly a partial mitigation of the "
    "*change* in summer runoff, not a full replacement of glacier "
    "hydrology -- see mass_balance.py."
)

# --- Steffen, Huss, Estermann, Hodel & Farinotti 2022: proglacial lakes ---

STEFFEN_2022_CITATION = (
    "Steffen, T., Huss, M., Estermann, R., Hodel, E., Farinotti, D. "
    "(2022). Volume, evolution, and sedimentation of future glacier lakes "
    "in Switzerland over the 21st century. Earth Surface Dynamics, 10, "
    "723-741. DOI: 10.5194/esurf-10-723-2022"
)
STEFFEN_2022_DOI = "10.5194/esurf-10-723-2022"

# Potential new proglacial lakes in the Swiss Alps (min. 5000 m^2, >5 m deep)
POTENTIAL_LAKE_COUNT = 683
POTENTIAL_LAKE_VOLUME_KM3 = 1.16
POTENTIAL_LAKE_VOLUME_KM3_RANGE = (1.05, 1.32)

# Under a "middle-of-the-road" climate scenario, only a fraction of that
# potential volume actually exists at a given point in time -- it forms
# gradually as glaciers retreat.
REALIZED_LAKE_VOLUME_FRACTION_BY_2050 = 0.10
REALIZED_LAKE_VOLUME_FRACTION_BY_2100 = 0.48

STEFFEN_NOTE = (
    "The often-quoted '683 new lakes / 1.16 km3' figure is the *total "
    "long-term potential*, not a volume available today or even by 2100: "
    "Steffen et al. (2022) project only ~10% realized by 2050 and ~48% by "
    "2100 under a middle-of-the-road scenario. Citing the full 1.16 km3 "
    "as near-term available storage (as casual summaries sometimes do) "
    "overstates the near-term picture."
)

# Bulk density of deposited glaciolacustrine sediment, kg/m^3 -- used to
# convert a sediment MASS input rate into a volume-loss rate (see
# reservoir.sediment_volume_loss_from_mass_input_m3). Attributed to the
# same Steffen et al. (2022) source as the proglacial-lake figures above;
# this specific density value was not independently re-verified in a
# fresh 2026-08-11 lookup (added 2026-08-11 from a later revision of the
# AGBR source report, "Ersatz alpiner Gletscherpuffer+AuswirkungenTektonik.md",
# section 4.2) -- treat it as documented, not re-confirmed.
SEDIMENT_DENSITY_KG_PER_M3 = 2200.0

# --- Fabbri, Haas, Kremer, Motta, Girardclos & Anselmetti 2021: sedimentation ---

FABBRI_2021_CITATION = (
    "Fabbri, S.C., Haas, I., Kremer, K., Motta, D., Girardclos, S., "
    "Anselmetti, F.S. (2021). Subaqueous geomorphology and delta dynamics "
    "of Lake Brienz (Switzerland): implications for the sediment budget "
    "in the alpine realm. Swiss Journal of Geosciences, 114, 22. "
    "DOI: 10.1186/s00015-021-00399-1"
)
FABBRI_2021_DOI = "10.1186/s00015-021-00399-1"

# Lake Brienz basin-plain sedimentation rate, 2003-2018, cm/year
BRIENZ_SEDIMENTATION_RATE_CM_PER_YR_AVG = 3.0
BRIENZ_SEDIMENTATION_RATE_CM_PER_YR_MIN = 2.0  # central basin
BRIENZ_SEDIMENTATION_RATE_CM_PER_YR_MAX = 4.7  # delta-proximal
# Historic (pre-2003) rate at the same lake, per Anselmetti et al. (2007),
# as reported inside Fabbri et al. (2021)
BRIENZ_HISTORIC_RATE_CM_PER_YR_1996_2003 = (1.1, 1.6)

SEDIMENTATION_NOTE = (
    "Lake Brienz's basin-plain rate (3.0 cm/yr average, up to 4.7 cm/yr "
    "near deltas) is 'extraordinarily high' even among Alpine lakes and "
    "was partly inflated by the exceptional 2005 flood in the measurement "
    "window. Treat it as a realistic worst-case for a glacially-fed "
    "proglacial reservoir, not a universal constant -- basin-specific "
    "sediment supply varies by orders of magnitude."
)

# --- Ochoa-Tocachi et al. 2019: pre-Inca Amuna infiltration (MAR) ---

OCHOA_TOCACHI_2019_CITATION = (
    "Ochoa-Tocachi, B.F., Bardales, J.D., Antiporta, J., Perez, K., "
    "Acosta, L., Mao, F., Zulkafli, Z., Gil-Rios, J., Angulo, O., "
    "Grainger, S., Gammie, G., De Bievre, B., Buytaert, W. (2019). "
    "Potential contributions of pre-Inca infiltration infrastructure to "
    "Andean water security. Nature Sustainability, 2, 584-593. "
    "DOI: 10.1038/s41893-019-0307-1"
)
OCHOA_TOCACHI_2019_DOI = "10.1038/s41893-019-0307-1"

# Water-tracer retention time through the Huamantanga amuna system, days
MAR_RETENTION_DAYS_MIN = 14  # 2 weeks
MAR_RETENTION_DAYS_MAX = 244  # ~8 months
MAR_RETENTION_DAYS_MEAN = 45

# Modeled dry-season flow increase at Huamantanga, percent (huge, site-specific range)
MAR_DRY_SEASON_FLOW_INCREASE_PCT_MIN = 3.0
MAR_DRY_SEASON_FLOW_INCREASE_PCT_MAX = 554.0

# Upscaled estimate for Lima's Rimac catchment: increase in dry-season baseflow, percent
MAR_LIMA_BASEFLOW_INCREASE_PCT = 7.5

MAR_NOTE = (
    "The 3%-554% dry-season flow increase range is a real modeled range "
    "for the single Huamantanga study site, not a general MAR "
    "'effectiveness' statistic -- it spans small tributaries to nearly-dry "
    "channels where any infiltrated water is a huge relative increase. "
    "The 7.5% Lima-catchment figure is the more representative number "
    "for basin-scale planning."
)

# --- Jodar et al. 2022: acequias de careo (Sierra Nevada, Spain) ---

JODAR_2022_CITATION = (
    "Jodar, J., Zakaluk, T., Gonzalez-Ramon, A., Ruiz-Constan, A., "
    "Marin-Lechado, C., Custodio, E., Urrutia, J., Herrera, C., Lamban, "
    "L., Duran, J., Martos-Rosillo, S. (2022). Artificial recharge by "
    "means of careo channels versus natural aquifer recharge in a "
    "semi-arid, high-mountain watershed (Sierra Nevada, Spain). Science "
    "of the Total Environment, 825, 153937. "
    "DOI: 10.1016/j.scitotenv.2022.153937"
)
JODAR_2022_DOI = "10.1016/j.scitotenv.2022.153937"

# Increase in total aquifer recharge attributable to the careo channel system, percent
ACEQUIAS_RECHARGE_INCREASE_PCT = 92.0
# Share of total recharge from the artificial channels vs. natural infiltration, percent
ACEQUIAS_ARTIFICIAL_SHARE_PCT = 48.0
ACEQUIAS_NATURAL_SHARE_PCT = 52.0

# --- Jin, Hu, Ziegler et al. 2023 + Ilgen et al. 2024: floating solar / evaporation ---

JIN_2023_CITATION = (
    "Jin, Y., Hu, S., Ziegler, A.D. et al. (2023). Energy production and "
    "water savings from floating solar photovoltaics on global "
    "reservoirs. Nature Sustainability, 6, 865-874. "
    "DOI: 10.1038/s41893-023-01089-6"
)
JIN_2023_DOI = "10.1038/s41893-023-01089-6"

ILGEN_2024_CITATION = (
    "Ilgen, K. et al. (2024). Evaporation reduction and energy generation "
    "potential using floating photovoltaic power plants on the Aswan "
    "High Dam Reservoir. Hydrological Sciences Journal, 69(6). "
    "DOI: 10.1080/02626667.2024.2332625"
)
ILGEN_2024_DOI = "10.1080/02626667.2024.2332625"

# Documented range of evaporation reduction from floating PV coverage, percent
FLOATING_SOLAR_EVAPORATION_REDUCTION_PCT_RANGE = (28.0, 60.0)
# Case study: Aswan High Dam Reservoir at 90% FPV occupancy, percent
ASWAN_EVAPORATION_REDUCTION_PCT_AT_90PCT_COVERAGE = 49.7
ASWAN_WATER_SAVINGS_BILLION_M3_PER_YR = 5.9

# Documented range of PV energy-yield boost from water cooling, percent
FLOATING_SOLAR_PV_YIELD_BOOST_PCT_RANGE = (3.0, 15.0)

FLOATING_SOLAR_NOTE = (
    "Evaporation-reduction figures for floating solar vary hugely with "
    "coverage fraction, climate and reservoir shape (28%-60% in the "
    "general literature, up to 49.7% at Aswan's 90% coverage case study). "
    "There is no single 'floating solar reduces evaporation by X%' "
    "constant -- treat any single number as coverage- and site-specific."
)

# =====================================================================
# OPTIONAL / WEAKLY SOURCED -- real numbers, but NOT independently
# re-verified this session, and/or sourced from non-primary-research
# documents. See peatland.py. Exposed for completeness, not load-bearing.
# =====================================================================

# Peatland/moor water storage capacity, m3 per hectare. The low end is a
# general rewetting reference figure cited (in the source DeepResearch
# report) from a court-decision document, not a primary hydrology study --
# a weak citation chain. The high end (Pau-de-Fruta, Brazil) is a real
# peer-reviewed measurement, but of a *tropical* deep peatland, not an
# Alpine bog -- storage capacity per hectare is not directly transferable
# across those two peat types/climates.
PEATLAND_STORAGE_M3_PER_HA_LOW_WEAK_SOURCE = 650.0
PEATLAND_STORAGE_M3_PER_HA_HIGH_NON_ALPINE = 6092.0

PEATLAND_STORAGE_NOTE = (
    "Do not treat (650, 6092) as an Alpine-bog storage range. 650 m3/ha "
    "traces to a legal-decision document cited in the source report, not "
    "a primary hydrology study; 6092 m3/ha is a real measurement but from "
    "a Brazilian tropical peatland (Pau-de-Fruta), not an Alpine one. "
    "Both are kept here only because the source report used them -- "
    "neither should be used to size a real Alpine restoration project "
    "without finding an Alpine-specific source first."
)

# Order-of-magnitude range for CO2-equivalent emissions from a drained,
# agriculturally-used peatland, t CO2e per hectare per year. Widely
# reported in peatland-drainage literature (consistent with IPCC Wetlands
# Supplement order-of-magnitude estimates); not tied to a single paper
# and not independently re-verified this session.
DRAINED_PEATLAND_EMISSIONS_TCO2_PER_HA_PER_YR_RANGE = (30.0, 40.0)

# Peatland restoration cost, EUR per hectare (as reported in the source
# report; not independently re-verified this session)
PEATLAND_RESTORATION_COST_EUR_PER_HA_RANGE = (1000.0, 17000.0)
