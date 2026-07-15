import argparse
import csv
from yourpkg import core
from yourpkg.exceptions import ValidationError,FileProcessingError

def handle_analyze(args)-> int:
    try:
        try:
            with open(args.file,"r", encoding="utf-8") as f:
                reader=csv.DictReader(f)
                raw_rows=list(reader)
        except FileNotFoundError:
            raise FileProcessingError(f"The file '{args.file}' was not found")
        except Exception as e:
            raise FileProcessingError(f"failed to read file:{e}")
        
        clean_data = core.clean_data(raw_rows,args.metric)
        core.display_daily_averages(clean_data)
        core.display_top_spikes(clean_data,args.top)
        core.display_anomalies(clean_data)

        return 0
    except FileProcessingError as e:
        raise SystemExit(f"File Error:{e}")
    except ValidationError as e:
        raise SystemExit(f"Data Validation Error:{e}")
    except Exception as e:
        raise SystemExit(f"unexpected processing error:{e}")
    
def main(argv=None)-> int:
    parser = argparse.ArgumentParser(
        prog="yourpkg"
        description="A CLI for time-series data analysis and anomaly detection."
    )

    subparsers = parser.add_subparsers(dest="command",required=True,help="available commands")

    analyze_parser=subparsers.add_parser("analyze",help="Analyze time-series data from a CSV.")

    analyze_parser.add_argument(
        "--file","-f",
        required=True,
        help="path to the csv file to analyze"
    )

    analyze_parser.add_argument(
        "--metric","-m",
        required=True,
        help="The name of the metric column to extract (e.g.,'price'.)"

    )
    analyze-parser.add_argument(
        "--top", "-t",
        type=int,
        default=3,
        help="Number of top spikes to display(default to 3)"
    )

    analyze_parser.set_default(func=handle_analyze)

    args=parser.parse_args(argv)
    return args.func(args)

     
