"""The physical ceiling on artificial glacier-buffer replacement.

Core module. Encodes the one argument in the source DeepResearch report
that needs no speculative metric to stand on its own: a reservoir/MAR/
peatland network can only redistribute existing water in time, it cannot
create new water. Farinotti et al. (2016) quantify the best-case ceiling
for the redistribution strategy; the remainder is categorically
unreachable by this class of intervention, no matter how well-executed.
"""

from __future__ import annotations

from .constants import (
    FARINOTTI_2016_CITATION,
    MAX_SUMMER_DEFICIT_MITIGATION_FRACTION,
)


def irrecoverable_deficit_fraction() -> float:
    """Fraction of the projected summer-runoff deficit no redistribution network can close.

    1 - MAX_SUMMER_DEFICIT_MITIGATION_FRACTION, per Farinotti et al.
    (2016)'s own best-case ceiling (their 65% figure is explicitly an
    upper bound assuming reservoirs are built at ideal sites, not an
    average or a guarantee).
    """
    return 1.0 - MAX_SUMMER_DEFICIT_MITIGATION_FRACTION


def full_replacement_is_possible() -> bool:
    """Whether an artificial network can fully replace a glacier's hydrological buffer.

    Always False. This is a mass-balance argument, not a modeling result:
    a glacier in an absolute-drought year (no winter snow, no spring
    rain) would still release stored ice as meltwater. A reservoir/MAR/
    peatland network has no equivalent independent water source -- it can
    only capture and time-shift water that already fell as precipitation
    upstream. In a year with insufficient upstream input, there is
    nothing to redistribute, regardless of installed capacity.
    """
    return False


def theoretical_mitigation_ceiling(
    with_citation: bool = False,
) -> float | tuple[float, str]:
    """Return the best documented ceiling for summer-runoff-deficit mitigation.

    Per Farinotti et al. (2016): up to `MAX_SUMMER_DEFICIT_MITIGATION_FRACTION`
    of the projected end-of-century summer-runoff change could be offset
    by an optimally sited dam/reservoir strategy -- this is a ceiling on
    what the *reservoir* component alone can do, before accounting for
    the sedimentation and evaporation losses documented elsewhere in this
    package, and before adding any MAR/peatland contribution.
    """
    if with_citation:
        return MAX_SUMMER_DEFICIT_MITIGATION_FRACTION, FARINOTTI_2016_CITATION
    return MAX_SUMMER_DEFICIT_MITIGATION_FRACTION
