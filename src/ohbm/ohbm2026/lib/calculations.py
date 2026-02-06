"""Probability calculations for agentic orchestration failures."""

from __future__ import annotations

from typing import Iterable


def value_clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    """Clamp a floating-point value to the inclusive range.

    Args:
        value: Value to clamp.
        lower: Lower bound for the range.
        upper: Upper bound for the range.

    Returns:
        Clamped value between lower and upper.
    """
    return max(lower, min(upper, value))


def effectiveCalls_calculate(depth: int, branching_factor: float) -> int:
    """Calculate effective call count given depth and branching factor.

    Args:
        depth: Depth (levels) in the orchestration graph.
        branching_factor: Average fan-out per level.

    Returns:
        Total number of calls up to this depth (geometric series), at least depth.
    """
    if branching_factor <= 1.0:
        return depth
    return int(((branching_factor**depth) - 1) / (branching_factor - 1))


def failureProbability_calculate(
    effective_calls: int,
    per_call_error: float,
    correlation_factor: float,
    correlation_enabled: bool,
) -> float:
    """Calculate failure probability for a given call count.

    Uses an independent Bernoulli chain when correlation is disabled. Adds a
    linear cascade multiplier when correlation is enabled to reflect parameter
    drift or compounding tool mismatches.

    Args:
        effective_calls: Number of calls including branching.
        per_call_error: Probability of error per call.
        correlation_factor: Linear cascade multiplier.
        correlation_enabled: Whether to apply the cascade multiplier.

    Returns:
        Failure probability clipped to [0, 1].
    """
    independent_success: float = (1.0 - per_call_error) ** effective_calls
    if correlation_enabled:
        cascade_multiplier: float = 1.0 + correlation_factor * max(effective_calls - 1, 0)
        failure_probability: float = 1.0 - independent_success * cascade_multiplier
    else:
        failure_probability = 1.0 - independent_success
    return value_clamp(failure_probability)


def misreportProbability_calculate(failure_probability: float, misreport_rate: float) -> float:
    """Calculate probability of a misreported success.

    Args:
        failure_probability: Probability that the pipeline failed.
        misreport_rate: Probability that a failure is reported as success.

    Returns:
        Probability of a silent failure.
    """
    return value_clamp(failure_probability * misreport_rate)


def failureCurve_build(
    depths: Iterable[int],
    per_call_error: float,
    correlation_factor: float,
    correlation_enabled: bool,
    branching_factor: float,
) -> list[float]:
    """Build failure probability curve across steps.

    Args:
        depths: Sequence of depth levels to evaluate.
        per_call_error: Error probability per orchestration call.
        correlation_factor: Linear cascade multiplier.
        correlation_enabled: Whether to apply the cascade multiplier.
        branching_factor: Average fan-out per level.

    Returns:
        Failure probability at each depth level.
    """
    return [
        failureProbability_calculate(
            effective_calls=effectiveCalls_calculate(depth=depth, branching_factor=branching_factor),
            per_call_error=per_call_error,
            correlation_factor=correlation_factor,
            correlation_enabled=correlation_enabled,
        )
        for depth in depths
    ]


def misreportCurve_build(
    failure_curve: Iterable[float], misreport_rate: float, near_failure_fraction: float
) -> list[float]:
    """Build misreport probability curve from a failure curve.

    Args:
        failure_curve: Sequence of failure probabilities (near + far).
        misreport_rate: Probability a near failure is misreported as success.
        near_failure_fraction: Fraction of failures that are near-path (plausible) deviations.

    Returns:
        Misreport probability for each depth level.
    """
    return [
        misreportProbability_calculate(value * near_failure_fraction, misreport_rate)
        for value in failure_curve
    ]
