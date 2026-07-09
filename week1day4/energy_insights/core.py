"""
Function specs (inside package)

    compute_daily_averages(rows: list[dict[str, str]], ts_col: str, value_col: str) -> dict[str, float]
        Input: rows, timestamp column, numeric value column
        Output: mapping YYYY-MM-DD -> average float
    find_spikes(rows: list[dict[str, str]], value_col: str, top: int) -> list[dict[str, str]]
        Input: rows, numeric value column, number of spikes
        Output: top entries by value

"""


def compute_daily_averages(rows, ts_col, value_col):
    totals = {}
    count = {}

    for row in rows:
        date = row[ts_col].split()[0]
        val = float(row[value_col])

        totals[date] = totals.get(date, 0.0) + val
        count[date] = count.get(date, 0) + 1

    return {date: value / count[date] for date, value in totals.items()}


def find_spikes(rows, value_col, top):
    sorted_rows = sorted(rows, key=lambda x: float(x[value_col]), reverse=True)
    return sorted_rows[:top]
