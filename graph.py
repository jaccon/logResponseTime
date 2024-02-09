import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

# Function to convert string timestamp to datetime object
def convert_to_datetime(timestamp_str):
    return datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')

# Initialize lists to store timestamps and response times
timestamps = []
response_times = []

# Open the CSV file
with open('response_log.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    # Iterate through each row in the CSV file
    for row in reader:
        # Extract timestamp and response time from the row
        timestamp = convert_to_datetime(row[0])
        response_time = float(row[4])
        # Append the extracted values to the lists
        timestamps.append(timestamp)
        response_times.append(response_time)

# Calculate the average response time
average_response_time = np.mean(response_times)

# Plot the graph
plt.plot(timestamps, response_times, marker='o', linestyle='-', label='Response Time')
plt.axhline(y=average_response_time, color='r', linestyle='--', label='Average Response Time')
plt.title('Response Time Over Time')
plt.xlabel('Timeline')
plt.ylabel('Response Time (s)')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
# Save the plot as a PNG file
plt.savefig('response_time_graph.png')

# Generate the HTML file
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Response Time Graph</title>
</head>
<body>
    <h1>Response Time Over Time</h1>
    <img src="response_time_graph.png" alt="Response Time Graph">
</body>
</html>
"""

# Write the HTML content to a file
with open('date-time.html', 'w') as html_file:
    html_file.write(html_content)

print("HTML file 'date-time.html' created successfully.")
