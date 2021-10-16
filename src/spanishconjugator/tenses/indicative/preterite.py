# -*- coding: iso-8859-15 -*-
from spanishconjugator.irregulars.irregular_dict              import irregulars_dictionary
def indicative_preterite_first_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["preterite"]["yo"]
        return conjugation
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "é"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "í"
            return conjugation

def indicative_preterite_first_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["preterite"]["nosotros"]
        return conjugation
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "amos"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "imos"
            return conjugation

def indicative_preterite_second_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["preterite"]["tu"]
        return conjugation
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "aste"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "iste"
            return conjugation

def indicative_preterite_second_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["preterite"]["vosotros"]
        return conjugation
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "asteis"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "isteis"
            return conjugation

def indicative_preterite_third_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["preterite"]["usted"]
        return conjugation
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ó"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ió"
            return conjugation

def indicative_preterite_third_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["preterite"]["ustedes"]
        return conjugation
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "aron"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ieron"
            return conjugation

def indicative_preterite(root_verb, pronoun):
    if pronoun == "yo":
        return indicative_preterite_first_person_singular(root_verb)

    elif pronoun == "tu":
        return indicative_preterite_second_person_singular(root_verb)
        
    elif pronoun == "usted" or pronoun == "el" or pronoun == "ella":
        return indicative_preterite_third_person_singular(root_verb)
        
    elif pronoun == "nosotros":
        return indicative_preterite_first_person_plural(root_verb)
        
    elif pronoun == "vosotros":
        return indicative_preterite_second_person_plural(root_verb)
        
    elif pronoun == "ustedes" or pronoun == "ellos" or pronoun == "ellas":
        return indicative_preterite_third_person_plural(root_verb)

    else:
        # no pronoun is given
        _dict = {'el/ella/usted': indicative_preterite_third_person_singular(root_verb), \
                 'ellos/ellas/ustedes':indicative_preterite_third_person_plural(root_verb),\
                 'tu':indicative_preterite_second_person_singular(root_verb),\
                 'vosotros':indicative_preterite_second_person_plural(root_verb),\
                 'yo':indicative_preterite_first_person_singular(root_verb),\
                 'nosotros':indicative_preterite_first_person_plural(root_verb)\
                }
        return _dict