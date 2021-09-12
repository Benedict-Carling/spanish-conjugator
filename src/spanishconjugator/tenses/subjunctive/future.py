# -*- coding: iso-8859-15 -*-
def subjunctive_future(root_verb, pronoun):
    if pronoun == "yo":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "are"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "iere"
            return conjugation

    if pronoun == "tu":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ares"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ieres"
            return conjugation

    if pronoun == "usted":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "are"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "iere"
            return conjugation
    if pronoun == "nosotros":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "áremos"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "iéremos"
            return conjugation

    if pronoun == "vosotros":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "areis"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "iereis"
            return conjugation

    if pronoun == "ustedes":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "aren"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ieren"
            return conjugation
