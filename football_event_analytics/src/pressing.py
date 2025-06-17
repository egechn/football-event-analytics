def calculate_pressing_intensity(events_df):
    pressure_events = events_df[events_df['type.name'] == 'Pressure']
    pressures_per_90 = len(pressure_events) / (events_df['minute'].max() / 90)
    return pressures_per_90
