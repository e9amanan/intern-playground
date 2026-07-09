target_record = 105
current_records = [101, 102, 103, 104]

for records in current_records:
    if target_record == current_records:
        print("record found")
        break

else:
    print("record not found")
