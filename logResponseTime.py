import csv
import time
import ping3
from tqdm import tqdm

# Function to perform ICMP ping and measure response time
def check_response_time(host):
    try:
        response_time = ping3.ping(host)
        if response_time is not None:
            return "Success", response_time
        else:
            return "Timeout", None
    except Exception as e:
        return "Error", None

# Function to log information to a CSV file
def log_to_csv(data):
    with open('response_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Main function to monitor response time and log data
def main(host, interval, duration):
    print(f"Monitoring response time for {duration} seconds at {interval} second intervals...")
    start_timestamp = time.time()
    end_timestamp = start_timestamp + duration
    request_number = 0

    # Initialize tqdm progress bar
    with tqdm(total=duration // interval) as pbar:
        while time.time() < end_timestamp:
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            status, response_time = check_response_time(host)
            request_number += 1

            if status == "Success":
                log_data = [timestamp, request_number, host, "Success", response_time]
                log_to_csv(log_data)
                print(f"{timestamp} - Request {request_number}: Response from {host} in {response_time:.2f} seconds")
            elif status == "Timeout":
                log_data = [timestamp, request_number, host, "Timeout", None]
                log_to_csv(log_data)
                print(f"{timestamp} - Request {request_number}: Timeout while waiting for response from {host}")
            else:
                log_data = [timestamp, request_number, host, "Error", None]
                log_to_csv(log_data)
                print(f"{timestamp} - Request {request_number}: Error occurred while pinging {host}")

            pbar.update(1)
            time.sleep(interval)

# Example usage
if __name__ == "__main__":
    host = "condor1230"  # Replace with the host you want to monitor
    interval = 1  # Interval between each check (in seconds)
    duration = 3600  # Duration of monitoring (in seconds)
    main(host, interval, duration)
