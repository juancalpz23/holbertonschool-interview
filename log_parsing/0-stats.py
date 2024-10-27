#!/usr/bin/python3
"""Module for log parsing script"""
import sys

if __name__ == "__main__":
    size = [0]
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    def check_match(line):
        """Checks for matching log line and updates metrics"""
        try:
            line = line.strip()
            words = line.split(" ")
            size[0] += int(words[-1])
            code = int(words[-2])
            if code in codes:
                codes[code] += 1
        except (ValueError, IndexError):
            pass

    def print_stats():
        """Prints accumulated statistics."""
        print("File size: {}".format(size[0]))
        for k in sorted(codes.keys()):
            if codes[k]:
                print("{}: {}".format(k, codes[k]))

    i = 1
    try:
        for line in sys.stdin:
            check_match(line)
            if i % 10 == 0:
                print_stats()
            i += 1
    except KeyboardInterrupt:
        print_stats()
        sys.exit(0)

    print_stats()
