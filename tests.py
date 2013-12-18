from skip_list import SkipList
from bst import BST
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
        'structure': 'skip_list',
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
        'structure': 'skip_list',
        'size': size,
        'time': end - start,
        'comparisons': sl.comparisons,
        'height': sl.maxHeight
    }


# Define runs fot BST
def bst_insert_run(size):
    # Create a BST
    bst = BST()

    # Now, get time
    start = time.clock()

    # Insert elements
    for i in xrange(size):
        if i % 1000 == 0:
            print("Done %d" % i)
        bst.insert(i)

    # Get final time, and store
    end = time.clock()

    return {
        'structure': 'bst',
        'size': size,
        'time': end - start,
        'comparisons': bst.comparisons,
    }


def bst_search_run(size):
    # Create a BST
    bst = BST()

    # Insert elements
    for i in xrange(size):
        bst.insert(i)

    # Now, get time
    start = time.clock()

    # Find elements
    for i in xrange(size):
        bst.find(size)

    # Get final time, and store
    end = time.clock()

    return {
        'structure': 'bst',
        'size': size,
        'time': end - start,
        'comparisons': bst.comparisons
    }


structures_runs = {
    'skip_list': {
        'insertion': insertion_run,
        'search': search_run
    },
    'bst': {
        'insertion': bst_insert_run,
        'search': bst_search_run
    }
}

# Run many times
n = 10
sizes = [10**4, 2 * 10 ** 4, 5 * 10 ** 4]

for structure in ['skip_list', 'bst']:
    logging.info("Starting %s structure tests" % structure)

    runs = structures_runs[structure]
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

        logging.info("Suite: %s done, bawf!" % suite)
    logging.info("Structure: %s done :D!" % structure)
