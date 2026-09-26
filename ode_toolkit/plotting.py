import matplotlib.pyplot as plt
import numpy as np
from typing import List, Any

def plot_time_series(solution: Any, 
                     labels: List[str], 
                     title: str = "Compartmental Model Time Series",
                     xlabel: str = "Time",
                     ylabel: str = "Population",
                     figsize: tuple = (10, 6)) -> None:
    """
    Plots the time series of all state variables from a SciPy ODE solution.
    """
    if len(labels) != solution.y.shape[0]:
        raise ValueError("Number of labels must match the number of state variables.")

    plt.figure(figsize=figsize)
    
    for i, label in enumerate(labels):
        plt.plot(solution.t, solution.y[i], label=label, linewidth=2)
        
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.legend(loc='best', frameon=True, shadow=True)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def plot_phase_plane(solution: Any, 
                     x_idx: int, 
                     y_idx: int, 
                     x_label: str, 
                     y_label: str,
                     title: str = "Phase Plane Portrait",
                     figsize: tuple = (8, 6)) -> None:
    """
    Plots a 2D phase plane for two specific state variables to analyze stability.
    """
    plt.figure(figsize=figsize)
    
    plt.plot(solution.y[x_idx], solution.y[y_idx], linewidth=2.5, color='#2c3e50')
    plt.plot(solution.y[x_idx, 0], solution.y[y_idx, 0], 'go', markersize=8, label='Start')
    plt.plot(solution.y[x_idx, -1], solution.y[y_idx, -1], 'ro', markersize=8, label='End')
    
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)
    plt.legend(loc='best', frameon=True, shadow=True)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()