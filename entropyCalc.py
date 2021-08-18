#!/usr/bin/env python3
# Program: EntropyCalculator 
# Author: Darren Trieu Nguyen
# Version: 0.2
# Function: Takes in an arbitrary character frequency distribution to
#           calculate the entropy of a given file

import sys
import json
import numpy as np
import argparse
import logging

""" Class that houses EntropyCalculator
"""
class EntropyCalculator:

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
            parser.add_argument('inputFiles', metavar='inputFiles', nargs='+',
                                help='Input files for which to calculate' \
                                ' entropy')
            # TODO: Add to documentation how baseline files should be formatted
            parser.add_argument('-b', '--baseline', default=None,
                                help='The file containing the' \
                                ' distribution to be used as the baseline for' \
                                ' the relative entropy calculation')
            parser.add_argument('-v', '--verbose',
                                help='Increases output verbosity', \
                                action='store_true')
            parser.add_argument('--log', nargs='?', default='WARNING',
                                help='Controls logging verbosity based off of'\
                                ' log message priority. Levels include:'\
                                'DEBUG, INFO, WARNING, ERROR, CRITICAL')
            # TODO: Give user the ability to specify an output file/directory
            # TODO: Give user the ability to output a file containing
            #       character distributions in the form of a serialized 
            #       dictionary

            args = parser.parse_args()

            # Initializing log file and log level
            logLevel = args.log
            logFile = None

            # Initializing logging
            self.logger = logging.getLogger(self.__class__.__name__)


            numeric_level = getattr(logging, logLevel.upper(), None)
            if not isinstance(numeric_level, int):
                raise ValueError('Invalid log level: %s' % logLevel)
            if logFile is not None:
                logging.basicConfig(filename=logFile, filemode='w', \
                                    level=numeric_level)
            else:
                logging.basicConfig(level=numeric_level)

            # Feeding input files into entropy functions
            for inputFile in args.inputFiles:
                self.logger.info('Analyzing ' + str(inputFile))

                # If baseline is specified, runs the Relative Entropy 
                # calculation
                if (args.baseline is not None):
                    inputBuffer, freqDict = self.parse(inputFile, args.baseline)
                    relEntropy = self.calcRelEntropy(inputBuffer, freqDict)
                    print('Relative Entropy of ' + str(inputFile) \
                          + ': ' + str(relEntropy))
                else:
                    inputBuffer = self.parse(inputFile)
                    shanEntropy = self.calcShanEntropy(inputBuffer)
                    print('Shannon Entropy of ' + str(inputFile) \
                          + ': ' + str(shanEntropy))

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

    """ Parsing function
        Takes in the input file and parses them
    """
    def parse(self, inputFile, distFile=None):
        
        # Reading the Input File
        inputBuffer = None
        with open(str(inputFile), 'r') as inputF:
            inputBuffer = inputF.read()

        if (inputBuffer is not None):
            self.logger.info('Input file successfully read.')
        else:
            self.logger.critical('Failed to read input file. Exiting.')
            sys.exit(2)
        if distFile is None:
            return inputFile

        # Reading the Dist File into a dictionary
        freqDict = None
        with open(str(distFile), 'r') as distF:
            freqDict = json.load(distF)

        if (freqDict is not None):
            self.logger.info('Distribution file successfully read.')
        else:
            self.logger.critical('Failed to read distribution file. Exiting.')
            sys.exit(3)
            # TODO: Add exit codes and meanings to documentation

        return inputBuffer, freqDict

    """ Count the number of occurrences of a given character in the input file for
        every character listed in freqDict
        And calculates the relative entropy term corresponding to the character
        Then adds the term to the total sum
    """
    def calcRelEntropy(self, inputBuffer, freqDict):
        self.logger.info('Calculating Relative Entropy.')

        relEntropy = 0
        entropyDict = {}

        # Calculating the entropy term for each unique character
        for char in freqDict.keys():

            # Calculating the current unique character's probability p_i
            inputRatio = float(inputBuffer.count(char)) \
                         / float(len(inputBuffer))

            # Calculating the normalized proportion term (p_i/q_i)
            ratioTerm = np.divide(float(inputBuffer.count(char)), \
                        float(freqDict[char]))

            # Calculating the full entropy term 
            if (ratioTerm != 0.0):
                entropyTerm = np.multiply(inputRatio, \
                    np.log2(inputRatio / float(freqDict[char])))
                entropyDict[str(char)] = float(entropyTerm)

            # Handling cases where the unique character does not have a nonzero
            # number of occurrences
            else:
                entropyTerm = 0
                entropyDict[str(char)] = 0.0

            # Summing the entropyTerm to the total Entropy
            relEntropy += entropyTerm

        self.logger.info('Relative Entropy: ' + str(relEntropy))
        return relEntropy

    """ Calculates the Shannon Entropy for the given inputBuffer
    """
    def calcShanEntropy(self, inputBuffer):
        self.logger.info('Calculating Shannon Entropy.')

        # Getting a list of all unique characters in the inputBuffer
        charList = sorted(list(set(inputBuffer)))

        shanEntropy = 0
        entropyDict = {}

        # Calculating the entropy term for each unique character
        for char in charList:

            # Calculating the current unique character's probability p_i
            inputRatio = float(inputBuffer.count(char)) \
                         / float(len(inputBuffer))

            # Calculating the full entropy term
            if (inputRatio != 0.0):
                entropyTerm = -np.multiply(inputRatio, np.log2(inputRatio))
                entropyDict[str(char)] = float(entropyTerm)
                shanEntropy += entropyTerm
            else:
                entropyTerm = 0
                entropyDict[str(char)] = 0.0

        self.logger.info('Shannon Entropy: ' + str(shanEntropy))
        return shanEntropy


entCalc = EntropyCalculator()
