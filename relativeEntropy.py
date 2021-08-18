#!/usr/bin/env python3
# Program: RelativeEntropy
# Author: Darren Trieu Nguyen
# Version: 0.1
# Function: Takes in an arbitrary character frequency distribution to
#           calculate the relative entropy of a given file

import sys
import json
import numpy as np

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
