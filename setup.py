from setuptools import setup

setup(
    name='spanishconjugator',
    version='0.0.3',
    description='A python library to conjugate spanish words with parameters tense, mood and pronoun',
    py_modules=["spanishconjugator"],
    package_dir={'': 'src'},
    classifiers = [
        "Programming Language :: python :: 3",
        "Programming Language :: python :: 3.6",
        "Programming Language :: python :: 3.7",
        "Programming Language :: python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent"
    ]
)