"""using loops for control flow"""

TARGET_RECORD = 105
current_records = [101, 102, 103, 104]


for record in current_records:

    if TARGET_RECORD == record:
        print("record found")
        break
else:
    print("record not found")


process_queue = [1, 2, 0, 3, None, 4]

index = 0
# while loop practice
while index < len(process_queue):
    item = process_queue[index]
    index += 1

    # truthy/falsy evaluation
    if not item:
        print(f"Skipping falsy item at index {index - 1}")
        # continue statement
        continue

    print(f"Processing valid item: {item}")
