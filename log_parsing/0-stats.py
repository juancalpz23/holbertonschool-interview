#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_file_size = 0
status_codes = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0


# Function to print metrics
def print_metrics():
    """Prints the total file size and count of status codes."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


# Signal handler for keyboard interrupt (CTRL + C)
def signal_handler(sig, frame):
    """Handles keyboard interrupt signal (CTRL + C) and prints metrics."""
    print_metrics()
    sys.exit(0)


# Register signal handler for SIGINT (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)


# Main loop to read input lines
for line in sys.stdin:
    try:
        # Parse the line
        parts = line.split()
        if len(parts) < 9:
            continue

        ip_address = parts[0]
        date = parts[3] + " " + parts[4]
        request = parts[5] + " " + parts[6] + " " + parts[7]
        status_code = parts[8]
        file_size = parts[9]

        # Validate the request format
        if request != '"GET /projects/260 HTTP/1.1"':
            continue

        # Update total file size
        total_file_size += int(file_size)

        # Update status code count if it's a valid integer
        if status_code.isdigit():
            status_code = int(status_code)
            if status_code in status_codes:
                status_codes[status_code] += 1

        line_count += 1

        # Print metrics after every 10 lines
        if line_count % 10 == 0:
            print_metrics()

    except Exception:
        continue

# Final print (if the program ends without interruption)
print_metrics()
