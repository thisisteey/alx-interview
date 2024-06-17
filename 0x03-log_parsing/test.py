#!/usr/bin/python3
"""Module for function that displays HTTP request stats from the stdin"""
import sys
from re import split

http_statusCodes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
log_count = 0
total_size = 0


def print_statistics():
    """Prints the accumulated file size and status code counts"""
    print(f"File size: {total_size}")
    for code, count in sorted(http_statusCodes.items()):
        if count != 0:
            print(f"{code}: {count}")


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            line_info = line.replace("\n", "")
            log_elements = split('- | "|" | " " ', str(line_info))
            try:
                request_info = log_elements[-1].split(" ")
                if int(request_info[0]) not in http_statusCodes.keys():
                    continue
                http_statusCodes[int(request_info[0])] += 1
                log_count += 1
                total_size += int(request_info[1])
                if log_count % 10 == 0:
                    print_statistics()
            except Exception:
                pass
        print_statistics()
    except KeyboardInterrupt:
        print_statistics()
