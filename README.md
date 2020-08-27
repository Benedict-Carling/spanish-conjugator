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
from spanishconjugator import Conjugator
imperfect_conjugation = Conjugator().conjugate('hablar','imperfect','indicitive','yo')
print(imperfect_conjugation)
>>> hablaba
```

## Tenses, Moods and Pronouns implemented

All pronouns are implemented
```yo, tu, usted, nosotros, vosotros, ustedes```

All moods currently implemented are
```indicitive, conditional```

All tenses currently implemented are
```present, imperfect, preterite, future, present_perfect, past_anterior, future_perfect, conditional_simple```

Exaple usage of different moods/tenses with hablar and yo

### Indicitive Present

```python
Conjugator().conjugate('hablar','present','indicitive','yo')
>>> hablo
```
### Indicitive Imperfect

```python
Conjugator().conjugate('hablar','imperfect','indicitive','yo')
>>> hablaba
```
### Indicitive Preterite

```python
Conjugator().conjugate('hablar','preterite','indicitive','yo')
>>> hablé
```
### Indicitive Future

```python
Conjugator().conjugate('hablar','future','indicitive','yo')
>>> hablaré
```
### Indicitive Present_Perfect

```python
Conjugator().conjugate('hablar','present_perfect','indicitive','yo')
>>> he hablado
```
### Indicitive Past_Anterior

```python
Conjugator().conjugate('hablar','past_anterior','indicitive','yo')
>>> hube hablado
```
### Indicitive Future_Perfect

```python
Conjugator().conjugate('hablar','future_perfect','indicitive','yo')
>>> habré hablado
```
### Conditional Simple

```python
Conjugator().conjugate('hablar','simple_conditional','conditional','yo')
>>> hablaría
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

to submit code to this repositry please fork and submit a pull request 🚀


