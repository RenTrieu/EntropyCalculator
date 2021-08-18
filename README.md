# EntropyCalculator
Script that facilitates analysis of entropy of a given file using an arbitrary 
character frequency distribution.

## Dependencies
```
numpy>=1.21.2
```

## Usage

Calculates the Shannon entropy of the text within the specified file.
```
    ./entropyCalc.py [Input File] 
```

Calculates the relative entropy of the text within the specified file
when a baseline character frequency distribution is specified.
```
    ./entropyCalc.py [Input File] --baseline [Baseline Distribution]
```

## Shannon Entropy Formula

When a baseline is not specified, the script will calculate the entropy
using the Shannon Entropy formula.

![equation](https://latex.codecogs.com/gif.latex?H%20%3D%20%5Csum_%7Bi%7Dp_%7Bi%7D%5Clog%20p_%7Bi%7D)

## Relative Entropy Formula

When a baseline is specified, the script will calculate the relative entropy
via the Kullback-Leibler divergence formula.

![equation](https://latex.codecogs.com/gif.latex?D_%7BKL%7D%28P_%7B%7C%7C%7DQ%29%3D%5Csum_%7Bi%7Dp_%7Bi%7Dlog%5Cleft%28%5Cfrac%7Bp_%7Bi%7D%7D%7Bq_%7Bi%7D%7D%5Cright%29)

Where ![equation](https://latex.codecogs.com/gif.latex?p_%7Bi%7D) is the 
proportion of the given character relative to the entire input distribution
and ![equation](https://latex.codecogs.com/gif.latex?q_%7Bi%7D) 
is the proportion from the baseline distribution.

## Example Files
``ExampleFiles`` contains example text files to run the script on.
``DistributionFiles`` contains an example character frequency distribution file.

## Sources
Built using Ben Downing's [Entropy Article](https://redcanary.com/blog/threat-hunting-entropy/)
as a reference and for the example baseline distribution.
