from setuptools import setup

setup(
    name='spanishconjugator',
    version='0.0.2',
    description='A python library to conjugate spanish words with parameters tense, mood and pronoun',
    py_modules=["spanishconjugator"],
    package_dir={'': 'src'},
)