#!/usr/bin/python3
"""Module for function that displays HTTP request stats from the stdin"""
import sys


def print_statistics(status_dict, total_size):
    """Prints the accumulated file size and status code counts"""
    print(f"File size: {total_size}")
    for code in sorted(status_dict.keys()):
        if status_dict[code] != 0:
            print(f"{code}: {status_dict[code]}")


http_statusCodes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
log_count = 0
total_size = 0

try:
    for line in sys.stdin:
        if log_count != 0 and log_count % 10 == 0:
            print_statistics(http_statusCodes, total_size)
        line_tokens = line.split()
        log_count += 1
        try:
            total_size += int(line_tokens[-1])
        except Exception:
            pass
        try:
            if line_tokens[-2] in http_statusCodes:
                http_statusCodes[line_tokens[-2]] += 1
        except Exception:
            pass
    print_statistics(http_statusCodes, total_size)
except KeyboardInterrupt:
    print_statistics(http_statusCodes, total_size)
    raise
