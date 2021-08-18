#!/usr/bin/env python3
# Program: RelativeEntropy
# Author: Darren Trieu Nguyen
# Version: 0.2
# Function: Takes in an arbitrary character frequency distribution to
#           calculate the relative entropy of a given file

import sys
import json
import numpy as np
import argparse
import logging

""" Class that houses RelativeEntropy 
"""

class RelativeEntropy:

    """ Initialization function
        Handles options from the CLI
    """
    def __init__(self):
        if __name__ == '__main__':
            version = 0.2

            # Parsing the CLI for options and parameters
            parser = argparse.ArgumentParser(
                description='Analyzes relative entropy of a given file'
            )
            # TODO: Add ability for script to handle multiple input files
            parser.add_argument('inputFile', metavar='inputFile', nargs='+',
                                help='Input files for which to calculate' \
                                ' entropy')
            # TODO: Add to documentation how baseline files should be formatted
            parser.add_argument('--baseline', help='The file containing the' \
                                ' distribution to be used as the baseline for' \
                                ' the relative entropy calculation')
            parser.add_argument('-v', '--verbose',
                                help='Increases output verbosity', \
                                action='store_true')
            parser.add_argument('--log', nargs='?', default='WARNING',
                                help='Controls logging verbosity based off of'\
                                ' log message priority. Levels include:'\
                                'DEBUG, INFO, WARNING, ERROR, CRITICAL')
            # TODO: Give user the ability to specify and output file/directory

            args = parser.parse_args()

            # Initializing log file and log level
            logLevel = args.log
            logFile = None

            # Initializing logging
            logger = logging.getLogger(self.__class__.__name__)

            numeric_level = getattr(logging, logLevel.upper(), None)
            if not isinstance(numeric_level, int):
                raise ValueError('Invalid log level: %s' % logLevel)
            if logFile is not None:
                logging.basicConfig(filename=logFile, filemode='w', \
                                    level=numeric_level)
            else:
                logging.basicConfig(level=numeric_level)

            #TODO: Script should call main function here
        # When called from another script
        else:
            # Initializing logging
            frame = inspect.currentframe().f_back
            try:
                try:
                    self_obj = frame.f_locals['self']
                    logName = type(self_obj).__name__
                except KeyError:
                    logName = self.__class__.__name__
            finally:
                del frame

            logger = logging.getLogger(logName + '.' \
                                        + str(self.__class__.__name__))
            self.logger = logger

# Usage Handling
if (len(sys.argv) != 3):
    print('Usage: ' + str(sys.argv[0]) + ' [Input File] [Frequency Distribution]')
    sys.exit(1)

inputFile = str(sys.argv[1])
distFile = str(sys.argv[2])

# Reading the Input File
inputBuffer = None
with open(str(inputFile), 'r') as inputF:
    inputBuffer = inputF.read()

if (inputBuffer is not None):
    print('Input file successfully read.')
else:
    print('Failed to read input file. Exiting.')
    sys.exit(2)

# Reading the Dist File into a dictionary
freqDict = None
with open(str(distFile), 'r') as distF:
    freqDict = json.load(distF)

if (freqDict is not None):
    print('Distribution file successfully read.')
else:
    print('Failed to read distribution file. Exiting.')
    sys.exit(3)

# Count the number of occurrences of a given character in the input file for
# every character listed in freqDict
# And calculates the relative entropy term corresponding to the character
# Then adds the term to the total sum

print('Calculating Relative Entropy')
relEntropy = 0
entropyDict = {}
for char in freqDict.keys():
    inputRatio = float(inputBuffer.count(char)) / float(len(inputBuffer))
    ratioTerm = np.divide(float(inputBuffer.count(char)), float(freqDict[char]))
    if (ratioTerm != 0.0):
        entropyTerm = np.multiply(inputRatio, \
            np.log2(inputRatio / float(freqDict[char])))
        entropyDict[str(char)] = float(entropyTerm)
    else:
        entropyDict[str(char)] = 0.0
        entropyTerm = 0
    relEntropy += entropyTerm

print('Relative Entropy: ' + str(relEntropy))
