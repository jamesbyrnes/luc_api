import json

def get_settings():
    with open('./settings.json') as f:
        settings = json.load(f)

    return settings
