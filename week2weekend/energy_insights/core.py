"""Time-series data structures and analytics for energy data."""

from datetime import datetime
from statistics import mean, stdev
from .exceptions import ValidationError


class EnergySeries:
    """Represents a time-series dataset for a specific metric."""

    def __init__(self, raw_rows: list[dict], metric: str):
        self.metric = metric
        self.data = self._clean(raw_rows)

        if not self.data:
            raise ValidationError(f"No valid numeric data found for metric '{self.metric}'.")

    def _clean(self, raw_rows: list[dict]) -> list[dict]:
        """Parse timestamps and filter out invalid rows."""
        cleaned = []
        for row in raw_rows:
            try:
                raw_ts = row.get("timestamp", "")
                timestamp = datetime.fromisoformat(raw_ts.replace("Z", "+00:00"))
                val = float(row[self.metric])
                cleaned.append({"ts": timestamp, "raw_ts": raw_ts, "value": val})
            except (ValueError, KeyError, TypeError):
                continue
        return cleaned

    def __len__(self) -> int:
        return len(self.data)

    def __repr__(self) -> str:
        return f"<EnergySeries(metric='{self.metric}', valid_rows={len(self)})>"

    def summary(self) -> dict:
        """Calculate count, min, max, and mean of the valid data."""
        vals = [d["value"] for d in self.data]
        return {
            "count": len(vals),
            "min": min(vals),
            "max": max(vals),
            "mean": mean(vals)
        }

    def top_spikes(self, count: int) -> list[dict]:
        """Return the top highest values in the dataset."""
        return sorted(self.data, key=lambda x: x["value"], reverse=True)[:count]

    def anomalies(self, threshold: float = 2.0) -> list[dict]:
        """Identify outliers using a standard deviation (z-score) threshold."""
        vals = [d["value"] for d in self.data]
        if len(vals) < 2:
            return []

        avg, std = mean(vals), stdev(vals)
        if std == 0:
            return []

        return [d for d in self.data if (abs(d["value"] - avg) / std) > threshold]