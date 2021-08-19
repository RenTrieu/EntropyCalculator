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

### Baseline File Format
Baseline (distribution) files are ``.json`` formatted such that each unique 
character and their corresponding probability are value pairs. The 
unique characters are formatted as strings, while the probabilities are 
formatted as floats. This can be seen in the included example ``alexaTop.json``
which contains the following:
```
{
    "-" : 0.013342298553905901,
    "_" : 9.04562613824129e-06,
    "0" : 0.0024875471880163543,
    "1" : 0.004884638114650296,
    "2" : 0.004373560237839663,
    "3" : 0.0021136613076357144,
    "4" : 0.001625197496170685,
    "5" : 0.0013070929769758662,
    "6" : 0.0014880054997406921,
    "7" : 0.001471421851820583,
    "8" : 0.0012663876593537805,
    "9" : 0.0010327089841158806,
    "a" : 0.07333590631143488,
    "b" : 0.04293204925644953,
    "c" : 0.027385633133525503,
    "d" : 0.02769469202658208,
    "e" : 0.07086192756262588,
    "f" : 0.01249653250998034,
    "g" : 0.038516276096631406,
    "h" : 0.024017645001386995,
    "i" : 0.060447396668797414,
    "j" : 0.007082725266242929,
    "k" : 0.01659570875496002,
    "l" : 0.05815885325582237,
    "m" : 0.033884915513851865,
    "n" : 0.04753175014774523,
    "o" : 0.09413783122067709,
    "p" : 0.042555148167356144,
    "q" : 0.0017231917793349655,
    "r" : 0.06460084667060655,
    "s" : 0.07214640647425614,
    "t" : 0.06447722311338391,
    "u" : 0.034792493336388744,
    "v" : 0.011637198026847418,
    "w" : 0.013318176884203925,
    "x" : 0.003170491961453572,
    "y" : 0.016381628936354975,
    "z" : 0.004715786426736459
}

```

## Exit Codes

##### 0
Script executed successfully

##### 1
Script failed to read a file

##### 2
Incorrect CLI usage

## Sources

#### Conceptual References
Built using Ben Downing's [Entropy Article](https://redcanary.com/blog/threat-hunting-entropy/)
as a reference and for the example baseline distribution.

#### Example References

##### Hamlet
The raw text for Hamlet was found [here](https://shakespeare.folger.edu/shakespeares-works/hamlet/download/).

##### ILOVEYOU
The raw text for the ILOVEYOU worm was found [here](http://www.cexx.org/loveletter.htm).

##### Malicious Domains
Malicious domains were taken from a [Fraudulent Sites Database](https://db.aa419.org/fakebankslist.php)
and stripped of extraneous repetitive text such as ``http``, ``www``, and ``com``.
