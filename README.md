# Network Monitoring Script

This Python script monitors the response time of a specified host using ICMP ping. It logs the results to a CSV file and displays a progress bar during monitoring.

## Features

1. **ICMP Ping Monitoring**: The script pings the specified host to measure response time (round-trip time).

2. **Response Time Logging**: It logs the following information to a CSV file (`response_log.csv`):
   - Timestamp
   - Request number
   - Host
   - Status (Success, Timeout, or Error)
   - Response time (if successful)

3. **Progress Bar**: The script uses the `tqdm` library to display a progress bar, updating with each ping request.

4. **Customization Options**:
   - Set the `host_to_monitor` variable to the desired host.
   - Adjust the monitoring interval (in seconds) using `interval_seconds`.
   - Specify the total monitoring duration (in seconds) with `monitoring_duration_seconds`.

## Example Usage

```python
# Example usage
if __name__ == "__main__":
    host_to_monitor = "example.com"
    interval_seconds = 5
    monitoring_duration_seconds = 60
    main(host_to_monitor, interval_seconds, monitoring_duration_seconds)
