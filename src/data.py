import json
PARSED_FILE_PATH = "weather.json"
def some_logic(parsed_file_path=PARSED_FILE_PATH):
    with open(parsed_file_path, "r") as f:
        data = json.load(f)
    return data