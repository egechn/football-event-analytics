import json
import pandas as pd

def load_event_data(path):
    with open(path, 'r') as f:
        data = json.load(f)
    return pd.json_normalize(data['events'])
