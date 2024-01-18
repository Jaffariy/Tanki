import json

DEFAULT_CONFIG = {
    "profile_name": "",
    "high_score": 0,
    "loses_count": 0,
    "fall_speed": 1,
    "achievements": {
        "Lose 1 game": False,
        "Lose 10 games": False,
        "Get 1000 score": False,
        "Get 5000 score": False,
    },
}


def load_config():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return DEFAULT_CONFIG.copy()


def save_config(config):
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)
