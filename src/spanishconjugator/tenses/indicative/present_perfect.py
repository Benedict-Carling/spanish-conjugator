# -*- coding: iso-8859-15 -*-
from spanishconjugator.irregulars.irregular_dict              import irregulars_dictionary
def indicative_present_perfect_first_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["present_perfect"]["yo"]
        return conjugation
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return "he " + conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return "he " + conjugation

def indicative_present_perfect_first_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["present_perfect"]["nosotros"]
        return conjugation
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return "hemos " + conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return "hemos " + conjugation

def indicative_present_perfect_second_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["present_perfect"]["tu"]
        return conjugation
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return "has " + conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return "has " + conjugation

def indicative_present_perfect_second_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["present_perfect"]["vosotros"]
        return conjugation
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return "habéis " + conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return "habéis " + conjugation

def indicative_present_perfect_third_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["present_perfect"]["usted"]
        return conjugation
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return "ha " + conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return "ha " + conjugation

def indicative_present_perfect_third_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["present_perfect"]["ustedes"]
        return conjugation
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return "han " + conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return "han " + conjugation

def indicative_present_perfect(root_verb, pronoun):
    if pronoun == "yo":
        return indicative_present_perfect_first_person_singular(root_verb)

    elif pronoun == "tu":
        return indicative_present_perfect_second_person_singular(root_verb)
        
    elif pronoun == "usted" or pronoun == "el" or pronoun == "ella":
        return indicative_present_perfect_third_person_singular(root_verb)
        
    elif pronoun == "nosotros":
        return indicative_present_perfect_first_person_plural(root_verb)
        
    elif pronoun == "vosotros":
        return indicative_present_perfect_second_person_plural(root_verb)
        
    elif pronoun == "ustedes" or pronoun == "ellos" or pronoun == "ellas":
        return indicative_present_perfect_third_person_plural(root_verb)

    else:
        # no pronoun is given
        _dict = {'el/ella/usted': indicative_present_perfect_third_person_singular(root_verb), \
                 'ellos/ellas/ustedes':indicative_present_perfect_third_person_plural(root_verb),\
                 'tu':indicative_present_perfect_second_person_singular(root_verb),\
                 'vosotros':indicative_present_perfect_second_person_plural(root_verb),\
                 'yo':indicative_present_perfect_first_person_singular(root_verb),\
                 'nosotros':indicative_present_perfect_first_person_plural(root_verb)\
                }
        return _dict