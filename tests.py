from skip_list import SkipList
from bst import BST
import time
import json
import logging

from random import randrange

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
def bst_insert_run(data):
    pass


def bst_search_run(data):
    # Create a BST
    bst = BST()

    # Insert elements
    for i in xrange(size):
        bst.find(i)

    # Now, get time
    start = time.clock()

    # Find elements
    for i in data:
        bst.find(i)

    # Get final time, and store
    end = time.clock()

    return {
        'structure': 'bst',
        'size': size,
        'time': end - start,
        'comparisons': bst.comparisons
    }


def swap(data):
    assert len(data) > 2
    # Choose two random indexes
    ii = randrange(0, len(data))
    jj = randrange(0, len(data))

    # Swap
    data[ii], data[jj] = data[jj], data[ii]

    return data

# Run many times
n = 100
sizes = [10**4, 2 * 10 ** 4, 5 * 10 ** 4]

constructors = {
    'bst': BST,
    'skip_list': SkipList
}


for structure in ['bst', 'skip_list']:
    logging.info("Starting %s structure tests" % structure)

    constructor = constructors[structure]

    # Now, for each size...
    for size in sizes:
        # CREATE INPUT
        data = range(size)
        fail_data = range(size, size * 2)

        insert_results = []
        search_results = []

        # Now, for each n that we will run...
        for ni in xrange(n):
            # SWAPS
            if structure == 'bst':
                k = int(round(0.005 * float(size)))

                # Perform swaps
                for i in range(k):
                    swap(data)

            # And insert data
            # Create a BST
            bst = constructor()

            # Now, get time
            start = time.clock()

            # Insert elements
            for i in data:
                bst.insert(i)

            # Get final time, and store
            end = time.clock()

            insert_result = {
                'structure': structure,
                'size': len(data),
                'n': ni,
                'time': end - start,
                'comparisons': bst.comparisons,
            }
            if structure == 'bst':
                insert_result['swaps'] = k
            print(insert_result)

            # Reset comparisons counter
            bst.comparisons = 0

            # Now, perform queries
            # Size of que search
            search_size = int(round(0.5 * float(size)))
            fail_size = int(round(0.25 * float(search_size)))
            useful_size = search_size - fail_size

            # Form data to search
            search_data = []

            # And populate
            for i in xrange(useful_size):
                # Pick random from data
                ir = randrange(0, size)
                search_data.append(data[ir])

            for i in xrange(fail_size):
                ir = randrange(0, size)
                search_data.append(fail_data[ir])

            # Perform searchs
            # Now, get time
            start = time.clock()

            # Find elements
            for i in data:
                bst.find(i)

            # Get final time, and store
            end = time.clock()

            search_result = {
                'structure': structure,
                'size': size,
                'n': ni,
                'time': end - start,
                'comparisons': bst.comparisons
            }
            print(search_result)

            # Store results
            insert_results.append(insert_result)
            search_results.append(search_result)

        # Dump things
        file_name = 'dumps/dump-%s-%d-%s.json' % (structure, size, 'insert')
        with open(file_name, 'w') as f:
            json.dump(insert_results, f, indent=2)

        # Dump results
        file_name = 'dumps/dump-%s-%d-%s.json' % (structure, size, 'search')
        with open(file_name, 'w') as f:
            json.dump(search_results, f, indent=2)

        logging.info("Size: %sd done :D!" % size)
    logging.info("Structure: %s done :D!" % structure)
