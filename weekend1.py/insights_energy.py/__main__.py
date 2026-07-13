import argparse
import csv
from collections import defaultdict
from datetime import datetime
from statistics import mean,stdev
from pathlib import Path

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


def parse_arguments():
    parser=argparse.ArgumentParser(
        description = "analyse hourly energy price data",
        exit_on_error=False
    )
    parser.add_argument("--File", required=True,help="CSV file path(required)")
    parser.add_argument("--metric",default="price",help="column name to analyze(default:'price')")
    parser.add_argument("--top",type=int,default=10,help="Number of spikes to show(default:10)")
    return parser.parse_args()

def validate_inputs(file_path, top_n):

    path=Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"the file '{file_path} does not exist.")
    if not path.is_file():
        raise ValidationError(f"The path '{file_path}' exists but is not a file.")
    
    if not isinstance(top_n,int):
        raise TypeError(f"The 'top' argument must be an integer. got:{type(top_n).__name__}")
    if top_n <= 0:
        raise ValueError(f"the 'top' argument must be a positive integer. Got: {top_n}")




def load_and_clean_data(file_path, metric):
    data = []

    with open(file_path,mode='r',encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        if not reader.fieldnames:
            raise ValidationError("the csv file is empty or missing headers")
        if metric not in reader.fieldnames:
            raise ValidationError(f"Metric column '{metric}' not found in csv headers.")
        
        for line_num, row in enumerate(reader,start=2):
            try:
                raw_ts=row["timestamp"].replace("Z","+00:00")
                ts = datetime.fromisoformat(raw_ts)
                val =float(row[metric])
                data.append({"timestamp": ts, "raw_ts": row["timestamp"],"value": val})
            except (ValueError, KeyError) as e:

                print(f"Warning: Skipping invalid row {line_num}: {e}")

    if not data:
        raise ValidationError("no valid data rows found in the CSV.")

    return data 

def display_daily_averages(data):
    daily_totals = defaultdict(list)
    for row in data:
        day_str = row["timestamp"].strftime("%y-%m-%d")
        daily_totals[day_str].append(row["value"])

        print("Daily averages:")
        print(f"{'Date:<12'} {'Avg Price'}")
        for day, values in sorted(daily_totals.items()):
            avg = mean(values)
            print(f"{day:<12} ${avg:.2f}")
        print()

def display_top_spikes(data,top_n):
    sorted_data= sorted(data,key=lambda x: x["value"],reverse = True)
    spikes = sorted-data[:top_n]

    print(f"top {top_n} price spikes: ")
    for spike in spikes:
        print(f"{spike['raw_ts']:<21} ${spike['value']:.2f}")
        print()

def display_anomalies(data):
    values =[row["value"]for row in data]

    if len(values) < 2:
        print("not enough data to calculate standard deviation for anomalies.\n")
        return
    
    data_mean=mean(values)
    data_std=stdev(values)

    if data_std == 0:
        print("anomalies detected: 0 as no variance in data ")
        return
    
    anomaly_count = sum(1 for val in values if (abs(val- data_mean) / data_std) > 2)
    print(f"anomalies detected: {anomaly_count} hour(s) (z-score > 2 threshold)\n")

def main():
    try:
        args=parse_arguments()

        validate_inputs(args.file, args.top)

        data = load_and_clean_data(args.file, args.metric)

        print()
        display_daily_averages(data)
        display_top_spikes(data, args.top)
        display_anomalies(data)

    except argparse.ArgumentError as e:
        print(f"command line error: {e}")
    except (FileNotFoundError, TypeError,ValueError,ValidationError) as e:
        print(f"validation error: {e}")
    except Exception as e:
        print(f"an unexpected error occurred: {e}")


if __name__ == "__main__" :
    main()


                        
                    