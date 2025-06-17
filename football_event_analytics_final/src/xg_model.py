import numpy as np

def calculate_xg(row):
    # Simple xG model: uses StatsBomb's xG value
    distance = row['shot.statsbomb_xg']
    return distance
