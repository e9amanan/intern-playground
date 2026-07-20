"""using loops for control flow"""

TARGET_RECORD = 105
current_records = [101, 102, 103, 104]

for records in current_records:
    if TARGET_RECORD == current_records:
        print("record found")
        break

else:
    print("record not found")
