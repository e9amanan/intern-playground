"""practice of comprehension in python"""

raw_prices = ["12.50", " ", "invalid", "95.20", "45.00"]

valid_prices = [float(p) for p in raw_prices if p.strip().replace(".", "", 1).isdigit()]
print("valid prices")

headers = ["  User_ID  ", "EMAIL@test.com", " Status"]
clean_header = {i: headers.strip().lower() for i, header in enumerate(headers)}
