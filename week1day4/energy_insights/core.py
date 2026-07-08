def compute_daily_averages(rows,ts_col,value_col):
    totals={}
    count={}

    for row in rows:
        date=row[ts_col].split()[0]
        val=float(row[value_col])

        totals[date] = totals.get(date,0.0) + val
        counts[data] = counts.get(data,0)+1

    return {date:totals[date]/counts[date]for date in total}

def find_spikes(rows, value_col,top):
    sorted_rows = sorted(rows,key=lambda x: float(x[value_col]),reverse = True)
    return sorted_rows[:top]
