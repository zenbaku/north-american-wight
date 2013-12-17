import collections
import json
import glob
import os

# Cd into dumps
os.chdir('dumps')

for suite in ['search', 'insertion']:
    # A dict to hold data
    DATA = collections.defaultdict(list)

    for file_name in glob.glob("*-%s.json" % suite):
        with open(file_name, 'r') as f:
            datas = json.load(f)
            for data in datas:
                # Now, form a key to store the result
                structure = data['structure']
                size = data['size']
                time = data['time']
                comparisons = data['comparisons']

                height = 0
                if structure == 'skip_list':
                    height = data['height']

                key = (structure, size)

                # Results
                r = {
                    'size': size,
                    'time': time,
                    'comparisons': comparisons,
                    'height': height
                }

                # Store result by key
                DATA[key].append(r)

    # To store the final results
    RESULT = {}

    # Process results
    for experiment in DATA:
        results = DATA[experiment]

        # Get the data
        comparisons = map(lambda d: d['comparisons'], results)
        times = map(lambda d: d['time'], results)
        heights = map(lambda d: d['height'], results)

        # Get means
        mean_comparisons = sum(comparisons) / float(len(comparisons))
        mean_times = sum(times) / float(len(times))
        mean_heights = sum(heights) / float(len(heights))

        # Final result
        r = {
            'average_time': mean_times,
            'average_comparisons': mean_comparisons,
            'average_height': mean_heights,
            'experiments': len(results)
        }

        # Store
        RESULT[experiment] = r

    print("Results for %s" % suite)
    for experiment in RESULT:
        print(experiment, RESULT[experiment])
