# import pyodbc  # for accessing the database directly
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import matplotlib.ticker as ticker
from pathlib import Path


def set_plot_params():
    """
    Sets default plotting options.
    Args:
        None
    Returns:
        None
    """
    sns.set_style("whitegrid", {"grid.linestyle": "--"})

    params = {
        "legend.fontsize": "large",
        "figure.figsize": (16, 6),
        "axes.labelsize": "large",
        "axes.labelweight": "bold",
        "axes.labelpad": 10.0,
        "axes.titlesize": "xx-large",
        "axes.titleweight": "bold",
        "axes.titlepad": 15.0,
        "xtick.labelsize": "large",
        "ytick.labelsize": "large",
    }

    plt.rcParams.update(params)
    return


def pointplot_with_barplot(
    data,
    x,
    y,
    title,
    yaxis_freq=25,
    ymax=105,
):
    data = data.copy()
    data = data.reset_index(drop=False)
    sns.set_style("white")
    plt.figure(figsize=(14, 6))

    ax1 = sns.barplot(data=data, x=x, y="total_PMs", color="steelblue", alpha=0.5)
    ax1.grid(False)
    _ = ax1.set(ylim=(0, 2000))

    ax2 = ax1.twinx()

    ax2 = sns.pointplot(
        data=data,
        x=x,
        y=y,
        marker="o",
        color="steelblue",
    )
    ax2.set(title=f"{title}")
    _ = ax2.set(ylim=(0, ymax))

    for point in [t for t in range(0, ymax) if t % yaxis_freq == 0]:
        plt.axhline(point, linestyle="--", alpha=0.25, color="grey")

    ax2.yaxis.set_major_locator(ticker.MultipleLocator(yaxis_freq))

    ax2.yaxis.set_label_position("left")
    ax2.yaxis.tick_left()
    ax1.yaxis.set_label_position("right")
    ax1.yaxis.tick_right()

    sns.despine()
    plt.show()