#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Problem:
Create a hash table. The hash table should implement double hashing (i.e., if
the first insertion fails, use a second hash function). If the insertion of a
value fails on both hash functions, you will print to the screen that the
insertion failed. The recipe for a hash function is covered in the course notes
(http://www.cs.siue.edu/~marmcke/docs/cs340/hashing.html#good-hash-functions).

usage: hashTable.py [-h] [-v] arraySize [cycles]

positional arguments:
  arraySize      size of the hash table
  cycles         number of cycles to run

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  display verbose debugging

"""

__author__ = 'John Broere'
__copyright__ = 'Copyright 2018'
__license__ = 'GPL'
__version__ = '1.0.0'
__credits__ = ['John Broere', 'Mark McKenney']

__company__ = 'Southern Illinois University Edwardsville'
__course__ = 'CS534 - Advanced Database Management Systems'
__email__ = 'jbroere@siue.edu'
__status__ = 'Development'

import os
import argparse
import numpy as np

class hasher:
    """
    Main hasher class for woking with user defined hash table
    """

    def __init__(self, arraySize, randInsert, verbose):
        """
        Setup the class variables needed
        """
        self.hashSize = arraySize   # size of hash table
        self.hashTable = []         # main hash table

        # values used in finding hash index
        self.consts = {'a1': 0, 'b1': 0, 'a2': 0, 'b2': 0}
        self.p = 18446744073709551557    # largest unsinged 64-bit prime

        self.randInsert = randInsert
        self.verbose = verbose

    def reset(self):
        """
        Reset hash table and select new a and b valus to be used for new cycel
        of the program
        """
        self.hashTable.clear()

        for i in range(self.hashSize):
            self.hashTable.append(None)

        limit = 10000000

        self.consts['a1'] = np.random.randint(limit)
        self.consts['b1'] = np.random.randint(limit)
        self.consts['a2'] = np.random.randint(limit)
        self.consts['b2'] = np.random.randint(limit)

        if self.verbose:
            print('Hash1 - [a: {}, b: {}]'.format(self.consts['a1'],
                self.consts['b1']))
            print('Hash2 - [a: {}, b: {}]'.format(self.consts['a2'],
                self.consts['b2']))
            self.printHashTable()
            print('===========================================================')

    def getIndexHash1(self, value):
        """
        Index formula given to us by our professor:
        http://www.cs.siue.edu/~marmcke/docs/cs340/hashing.html#good-hash-functions
        """
        return (self.consts['a1'] * value + self.consts['b1']) \
            % self.p % self.hashSize

    def getIndexHash2(self, value):
        """
        Index formula given to us by our professor:
        http://www.cs.siue.edu/~marmcke/docs/cs340/hashing.html#good-hash-functions
        """
        return (self.consts['a2'] * value + self.consts['b2']) \
            % self.p % self.hashSize

    def insertItem(self, value):
        """
        Function for inserting an item into the hash table. First we attempt to use
        the first index, if that fails try a second index. If both indexes fail then
        we give up and do not attempt a third insert. This function returns a tuple
        showing the results of first and second insert attempts.
        """
        index1 = self.getIndexHash1(value)
        if self.verbose:
            print('index1: {}'.format(index1))

        if self.hashTable[index1] == None:
            self.hashTable[index1] = value
            return (None, None)
        else:
            if self.verbose:
                print('\tcan not insert {} at index {}'.format(value, index1))

            index2 = self.getIndexHash2(value)
            if self.verbose:
                print('index2: {}'.format(index2))

            if self.hashTable[index2] == None:
                self.hashTable[index2] = value
                return (index1, None)
            else:
                if self.verbose:
                    print('\tcan not insert {} at index {}'.format(value, index2))
                return (index1, index2)

    def printHashTable(self):
        """
        Print the hash table in its current form. If the hash table is large, it
        will not look pretty on the screen
        """
        print(self.hashTable)
        print('-----------------------------------------------------------')

    def fillHashTable(self):
        """
        Main function for filling in the hash table. This function will attempt to
        put n elements in a hash table of size n. The total number of successful
        inserts will be returned.
        """
        successes = 0

        for x in range(self.hashSize):

            # if we use random numbers we lower our overall average of success
            if self.randInsert:
                value = np.random.randint(1000000)
            else:
                value = x

            if self.verbose:
                print('inserting: {}'.format(value))

            id1, id2 = self.insertItem(value)

            if self.verbose:
                print('Collision: [{} | {}]'.format(id1, id2))

            if id1 != None and id2 != None:
                print('\tfailed to insert {} into the hastTable'.format(value))
                return successes
            else:
                successes += 1

            if self.verbose:
                self.printHashTable()

        return successes

def cls():
    """
    Function for clearing the screen on different OS running this program.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """
    Main for running this program. This main will check command line arguments and
    attempt to fill the desired hash table as many times as requested.
    """
    cls()

    # use of argparse to control command line input
    parser = argparse.ArgumentParser(prog='hashTable.py',
        description='Hash Table Implementation Lab')
    parser.add_argument('-s', '--size', type=int, default=10, metavar='n',
        help='size of the hash table [default: 10]')
    parser.add_argument('-c', '--cycles', type=int, default=1, metavar='n',
        help='number of cycles to run [default: 1]')
    parser.add_argument('-r', '--random', action='store_true',
        help='use random numbers for insert [default: sequential]')
    parser.add_argument('-v', '--verbose', action='store_true',
        help='display verbose output')
    args = parser.parse_args()

    arraySize = args.size
    cycles = args.cycles
    successes = []

    # get an instance of the hasher of the desired size
    h = hasher(arraySize, args.random, args.verbose)

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(' *  *  *  *  *   H   A   S   H   E   R  *  *  *  *  *')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    for i in range(cycles):
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('Cycle - {} of {}'.format(i+1, cycles))
        successes.append(0)

        h.reset()

        successes[i] = h.fillHashTable()
        print('successful inserts: {}/{}'.format(successes[i], arraySize))
        print('average successful: {:.1f}%'.format(successes[i]/arraySize*100))

        if args.verbose:
            h.printHashTable()

    print('###########################################################')
    sum = np.sum(successes)
    avg = np.average(successes)
    print('total successful insertions: {}/{}'.format(sum, arraySize*cycles))
    print('total average successful: {:.1f}%'.format(avg/arraySize*100))

if __name__ == '__main__':
    """
    Main entry point of this program.
    """
    main()
