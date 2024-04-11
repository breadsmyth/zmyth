import json

def load():
    with open('settings.json') as settings_file:
        settings_json = settings_file.read()

    settings_obj = json.loads(settings_json)
    return settings_obj
