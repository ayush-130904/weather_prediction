import numpy as np
import pandas as pd
import requests

# Fetching Real Weather Data for Kalyan Coordinates
url = "https://api.open-meteo.com/v1/forecast?latitude=19.2437&longitude=73.13554&hourly=temperature_2m&current=temperature_2m"
response = requests.get(url).json()

all_temps = response['hourly']['temperature_2m']  # Taking hourly temperature from api response
all_times = response['hourly']['time']            # Taking timestamp for all_temps

current_time_str = response['current']['time']
current_time_dt = pd.to_datetime(current_time_str).replace(minute=0, second=0, microsecond=0)    #  normalizes the current time it to the nearest hour by setting minutes, seconds, and microseconds to zero.

# Find the index of the hourly forecast closest to or just before the current time
closest_hourly_index = 0
for i, hourly_time_str in enumerate(all_times):     #enumerate provides both the index (i) and the value (hourly_time_str) for each item in the list.
    hourly_time_dt = pd.to_datetime(hourly_time_str)
    if hourly_time_dt <= current_time_dt:
        closest_hourly_index = i
    else:
        break

# Get the last 3 hourly temperatures leading up to the current time
# Ensure we don't go out of bounds if there aren't 3 preceding hours
start_index = max(0, closest_hourly_index - 2)
recent_temps = np.array(all_temps[start_index : closest_hourly_index + 1]) # Take 3 readings ending at closest_hourly_index

# Calculating the trends/diff using Numpy
diff = np.diff(recent_temps)

# The averaging logic
avg_change = np.mean(diff)

# Predicted Temperature
current_temp = response['current']['temperature_2m']
predicted_temp = current_temp + avg_change

print(f"Recent Tempeartures(Last3h) : {recent_temps}")
print(f"Average Change : {avg_change:+.2f}'C per hour")
print(f"---")
print(f"Current Temperature : {current_temp}'C")
print(f"Predicted Temperature : {predicted_temp:+.2f}'C")