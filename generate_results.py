import collections
import json
import csv
import glob
import os

# Cd into dumps
os.chdir('dumps')

for file_name in glob.glob("*.json"):
    dump_file_name = file_name.replace('json', 'csv')

    bst = 'bst' in file_name
    insert = 'insert' in file_name

    f = open(file_name, 'r')
    data = json.load(f)

    # Read data, and generate row
    with open(dump_file_name, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        if bst and insert:
            # Write header
            writer.writerow(['SIZE', 'N', 'COMPARISONS', 'TIME', 'SWAPS'])
        else:
            writer.writerow(['SIZE', 'N', 'COMPARISONS', 'TIME'])

        for result in data:
            d = []
            d.append(result['size'])
            d.append(result['n'])
            d.append(result['comparisons'])
            d.append(result['time'])

            if bst and insert:
                d.append(result['swaps'])

            writer.writerow(d)
