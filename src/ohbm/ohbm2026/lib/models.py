"""Data models for agentic failure simulation scenarios."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass
class ScenarioProfile:
    """Configuration for a single orchestration scenario."""

    label: str
    per_step_error_near: float
    per_step_error_far: float
    correlation_factor: float
    misreport_rate: float
    branching_factor: float
    near_failure_fraction: float


@dataclass
class CurveSeries:
    """Computed probabilities for a scenario across step counts."""

    label: str
    steps: list[int]
    failure_probabilities: list[float]
    misreport_probabilities: list[float]
    correlation_enabled: bool
    per_step_error_near: float
    per_step_error_far: float
    correlation_factor: float
    misreport_rate: float
    branching_factor: float
    near_failure_fraction: float


@dataclass
class ThresholdCrossing:
    """Threshold crossing summary for plotting annotations."""

    label: str
    threshold: float
    steps_crossed: int | None
