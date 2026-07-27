"""practice of comprehension in python"""

raw_prices = ["12.50", " ", "invalid", "95.20", "45.00"]

valid_prices = [float(p) for p in raw_prices if p.strip().replace(".", "", 1).isdigit()]
print("Valid Prices:", valid_prices)

headers = ["  User_ID  ", "EMAIL@test.com", " Status"]
clean_header = {i: header.strip().lower() for i, header in enumerate(headers)}
print("Clean Headers:", clean_header)


raw_tags = ["Python", "java", "PYTHON", "C++", "Java"]
unique_tags = {tag.lower() for tag in raw_tags}
print("Unique Tags:", unique_tags)
