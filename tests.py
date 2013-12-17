from random import randint, seed
from skip_list import SkipList
import time
import json
import logging

logging.basicConfig(
    format='[%(levelname)s][%(asctime)s]: %(message)s', level=logging.INFO)


# Define a runner for the Skip List
def insertion_run(size):
    # Create an Skip List
    sl = SkipList()

    # Now, get time
    start = time.clock()

    # Insert elements
    for i in xrange(size):
        sl.insert(i)

    # Get final time, and store
    end = time.clock()

    return {
        'size': size,
        'time': end - start,
        'comparisons': sl.comparisons,
        'height': sl.maxHeight
    }


def search_run(size):
    # Create an Skip List
    sl = SkipList()

    # Insert elements
    for i in xrange(size):
        sl.insert(i)

    # Now, get time
    start = time.clock()

    # Find elements
    for i in xrange(size):
        sl.find(size)

    # Get final time, and store
    end = time.clock()

    return {
        'size': size,
        'time': end - start,
        'comparisons': sl.comparisons,
        'height': sl.maxHeight
    }


runs = {
    'insertion': insertion_run,
    'search': search_run
}

# Run many times
n = 50
sizes = [10**4, 2 * 10 ** 4, 5 * 10 ** 4]

for suite in runs:
    run = runs[suite]

    results = []

    logging.info("Will run %s tests %d times" % (suite, n))
    for i in range(n):
        for size in sizes:
            r = run(size)
            results.append(r)
        logging.info("Run %d done" % (i+1))

    logging.info("Will dump results..")

    # Dump results
    file_name = 'dumps/dump-%d-%s.json' % (time.time(), suite)
    with open(file_name, 'w') as f:
        json.dump(results, f)

    print("Suite: %s done, bawf!" % suite)
