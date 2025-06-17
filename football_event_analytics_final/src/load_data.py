import json
import pandas as pd

def load_event_data(uploaded_file):
    stringio = uploaded_file.read().decode("utf-8")
    data = json.loads(stringio)
    return pd.json_normalize(data)
