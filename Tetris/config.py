import json

DEFAULT_CONFIG = {
    "high_score": 0,
    "achievements": {
        "Lose 1 game": False,
        "Lose 10 games": False,
        "Win 1 game": False,
        "Win 10 games": False,
    }
}

def load_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return DEFAULT_CONFIG.copy()

def save_config(config):
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)
