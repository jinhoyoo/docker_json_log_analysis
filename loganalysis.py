import json
import sys
import dateutil.parser
import datetime
import time
import mmap
from tqdm import tqdm


def get_num_lines(file_path):
    fp = open(file_path, "r+")
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    return lines



filename = sys.argv[1]

# Read file and compare time one by one.
tollerable_duration_sec = 1
line_count = 0


with open(filename) as f:
    line_count += 1
    data = json.loads(f.readline())
    previous_time = dateutil.parser.parse(data['time'])

    for line in tqdm(f, total=get_num_lines(filename)):
        if line == '':
            break
        data = json.loads(line)
        current_time = dateutil.parser.parse(data['time'])
        diff = current_time - previous_time
        if diff.seconds > tollerable_duration_sec:
            print( f"Line{line_count}: {line}")

        previous_time = current_time
        line_count += 1
