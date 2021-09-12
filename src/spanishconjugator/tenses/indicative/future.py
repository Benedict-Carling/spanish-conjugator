# -*- coding: iso-8859-15 -*-
def indicative_future(root_verb, pronoun):
    if pronoun == "yo":
        if root_verb[-2:] == "ar" or "er" or "ir":
            conjugation = root_verb + "é"
            return conjugation

    if pronoun == "tu":
        if root_verb[-2:] == "ar" or "er" or "ir":
            conjugation = root_verb + "ás"
            return conjugation

    if pronoun == "usted":
        if root_verb[-2:] == "ar" or "er" or "ir":
            conjugation = root_verb + "á"
            return conjugation

    if pronoun == "nosotros":
        if root_verb[-2:] == "ar" or "er" or "ir":
            conjugation = root_verb + "emos"
            return conjugation

    if pronoun == "vosotros":
        if root_verb[-2:] == "ar" or "er" or "ir":
            conjugation = root_verb + "éis"
            return conjugation

    if pronoun == "ustedes":
        if root_verb[-2:] == "ar" or "er" or "ir":
            conjugation = root_verb + "án"
            return conjugation
