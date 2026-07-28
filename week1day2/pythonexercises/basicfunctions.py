"""
practice of basic python function"""

import statistics

import numpy as np


def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting},{name}"


def calculate_stats(*numbers: float) -> dict[str, float]:
    return {
        "min": min(numbers),
        "max": max(numbers),
        "mean": statistics.mean(numbers),
        "median": statistics.median(numbers),
    }


def calculate_stats_numpy(*numbers: float) -> dict[str, float]:
    arr = np.array(numbers)
    return {
        "min": float(np.min(arr)),
        "max": float(np.max(arr)),
        "mean": float(np.mean(arr)),
        "median": float(np.median(arr)),
    }


