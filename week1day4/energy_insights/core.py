"""
Function specs (inside package)

    compute_daily_averages(rows: list[dict[str, str]], ts_col: str, value_col: str) -> dict[str, float]
        Input: rows, timestamp column, numeric value column
        Output: mapping YYYY-MM-DD -> average float
    find_spikes(rows: list[dict[str, str]], value_col: str, top: int) -> list[dict[str, str]]
        Input: rows, numeric value column, number of spikes
        Output: top entries by value

"""


"""def compute_daily_averages(rows, ts_col, value_col):
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

    """
def compute_daily_averages(rows: list[dict[str, str]], ts_col: str, value_col: str) -> dict[str, float]:
    totals: dict[str, float] = {}
    counts: dict[str, int] = {}

    for row in rows:
       
        if ts_col not in row or value_col not in row:
            raise KeyError(f"Missing column '{ts_col}' or '{value_col}' in data.")

        timestamp = row[ts_col]
        val_str = row[value_col]

        
        if not timestamp or not val_str:
            continue

        date = timestamp.split()[0]

       
        try:
            val = float(val_str)
        except ValueError:
            continue  

        totals[date] = totals.get(date, 0.0) + val
        counts[date] = counts.get(date, 0) + 1

    if not counts:
        raise ValueError("No valid numeric data found to compute averages.")

    
    return {date: total / counts[date] for date, total in totals.items()}


def find_spikes(rows: list[dict[str, str]], value_col: str, top: int) -> list[dict[str, str]]:
    if not rows:
        return []
        
    if value_col not in rows[0]:
        raise KeyError(f"Column '{value_col}' not found.")

    def get_sort_key(row: dict[str, str]) -> float:
        try:
            return float(row.get(value_col, 0))
        except (ValueError, TypeError):
            return float("-inf") 

    sorted_rows = sorted(rows, key=get_sort_key, reverse=True)
    return sorted_rows[:top]