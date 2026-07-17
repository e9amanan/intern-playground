import argparse
from pathlib import Path
from energy_insights.io_utils import load_data
from energy_insights.core import EnergySeries
from energy_insights.exceptions import DataLoadError, ValidationError

def _get_series(args) -> EnergySeries:
    
    raw_data = load_data(Path(args.file))
    return EnergySeries(raw_data, args.metric)

def handle_summary(args) -> int:
    try:
        series = _get_series(args)
        stats = series.summary()
        print(f"Row count: {stats['count']}")
        print(f"Min: {stats['min']:.2f}")
        print(f"Max: {stats['max']:.2f}")
        print(f"Mean: {stats['mean']:.2f}")
        return 0
    except (DataLoadError, ValidationError) as e:
        raise SystemExit(f"Error: {e}")

def handle_spikes(args) -> int:
    try:
        series = _get_series(args)
        spikes = series.top_spikes(args.top)
        print(f"Top {args.top} price spikes:")
        for spike in spikes:
            print(f"  {spike['raw_ts']:<21} ${spike['value']:.2f}")
        return 0
    except (DataLoadError, ValidationError) as e:
        raise SystemExit(f"Error: {e}")

def handle_anomalies(args) -> int:
    try:
        series = _get_series(args)
        anomalies = series.anomalies()
        print(f"Anomalies detected: {len(anomalies)} hour(s) (z-score > 2 threshold)")
        return 0
    except (DataLoadError, ValidationError) as e:
        raise SystemExit(f"Error: {e}")

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="energy_insights", 
        description="CLI tool for hourly energy price analysis."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument("--file", required=True, help="Path to CSV/JSON data file.")
    parent_parser.add_argument("--metric", required=True, help="Column name to analyze.")

   
    summary_p = subparsers.add_parser("summary", parents=[parent_parser], help="View dataset stats.")
    summary_p.set_defaults(func=handle_summary)

  
    spikes_p = subparsers.add_parser("spikes", parents=[parent_parser], help="View highest values.")
    spikes_p.add_argument("--top", type=int, default=5, help="Number of spikes (default: 5).")
    spikes_p.set_defaults(func=handle_spikes)

    
    anomalies_p = subparsers.add_parser("anomalies", parents=[parent_parser], help="Detect outliers.")
    anomalies_p.set_defaults(func=handle_anomalies)

    args = parser.parse_args(argv)
    return args.func(args)