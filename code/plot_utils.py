import constants as c
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial"]


def plot_scatters_per_metric(dfs, metric):
    n_cols = len(dfs)
    n_rows = 1

    fig, axes = plt.subplots(
        n_rows, n_cols, figsize=(6 * n_cols, 6 * n_rows), sharex=False, sharey=False
    )

    if isinstance(axes, np.ndarray):
        axes = axes.flatten()
    else:
        axes = [axes]

    df_counter = 0
    for ax, df in zip(axes, dfs):
        idle_column = "Base (" + metric.split(" (")[-1]
        attack_column = "Attack (" + metric.split(" (")[-1]

        min_val = df[[idle_column, attack_column]].min().min()
        max_val = df[[idle_column, attack_column]].max().max()
        pad = (max_val - min_val) * 0.05
        min_val -= pad
        max_val += pad

        attack_id = list(c.ATTACK_TYPES.keys())[df_counter]
        scatter_configuration = c.PLOT_SCATTERS_CONFIGURATIONS.get(attack_id)

        sns.scatterplot(
            x=idle_column,
            y=attack_column,
            data=df,
            alpha=0.7,
            ax=ax,
            s=80,
            color=scatter_configuration.get("color", "gray"),
            marker=scatter_configuration.get("marker", "o"),
        )

        idle_label = "Baseline " + metric
        attack_label = "Attack " + metric

        ax.plot([min_val, max_val], [min_val, max_val], "k--", label="x = y")
        ax.set_aspect("equal", adjustable="box")
        ax.set_xlim(min_val, max_val)
        ax.set_ylim(min_val, max_val)
        ax.set_title(c.ATTACK_TYPES.get(attack_id, attack_id))
        ax.set_xlabel(idle_label)
        ax.set_ylabel(attack_label)
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles=handles, loc="lower right")

        df_counter += 1

    for i, ax in enumerate(axes[:n_cols]):
        ax.text(
            -0.1,
            1.05,
            f"{chr(97 + i)})",
            transform=ax.transAxes,
            fontsize=12,
            fontweight="bold",
            va="top",
            ha="right",
        )

    for ax in axes[n_cols:]:
        ax.axis("off")

    plt.tight_layout(rect=[0, 0.07, 1, 0.93])

    plt.savefig(
        f"{c.FIGURES_OUTPUT_DIRECTORY_PATH}/500F-baseline-vs-attack-{metric.lower().split(' (')[0].replace(' ', '-')}-scatter.png",
        dpi=600,
        bbox_inches="tight",
    )
    plt.close()
