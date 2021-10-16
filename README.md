# Spanish Conjugator 🇪🇸
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/Imperial-iGEM/DJANGO-Assembly-Methods/Django%20CI)
![GitHub repo size](https://img.shields.io/github/repo-size/Benedict-Carling/spanish-conjugator)
![PyPI - Downloads](https://img.shields.io/pypi/dm/spanishconjugator)
![GitHub top language](https://img.shields.io/github/languages/top/Benedict-Carling/spanish-conjugator)
![GitHub](https://img.shields.io/github/license/Benedict-Carling/spanish-conjugator)
![PyPI](https://img.shields.io/pypi/v/spanishconjugator)


A class Conjugator containing a function conjugate which conjugates spanish verbs by tense, mood and pronoun. 

## Installation
`pip install spanishconjugator`

## Example usage
Example python usage; the `conjugate` function of the `Conjugator` Class takes 4 parameters being root-verb, tense, mood, pronoun respectively

```python
from spanishconjugator import Conjugator
imperfect_conjugation = Conjugator().conjugate('hablar','imperfect','indicative','yo')
print(imperfect_conjugation)
>>> hablaba
```
## Tenses, Moods and Pronouns implemented

All pronouns are implemented
```yo, tu, usted, nosotros, vosotros, ustedes```

All moods currently implemented are
```indicative, conditional```

All tenses currently implemented are
```present, imperfect, preterite, future, present_perfect, past_anterior, future_perfect, conditional_simple```

Exaple usage of different moods/tenses with hablar and yo

### Indicative Present

```python
Conjugator().conjugate('hablar','present','indicative','yo')
>>> hablo
```

In case of indicative present, 4th param pronoun is optional.
```python
from spanishconjugator import Conjugator
present_indicative_conjugation = Conjugator().conjugate('hablar','present','indicative')
print(present_indicative_conjugation)
>>> {'el/ella/usted': 'habla', 'ellos/ellas/ustedes': 'hablan', 'tu': 'hablas', 'vosotros': 'hablÃ¡is', 'yo': 'hablo', 'nosotros': 'hablamos'}
```

### Indicative Imperfect

```python
Conjugator().conjugate('hablar','imperfect','indicative','yo')
>>> hablaba
```
### Indicative Preterite

```python
Conjugator().conjugate('hablar','preterite','indicative','yo')
>>> hablé
```
### Indicative Future

```python
Conjugator().conjugate('hablar','future','indicative','yo')
>>> hablaré
```
### Indicative Present_Perfect

```python
Conjugator().conjugate('hablar','present_perfect','indicative','yo')
>>> he hablado
```
### Indicative Past_Anterior

```python
Conjugator().conjugate('hablar','past_anterior','indicative','yo')
>>> hube hablado
```
### Indicative Future_Perfect

```python
Conjugator().conjugate('hablar','future_perfect','indicative','yo')
>>> habré hablado
```
### Conditional Simple

```python
Conjugator().conjugate('hablar','simple_conditional','conditional','yo')
>>> hablaría
```
### Conditional Perfect

```python
Conjugator().conjugate('hablar','perfect','conditional','yo')
>>> habría hablado
```
### Imperative Afferative

```python
Conjugator().conjugate('hablar','affirmative','imperative','tu')
>>> habla
```
### Imperative Negative

```python
Conjugator().conjugate('hablar','negative','imperative','tu')
>>> hables
```
### Subjunctive Present

```python
Conjugator().conjugate('hablar','present','subjunctive','yo')
>>> hable
```
### Subjunctive Imperfect

```python
Conjugator().conjugate('hablar','imperfect','subjunctive','yo')
>>> hablara
```
### Subjunctive Imperfect_se

```python
Conjugator().conjugate('hablar','imperfect_se','subjunctive','yo')
>>> hablase
```
### Subjunctive Future

```python
Conjugator().conjugate('hablar','future','subjunctive','yo')
>>> hablare
```

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

output should show the different tenses implemented should pass their unit tests as below.(27/08/2020)
![alt text](https://github.com/Benedict-Carling/spanish-conjugator/blob/master/images/pytest.png?raw=true)

## Developing - Submission

To submit code to this repositry please fork and submit a pull request 🚀

# Alternative Versions
Check out the Javascript npm version of the library if you are working in a node or browser enviroment

https://github.com/Benedict-Carling/spanish-conjugatorjs
