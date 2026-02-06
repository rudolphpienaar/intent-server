"""Scenario sweeps for agentic orchestration simulations."""

from __future__ import annotations

from typing import Iterable

from ohbm2026.lib.calculations import failureCurve_build, misreportCurve_build
from ohbm2026.lib.models import CurveSeries, ScenarioProfile, ThresholdCrossing


def curveSeries_build(
    profile: ScenarioProfile, depths: Iterable[int], correlation_enabled: bool
) -> CurveSeries:
    """Build a single curve series for the provided profile.

    Args:
        profile: Scenario configuration to evaluate.
        depths: Sequence of depth levels.
        correlation_enabled: Whether correlated error multiplier is applied.

    Returns:
        Failure and misreport curves wrapped in a CurveSeries.
    """
    depths_list: list[int] = list(depths)
    failure_curve: list[float] = failureCurve_build(
        depths=depths_list,
        per_call_error=profile.per_step_error_near + profile.per_step_error_far,
        correlation_factor=profile.correlation_factor,
        correlation_enabled=correlation_enabled,
        branching_factor=profile.branching_factor,
    )
    misreport_curve: list[float] = misreportCurve_build(
        failure_curve=failure_curve,
        misreport_rate=profile.misreport_rate,
        near_failure_fraction=profile.near_failure_fraction,
    )
    if profile.correlation_factor == 0.0:
        label_suffix: str = ""
    else:
        label_suffix = " (correlated)" if correlation_enabled else " (independent)"
    return CurveSeries(
        label=f"{profile.label}{label_suffix}",
        steps=depths_list,
        failure_probabilities=failure_curve,
        misreport_probabilities=misreport_curve,
        correlation_enabled=correlation_enabled,
        per_step_error_near=profile.per_step_error_near,
        per_step_error_far=profile.per_step_error_far,
        correlation_factor=profile.correlation_factor,
        misreport_rate=profile.misreport_rate,
        branching_factor=profile.branching_factor,
        near_failure_fraction=profile.near_failure_fraction,
    )


def scenarioFamily_build(profile: ScenarioProfile, depths: Iterable[int]) -> list[CurveSeries]:
    """Build correlated and independent curve series for a profile.

    Args:
        profile: Scenario configuration to evaluate.
        depths: Sequence of depth levels.

    Returns:
        Two curve series: independent and correlated.
    """
    if profile.correlation_factor == 0.0:
        return [
            curveSeries_build(profile=profile, depths=depths, correlation_enabled=False),
        ]
    return [
        curveSeries_build(profile=profile, depths=depths, correlation_enabled=False),
        curveSeries_build(profile=profile, depths=depths, correlation_enabled=True),
    ]


def thresholdCrossing_find(values: list[float], depths: list[int], threshold: float) -> int | None:
    """Return the smallest depth where the curve crosses the threshold.

    Args:
        values: Curve values aligned with steps.
        depths: Depth levels corresponding to the values.
        threshold: Threshold to evaluate.

    Returns:
        First step that crosses the threshold, or None if never crosses.
    """
    for depth, value in zip(depths, values, strict=True):
        if value >= threshold:
            return depth
    return None


def thresholds_summary_build(
    series_list: Iterable[CurveSeries], thresholds: Iterable[float]
) -> list[ThresholdCrossing]:
    """Build threshold crossing summaries for a set of curve series.

    Args:
        series_list: Curve series to analyze.
        thresholds: Thresholds to compute crossings for.

    Returns:
        Collection of threshold crossing records.
    """
    summaries: list[ThresholdCrossing] = []
    for series in series_list:
        for threshold in thresholds:
            steps_crossed: int | None = thresholdCrossing_find(
                values=series.failure_probabilities, depths=series.steps, threshold=threshold
            )
            summaries.append(
                ThresholdCrossing(
                    label=series.label,
                    threshold=threshold,
                    steps_crossed=steps_crossed,
                )
            )
    return summaries
