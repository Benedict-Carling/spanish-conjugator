# Spanish Conjugator 🇪🇸
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/Imperial-iGEM/DJANGO-Assembly-Methods/Django%20CI)
![GitHub repo size](https://img.shields.io/github/repo-size/Benedict-Carling/spanish-conjugator)
![PyPI - Downloads](https://img.shields.io/pypi/dm/spanishconjugator)
![GitHub top language](https://img.shields.io/github/languages/top/Benedict-Carling/spanish-conjugator)
![GitHub](https://img.shields.io/github/license/Benedict-Carling/spanish-conjugator)


A class Conjugator containing a function conjugate which conjugates spanish verbs by tense, mood and pronoun. 

## Installation
`pip install spanishconjugator`

## Example usage
Example python usage; the `conjugate` function of the `Conjugator` Class takes 4 parameters being root-verb, tense, mood, pronoun respectively  
```python
from spanishconjugator.spanishconjugator import Conjugator
imperfect_conjugation = Conjugator().conjugate('hablar','imperfect','indicitive','yo')
print(imperfect_conjugation)
>>> hablaba
```

## Tenses, Moods and Pronouns implemented

All pronouns are implemented
```yo, tu, usted, nosotros, vosotros, ustedes```

The following tense mood combinations are currently implemented
```indicitive present```
```indicitive imperfect```
```indicitive preterite```
```indicitive future```
```indicitive present_perfect```
```indicitive past_perfect```
```indicitive past_anterior```
```indicitive future perfect```
```conditional simple```



## Developing
if you would like to help develop spanishconjugator, follow succeeding code

Whilst in command line create a folder in which you would like to work (name only reccommended)

`$ mkdir spanish_conjugator_enviroment`

change directory into the enviroment you have just made

`$ cd spanish_conjugator_enviroment`

install virtualenv

`$ pip install virtualenv`

create a virtual enviroment from path of python3

`$ virtualenv -p $(which python3) my_venv`

activate virtual enviroment

`$ source my_venv/bin/activate`

> tip: once you want to disactivate your virtual enviroment simply run `$ deactivate`

Clone Spanish-Conjugator

`$ git clone https://github.com/Benedict-Carling/spanish-conjugator.git`

Install developer dependencies for unit test e.g pytest and for other library tools

`pip install -e .[dev]`

## Developing - Testing

We have chosen to use the library pytest for our unit test
At this point in the developing guide you can check the code works by running it against out current unit tests located in the `/tests` folder

`$ pytest`

## Developing - Submission

to submit code to this repositry please fork and submit a pull request 🚀


