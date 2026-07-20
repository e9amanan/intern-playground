"""happy path"""


def process_upload_clean(file_data):
    """simple un-nested loops"""
    if not file_data:
        return "No data"

    if not file_data.endswith(".csv"):
        return "Not a CSV"

    return "Processed successfully"
