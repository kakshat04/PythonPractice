"""
You're given a CSV file with sensor readings from a wind turbine:

timestamp,power_output,wind_speed
2025-07-15 09:00,540.0,12.5
2025-07-15 09:05,9999.9,12.6
2025-07-15 09:10,538.5,12.7
Write a script to:

Detect and print rows where power_output is clearly faulty (e.g., above 9000 or negative).

Return the average of valid power_output values.
"""
import csv


def sensor_data_validator(csv_file):
    total_power_output = 0
    with open(csv_file) as csv_file:
        csv_reader = list(csv.reader(csv_file, delimiter=','))
        for row in range(1, len(csv_reader)):
            if int(float(csv_reader[row][1])) > 9000 or int(float(csv_reader[row][1])) < 0:
                total_power_output += float(csv_reader[row][1])
    return (total_power_output / row), total_power_output



print(sensor_data_validator('turbine_sensor_data.csv'))