#!/usr/bin/python3
""" doc """

import sys


def print_stats(file_size, status_counts):
    """ doc """
    print(f"File size: {file_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

file_size = 0
status_counts = {200: 0, 301: 0, 400: 0,
                 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1

        parts = line.split()

        if len(parts) >= 7:
            try:
                file_size += int(parts[-1])
                status_code = int(parts[-2])

                if status_code in status_counts:
                    status_counts[status_code] += 1
            except ValueError:
                pass

        if line_count % 10 == 0:
            print_stats(file_size, status_counts)

except KeyboardInterrupt:
    print_stats(file_size, status_counts)
    raise

print_stats(file_size, status_counts)
