# -*- coding: iso-8859-15 -*-
def indicative_present_first_person_singular(root_verb):
    if root_verb[-2:] == "ar":
        conjugation = root_verb[:-2] + "o"
        return conjugation
    if root_verb[-2:] == "er":
        conjugation = root_verb[:-2] + "o"
        return conjugation
    if root_verb[-2:] == "ir":
        conjugation = root_verb[:-2] + "o"
        return conjugation


def indicative_present_first_person_plural(root_verb):
    if root_verb[-2:] == "ar":
        conjugation = root_verb[:-2] + "amos"
        return conjugation
    if root_verb[-2:] == "er":
        conjugation = root_verb[:-2] + "emos"
        return conjugation
    if root_verb[-2:] == "ir":
        conjugation = root_verb[:-2] + "imos"
        return conjugation


def indicative_present_second_person_singular(root_verb):
    if root_verb[-2:] == "ar":
        conjugation = root_verb[:-2] + "as"
        return conjugation
    if root_verb[-2:] == "er":
        conjugation = root_verb[:-2] + "es"
        return conjugation
    if root_verb[-2:] == "ir":
        conjugation = root_verb[:-2] + "es"
        return conjugation


def indicative_present_second_person_plural(root_verb):
    if root_verb[-2:] == "ar":
        conjugation = root_verb[:-2] + "áis"
        return conjugation
    if root_verb[-2:] == "er":
        conjugation = root_verb[:-2] + "éis"
        return conjugation
    if root_verb[-2:] == "ir":
        conjugation = root_verb[:-2] + "ís"
        return conjugation


def indicative_present_third_person_singular(root_verb):
    if root_verb[-2:] == "ar":
        conjugation = root_verb[:-2] + "a"
        return conjugation
    if root_verb[-2:] == "er":
        conjugation = root_verb[:-2] + "e"
        return conjugation
    if root_verb[-2:] == "ir":
        conjugation = root_verb[:-2] + "e"
        return conjugation


def indicative_present_third_person_plural(root_verb):
    if root_verb[-2:] == "ar":
        conjugation = root_verb[:-2] + "an"
        return conjugation
    if root_verb[-2:] == "er":
        conjugation = root_verb[:-2] + "en"
        return conjugation
    if root_verb[-2:] == "ir":
        conjugation = root_verb[:-2] + "en"
        return conjugation


def indicative_present(root_verb, pronoun):
    if pronoun == "yo":
        return indicative_present_first_person_singular(root_verb)

    elif pronoun == "tu":
        return indicative_present_second_person_singular(root_verb)

    elif pronoun == "usted" or pronoun == "el" or pronoun == "ella":
        return indicative_present_third_person_singular(root_verb)

    elif pronoun == "nosotros":
        return indicative_present_first_person_plural(root_verb)

    elif pronoun == "vosotros":
        return indicative_present_second_person_plural(root_verb)

    elif pronoun == "ustedes" or pronoun == "ellos" or pronoun == "ellas":
        return indicative_present_third_person_plural(root_verb)

    else:
        # no pronoun is given
        _dict = {
            "el/ella/usted": indicative_present_third_person_singular(root_verb),
            "ellos/ellas/ustedes": indicative_present_third_person_plural(root_verb),
            "tu": indicative_present_second_person_singular(root_verb),
            "vosotros": indicative_present_second_person_plural(root_verb),
            "yo": indicative_present_first_person_singular(root_verb),
            "nosotros": indicative_present_first_person_plural(root_verb),
        }
        return _dict
