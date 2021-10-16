# -*- coding: iso-8859-15 -*-
def conditional_simple_conditional(root_verb, pronoun):
    if pronoun == "yo":
        if root_verb[-2:] == "ar" or "er" or "ir":
            conjugation = root_verb + "ía"
            return conjugation

    if pronoun == "tu":
        if root_verb[-2:] == "ar" or "er" or "ir":
            conjugation = root_verb + "ías"
            return conjugation

    if pronoun == "usted":
        if root_verb[-2:] == "ar" or "er" or "ir":
            conjugation = root_verb + "ía"
            return conjugation

    if pronoun == "nosotros":
        if root_verb[-2:] == "ar" or "er" or "ir":
            conjugation = root_verb + "íamos"
            return conjugation

    if pronoun == "vosotros":
        if root_verb[-2:] == "ar" or "er" or "ir":
            conjugation = root_verb + "íais"
            return conjugation

    if pronoun == "ustedes":
        if root_verb[-2:] == "ar" or "er" or "ir":
            conjugation = root_verb + "ían"
            return conjugation
