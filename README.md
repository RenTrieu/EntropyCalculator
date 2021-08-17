# RelativeEntropy
Script that facilitates analysis of entropy of a given file using an arbitrary character frequency distribution.

## Usage

```
    ./relativeEntropy.py [Input File] [Frequency Distribution]
```

## Uses the Relative Entropy Formula

Relative Entropy was calculated via the following formula:

<img src=https://render.githubusercontent.com/render/math?math=D_{KL}\left(P_{||}Q)=\sum_{i}p_{i}\log\left(\frac{p_{i}}{q_{i}}\right)>

Where ``p`` corresponds to the input distribution and ``q`` corresponds to the 
baseline distribution.
