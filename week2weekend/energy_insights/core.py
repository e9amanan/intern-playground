from datetime import datetime
from statistics import mean, stdev
from .exceptions import ValidationError

class EnergySeries:
    
    def __init__(self, raw_rows: list[dict], metric: str):
        self.metric = metric
        self.data = self._clean(raw_rows)
        
        if not self.data:
            raise ValidationError(f"No valid numeric data found for metric '{metric}'.")

    def _clean(self, raw_rows: list[dict]) -> list[dict]:
        
        cleaned = []
        for row in raw_rows:
            try:
                raw_ts = row.get("timestamp", "")
                ts = datetime.fromisoformat(raw_ts.replace("Z", "+00:00"))
                val = float(row[self.metric])
                cleaned.append({"ts": ts, "raw_ts": raw_ts, "value": val})
            except (ValueError, KeyError, TypeError):
                continue  
        return cleaned

    def __len__(self) -> int:
        return len(self.data)

    def __repr__(self) -> str:
        return f"<EnergySeries(metric='{self.metric}', valid_rows={len(self)})>"

    def summary(self) -> dict:
        
        vals = [d["value"] for d in self.data]
        return {
            "count": len(vals),
            "min": min(vals),
            "max": max(vals),
            "mean": mean(vals)
        }

    def top_spikes(self, n: int) -> list[dict]:
        
        return sorted(self.data, key=lambda x: x["value"], reverse=True)[:n]

    def anomalies(self, threshold: float = 2.0) -> list[dict]:
       
        vals = [d["value"] for d in self.data]
        if len(vals) < 2:
            return []
            
        avg, std = mean(vals), stdev(vals)
        if std == 0:
            return []
            
        return [d for d in self.data if (abs(d["value"] - avg) / std) > threshold]