#!/usr/bin/python3
import sys
import re
import signal

print("yhh")
ctrl_c_pressed = False
line_count = 0
file_size = 0
pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
default_status_codes = {200: 0, 301: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
status_codes = default_status_codes


def signal_handler(sigNumber, Frame):
    global ctrl_c_pressed
    ctrl_c_pressed = True


signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    line = line.strip()
    line_count += 1
    match = re.match(pattern, line)
    if match:
        statuscode = match.group(1)
        file_size += int(match.group(2))
        if statuscode.isdigit():
            statuscode = int(statuscode)
            if statuscode in status_codes:
                status_codes[statuscode] += 1
            else:
                status_codes[statuscode] = 1
        if line_count == 10 or ctrl_c_pressed:
            line_count = 0
            ctrl_c_pressed = False
            print('File size: {}'.format(int(match.group(2))))
            for key, value in sorted(status_codes.items()):
                if value > 0:
                    print('{} : {}'.format(key, value))
            status_codes = default_status_codes
