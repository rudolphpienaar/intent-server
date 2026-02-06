"""Entrypoint for OHBM agentic failure simulations.

This module orchestrates generation of failure and misreport probability curves
for unbounded agentic orchestration versus IAS-bounded workflows. Outputs are
PNG figures and a JSON summary that can feed the OHBM abstract.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from ohbm2026.lib.models import CurveSeries, ScenarioProfile, ThresholdCrossing
from ohbm2026.lib.sweeps import scenarioFamily_build, thresholds_summary_build
from ohbm2026.util.plotting import curves_failure_plot, curves_misreport_plot


def arguments_parse() -> argparse.Namespace:
    """Parse CLI arguments for simulation execution.

    Returns:
        Parsed arguments namespace with output_dir and max_steps fields.
    """
    default_output: Path = Path(__file__).resolve().parents[3] / "build" / "ohbm"
    parser = argparse.ArgumentParser(description="Generate OHBM agentic failure curves.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=default_output,
        help="Directory for generated figures and summary JSON.",
    )
    parser.add_argument(
        "--max-steps",
        type=int,
        default=30,
        help="Maximum number of orchestration steps to model.",
    )
    return parser.parse_args()


def scenarioProfiles_default_get() -> list[ScenarioProfile]:
    """Return default scenario profiles for unbounded agent and IAS-bounded agent.

    Returns:
        List of scenario profiles used to build curves.
    """
    return [
        ScenarioProfile(
            label="Baseline agentic orchestration",
            per_step_error_near=0.02,
            per_step_error_far=0.02,
            correlation_factor=0.08,
            misreport_rate=0.30,
            branching_factor=2.5,
            near_failure_fraction=0.6,
        ),
        ScenarioProfile(
            label="IAS-constrained orchestration",
            per_step_error_near=0.01,
            per_step_error_far=0.0,
            correlation_factor=0.0,
            misreport_rate=0.10,
            branching_factor=1.05,
            near_failure_fraction=0.4,
        ),
    ]


def thresholds_default_get() -> list[float]:
    """Return failure thresholds to annotate on plots.

    Returns:
        Failure probability thresholds.
    """
    return [0.05, 0.20]


def stepsRange_build(max_steps: int) -> list[int]:
    """Build a 1-indexed list of orchestration depths.

    Args:
        max_steps: Maximum orchestration depth (levels).

    Returns:
        List of depth levels from 1..max_steps.
    """
    return list(range(1, max_steps + 1))


def summary_write(output_dir: Path, threshold_summaries: list[ThresholdCrossing]) -> None:
    """Write threshold crossing summaries to JSON.

    Args:
        output_dir: Directory for output artifacts.
        threshold_summaries: Threshold crossing records to serialize.
    """
    data = [
        {
            "label": crossing.label,
            "threshold": crossing.threshold,
            "steps_crossed": crossing.steps_crossed,
        }
        for crossing in threshold_summaries
    ]
    summary_path: Path = output_dir / "summary.json"
    summary_path.write_text(json.dumps(data, indent=2))


def main() -> None:
    """Entrypoint that coordinates curve generation and figure export."""
    args = arguments_parse()
    output_dir: Path = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    profiles: list[ScenarioProfile] = scenarioProfiles_default_get()
    depths: list[int] = stepsRange_build(args.max_steps)
    thresholds: list[float] = thresholds_default_get()

    all_series: list[CurveSeries] = []
    for profile in profiles:
        all_series.extend(scenarioFamily_build(profile=profile, depths=depths))

    curves_failure_plot(
        output_path=output_dir / "failure_vs_steps.png",
        series_list=all_series,
        thresholds=thresholds,
    )
    curves_misreport_plot(
        output_path=output_dir / "misreport_vs_steps.png",
        series_list=all_series,
    )

    threshold_summaries: list[ThresholdCrossing] = thresholds_summary_build(
        series_list=all_series, thresholds=thresholds
    )
    summary_write(output_dir=output_dir, threshold_summaries=threshold_summaries)


if __name__ == "__main__":
    main()
