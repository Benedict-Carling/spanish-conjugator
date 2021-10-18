# -*- coding: iso-8859-15 -*-
from spanishconjugator.irregulars.irregular_dict              import irregulars_dictionary
def indicative_imperfect_first_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["imperfect"]["yo"]
        return conjugation
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "aba"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ía"
            return conjugation

def indicative_imperfect_first_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["imperfect"]["nosotros"]
        return conjugation
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ábamos"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "íamos"
            return conjugation

def indicative_imperfect_second_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["imperfect"]["tu"]
        return conjugation
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "abas"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ías"
            return conjugation

def indicative_imperfect_second_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["imperfect"]["vosotros"]
        return conjugation
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "abais"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "íais"
            return conjugation

def indicative_imperfect_third_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["imperfect"]["usted"]
        return conjugation
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "aba"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ía"
            return conjugation

def indicative_imperfect_third_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["imperfect"]["ustedes"]
        return conjugation
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "aban"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ían"
            return conjugation

def indicative_imperfect(root_verb, pronoun):
    if pronoun == "yo":
        return indicative_imperfect_first_person_singular(root_verb)

    elif pronoun == "tu":
        return indicative_imperfect_second_person_singular(root_verb)
        
    elif pronoun == "usted" or pronoun == "el" or pronoun == "ella":
        return indicative_imperfect_third_person_singular(root_verb)
        
    elif pronoun == "nosotros":
        return indicative_imperfect_first_person_plural(root_verb)
        
    elif pronoun == "vosotros":
        return indicative_imperfect_second_person_plural(root_verb)
        
    elif pronoun == "ustedes" or pronoun == "ellos" or pronoun == "ellas":
        return indicative_imperfect_third_person_plural(root_verb)

    else:
        # no pronoun is given
        _dict = {'el/ella/usted': indicative_imperfect_third_person_singular(root_verb), \
                 'ellos/ellas/ustedes':indicative_imperfect_third_person_plural(root_verb),\
                 'tu':indicative_imperfect_second_person_singular(root_verb),\
                 'vosotros':indicative_imperfect_second_person_plural(root_verb),\
                 'yo':indicative_imperfect_first_person_singular(root_verb),\
                 'nosotros':indicative_imperfect_first_person_plural(root_verb)\
                }
        return _dict
        