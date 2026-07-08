def compute_daily_averages(rows,ts_col,value_col):
    totals={}
    count={}

    for row in rows:
        date=row[ts_col].split()[0]
        val=float(row[value_col])

        totals[date] = totals.get(date,0.0) + val
        count[date] = count.get(date,0)+1

    return {date:totals[date]/count[date]for date in totals}

def find_spikes(rows, value_col,top):
    sorted_rows = sorted(rows,key=lambda x: float(x[value_col]),reverse = True)
    return sorted_rows[:top]
