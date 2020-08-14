# Spanish Conjugator 🇪🇸
![GitHub repo size](https://img.shields.io/github/repo-size/Benedict-Carling/spanish-conjugator)
![GitHub search hit counter](https://img.shields.io/github/search/Benedict-Carling/spanish-conjugator/goto)

A class Conjugator containing a function conjugate which conjugates spanish verbs by tense, mood and pronoun. 

## Installation
`pip install spanishconjugator`

## Example usage
Example python usage; the `conjugate` function of the `Conjugator` Class takes 4 parameters being root-verb, tense, mood, pronoun respectively  
```python
from spanishconjugator import Conjugator
imperfect_conjugation = Conjugator().conjugate('hablar','imperfect','imperitive','yo')
print(imperfect_conjugation)
```


# Developing
if you would like to help develop spanishconjugator, here is how your install developer dependencies;
run the following inside your virtual enviroment.
`pip install -e .[dev]`
