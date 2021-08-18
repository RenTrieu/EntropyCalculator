# RelativeEntropy
Script that facilitates analysis of entropy of a given file using an arbitrary 
character frequency distribution.

## Dependencies
```
numpy>=1.21.2
```

## Usage

```
    ./relativeEntropy.py [Input File] [Frequency Distribution]
```

## Uses the Relative Entropy Formula

Relative Entropy was calculated via the following formula:

![equation](https://latex.codecogs.com/gif.latex?D_%7BKL%7D%28P_%7B%7C%7C%7DQ%29%3D%5Csum_%7Bi%7Dp_%7Bi%7Dlog%5Cleft%28%5Cfrac%7Bp_%7Bi%7D%7D%7Bq_%7Bi%7D%7D%5Cright%29)

Where ![equation](https://latex.codecogs.com/gif.latex?p_%7Bi%7D) is the 
proportion of the given character relative to the entire input distribution
and ![equation](https://latex.codecogs.com/gif.latex?q_%7Bi%7D) 
is the proportion from the baseline distribution.

