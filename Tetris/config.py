import json

DEFAULT_CONFIG = {
    "profile_name": "",
    "high_score": 0,
    "achievements": {
        "Lose 1 game": True,
        "Lose 10 games": True,
        "Win 1 game": True,
        "Win 10 games": True,
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
