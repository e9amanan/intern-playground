def process_upload_clean(file_data):
   
    if not file_data:
        return "No data"
        
    
    if not file_data.endswith('.csv'):
        return "Not a CSV"
        
    # The Happy Path: Un-nested and easy to read
    return "Processed successfully"