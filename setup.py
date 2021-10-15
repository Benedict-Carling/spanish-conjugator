from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="spanishconjugator",
    version="2.3.275",
    description="A python library to conjugate spanish words with parameters tense, mood and pronoun",
    packages=[
        "spanishconjugator",
        "spanishconjugator.tenses",
        "spanishconjugator.tenses.conditional",
        "spanishconjugator.tenses.indicative",
        "spanishconjugator.tenses.imperative",
        "spanishconjugator.tenses.subjunctive",
        "spanishconjugator.irregulars",
    ],
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    extras_require={
        "dev": ["pytest", "check-manifest", "twine"],
    },
    url="https://github.com/Benedict-Carling/spanish-conjugator",
    author="Benedict Carling",
    author_email="bencarling1@gmail.com",
)
