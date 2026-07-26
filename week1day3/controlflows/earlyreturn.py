"""happy path"""


def process_upload_clean(file_data):
    """simple un-nested loops with elif"""
    if not file_data:
        return "No data"
    elif not file_data.endswith(".csv"):
        return "Not a CSV"

    return "Processed successfully"