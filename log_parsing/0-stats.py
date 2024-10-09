#!/usr/bin/python3
"""
Parses a log of HTTP GET request results from stdin to tabulate the total
counts of status codes appearing in each response, and the file size
"""


from sys import argv

def print_log_totals(total_file_size, code_counts):
    """
    Prints current totals of file size and status code counts.
    """
    print("File size: {}".format(total_file_size))
    for code in code_counts:
        if code_counts[code] > 0:
            print("{}: {}".format(code, code_counts[code]))


if __name__ == '__main__':
    from sys import stdin, stderr
    from collections import OrderedDict
    from datetime import datetime

    line_no = 0
    total_file_size = 0
    code_counts = OrderedDict.fromkeys([200, 301, 400, 401, 403, 404, 405, 500], 0)

    try:
        for line in stdin:
            line_no += 1

            # Split line to handle IP address and the rest of the data
            a = line.split('-', 1)
            if len(a) != 2:
                # Likely not a formatted line
                continue

            # Extracting timestamp and request
            b = a[1].split(']')
            timecode = b[0].lstrip(' [')
            try:
                datetime.strptime(timecode, '%Y-%m-%d %H:%M:%S.%f')
            except ValueError:
                stderr.write("{}: {}: invalid timecode\n".format(argv[0], line_no))
                continue  # Skip line if timecode is invalid

            # Extracting URL request
            c = b[1].split('"')
            c = c[1:]  # We expect the second element to be the GET request
            if c[0] != 'GET /projects/260 HTTP/1.1':
                stderr.write("{}: {}: unexpected HTTP request\n".format(argv[0], line_no))
                continue  # Skip line if the request is not as expected

            # Extract status code and file size
            d = c[1].strip().split(' ')

            # Process status code
            if d[0].isdigit():
                code = int(d[0])
                if code in code_counts:
                    code_counts[code] += 1
                else:
                    stderr.write("{}: {}: invalid status code {}\n".format(argv[0], line_no, code))

            # Process file size
            if d[1].isdigit():
                total_file_size += int(d[1])
            else:
                stderr.write("{}: {}: invalid file size {}\n".format(argv[0], line_no, d[1]))

            # Print totals every 10 lines
            if line_no % 10 == 0:
                print_log_totals(total_file_size, code_counts)

        # Final totals after loop completes
        print_log_totals(total_file_size, code_counts)

    except KeyboardInterrupt:
        print_log_totals(total_file_size, code_counts)
        raise
