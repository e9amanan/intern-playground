import csv
from pathlib import Path
from .exceptions import FileProcessingError, ValidationError

def read_csv(file_path:str, required_column:str)-> list[dict]:
    path=Path(file_path)

    if not path.exists():
        raise FileProcessingError(f"The file '{file_path}' does not exist")
    if not path.is_file():
        raise FileProcessingError(f"The path '{file_path}' exists but is not a file.")
    
    try:
        with open(file_path,mode='r',encoding='utf-8') as csvfile: 
            reader = csv.DictReader(csvfile)

            if not reader.fieldnames:
                raise ValidationError("the csv file is empty or missing headers")
            if required_column and required_column not in reader.fieldnames:
                raise ValidationError(f"Metric columns '{required_column}' not found in headers")

            return list(reader)
        
    except IOError as e:
        raise FileProcessingError(f"couldnt read csv file: {e}")

def write_csv(file_path:str,data:list[dict],fieldnames:list[str])-> None:
    if not data:
        return
    try:
        with open(file_path,mode="w",encoding="utf-8",newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except IOError as e:
        raise FileProcessingError(f"Failed to write CSV to {file_path}: {e}")

def read_json(file_path:str,expected_type:type=list):
    path = Path(file_path)
    if not path.exists():
        raise FileProcessingError(f"File not found: {file_path}")

    try:
        with open(file_path,mode = "r",encoding='utf-8') as file:
            data = json.load(file)
            if not isinstance(data, expected_type):
                raise ValidationError(f"Expected data type {expected_type.__name__}, but got {type(data).__name__}")
            return data 
    except json.JSONDecodeError as e:
        raise FileProcessingError(f"invalid JSON format in {file_path}: {e}")
    except IOError as e:
        raise FileProcessingError(f"could not read JSON file: {e}")
    
def write_json(file_path:str,data)-> None:
    try:
        with open(file_path,mode="w",encoding="utf-8") as File:
            json.dump(data,file,indent=4)
    except IOError as e:
        raise FileProcessingError(f"Failed to write JSON to {file_path}: {e}")
