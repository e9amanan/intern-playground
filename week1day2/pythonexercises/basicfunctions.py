import statistics

def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting},{name}"
    

def calculate_stats(*numbers: float) -> dict[str, float]:
    return {
        "min": min(numbers),
        "max": max(numbers),
        "mean": statistics.mean(numbers),
        "median": statistics.median(numbers)
    }

def build_query(**params) -> str:
    """Build URL query string from keyword arguments."""
    # Example: build_query(page=1, limit=10) → "?page=1&limit=10"
    pairs = [f"{k}={v}" for k, v in params.items()]
    return "?" + "&".join(pairs)