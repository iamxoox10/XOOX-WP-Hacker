import json

def load_config():
    try:
        with open("data/config.json", "r") as file:
            config_data = json.load(file)
            return config_data
    except FileNotFoundError:
        print("Configuration file not found. Using default settings.")
        return {}
