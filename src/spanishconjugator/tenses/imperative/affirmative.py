# -*- coding: iso-8859-15 -*-
def affirmative(root_verb, pronoun):
    if pronoun == "yo":
        return "prounoun 'yo' does not have imperative conjugations"

    if pronoun == "tu":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "a"
            return conjugation
        if root_verb[-2:] == "er":
            conjugation = root_verb[:-2] + "e"
            return conjugation
        if root_verb[-2:] == "ir":
            conjugation = root_verb[:-2] + "e"
            return conjugation

    if pronoun == "usted":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "e"
            return conjugation
        if root_verb[-2:] == "er":
            conjugation = root_verb[:-2] + "a"
            return conjugation
        if root_verb[-2:] == "ir":
            conjugation = root_verb[:-2] + "a"
            return conjugation

    if pronoun == "nosotros":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "emos"
            return conjugation
        if root_verb[-2:] == "er":
            conjugation = root_verb[:-2] + "amos"
            return conjugation
        if root_verb[-2:] == "ir":
            conjugation = root_verb[:-2] + "amos"
            return conjugation

    if pronoun == "vosotros":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ad"
            return conjugation
        if root_verb[-2:] == "er":
            conjugation = root_verb[:-2] + "ed"
            return conjugation
        if root_verb[-2:] == "ir":
            conjugation = root_verb[:-2] + "id"
            return conjugation

    if pronoun == "ustedes":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "en"
            return conjugation
        if root_verb[-2:] == "er":
            conjugation = root_verb[:-2] + "an"
            return conjugation
        if root_verb[-2:] == "ir":
            conjugation = root_verb[:-2] + "an"
            return conjugation
