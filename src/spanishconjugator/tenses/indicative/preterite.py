# -*- coding: iso-8859-15 -*-
def indicative_preterite(root_verb, pronoun):
    if pronoun == "yo":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "é"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "í"
            return conjugation
    if pronoun == "tu":

        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "aste"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "iste"
            return conjugation
    if pronoun == "usted":

        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ó"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ió"
            return conjugation
    if pronoun == "nosotros":

        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "amos"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "imos"
            return conjugation
    if pronoun == "vosotros":

        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "asteis"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "isteis"
            return conjugation

    if pronoun == "ustedes":
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "aron"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ieron"
            return conjugation
