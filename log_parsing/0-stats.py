#!/usr/bin/python3
""" doc """
import sys


def print_stats(file_size, status_counts):
    """ doc """
    print(f"File size: {file_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


# Initialize variables to store total file size
# and counts for each status code.
file_size = 0
status_counts = {200: 0, 301: 0, 400: 0,
                 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    # Read input lines from stdin one by one
    for line in sys.stdin:
        line_count += 1  # Increment the line count

        # Split the line into parts based on spaces
        parts = line.split()

        # Ensure the line has the correct
        # number of parts (>=7 for valid entries)
        if len(parts) >= 7:
            try:
                # Extract the file size and status code from the log entry
                # File size is the last part of the line
                file_size += int(parts[-1])
                # Status code is the second-to-last part
                status_code = int(parts[-2])

                # Update the count for the status code
                # if it's one of the valid codes
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except ValueError:
                # If there's an error (e.g., non-integer
                # status code or file size),
                # skip that line without raising an exception
                pass

        # Every 10 lines, print the current statistics
        if line_count % 10 == 0:
            print_stats(file_size, status_counts)

except KeyboardInterrupt:
    # On a keyboard interrupt (Ctrl + C), print the current statistics
    print_stats(file_size, status_counts)
    raise  # Re-raise the exception to allow graceful exit

# After reaching the end of input (EOF), print the final statistics
print_stats(file_size, status_counts)
