"""Plotting utilities for OHBM agentic failure simulations."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt

from ohbm2026.lib.models import CurveSeries


def _apply_plot_style() -> None:
    """Apply a clean plot style suitable for paper figures."""
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update(
        {
            "axes.titlesize": 12,
            "axes.labelsize": 11,
            "legend.fontsize": 9,
            "figure.figsize": (7, 4),
            "lines.linewidth": 2.0,
        }
    )


def curves_failure_plot(
    output_path: Path, series_list: Iterable[CurveSeries], thresholds: Iterable[float]
) -> None:
    """Plot failure probability versus steps for multiple series.

    Args:
        output_path: Destination path for the figure.
        series_list: Curve series to plot.
        thresholds: Thresholds to draw as horizontal reference lines.
    """
    _apply_plot_style()
    fig, ax = plt.subplots()

    for series in series_list:
        linestyle: str = "-" if series.correlation_enabled else "--"
        ax.plot(
            series.steps,
            series.failure_probabilities,
            label=series.label,
            linestyle=linestyle,
        )

    for threshold in thresholds:
        ax.axhline(
            y=threshold,
            color="gray",
            linestyle=":",
            linewidth=1.2,
            label=f"{threshold*100:.0f}%",
        )

    ax.set_xlabel("Orchestration depth (levels, log scale)")
    ax.set_ylabel("Failure probability")
    ax.set_ylim(0, 1)
    ax.set_xscale("log")
    ax.legend()
    ax.set_title("Failure probability vs. orchestration depth")

    fig.tight_layout()
    fig.savefig(output_path, dpi=300)
    plt.close(fig)


def curves_misreport_plot(output_path: Path, series_list: Iterable[CurveSeries]) -> None:
    """Plot misreport probability versus steps for multiple series.

    Args:
        output_path: Destination path for the figure.
        series_list: Curve series to plot.
    """
    _apply_plot_style()
    fig, ax = plt.subplots()

    for series in series_list:
        linestyle: str = "-" if series.correlation_enabled else "--"
        ax.plot(
            series.steps,
            series.misreport_probabilities,
            label=series.label,
            linestyle=linestyle,
        )

    ax.set_xlabel("Orchestration depth (levels, log scale)")
    ax.set_ylabel("Misreport probability")
    ax.set_ylim(0, 1)
    ax.set_xscale("log")
    ax.legend()
    ax.set_title("Misreport probability vs. orchestration depth")

    fig.tight_layout()
    fig.savefig(output_path, dpi=300)
    plt.close(fig)
