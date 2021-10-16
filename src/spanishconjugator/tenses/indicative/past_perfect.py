# -*- coding: iso-8859-15 -*-
from spanishconjugator.irregulars.irregular_dict              import irregulars_dictionary
def indicative_past_perfect_first_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["past_perfect"]["yo"]
        return conjugation
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return "había " + conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return "había " + conjugation

def indicative_past_perfect_first_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["past_perfect"]["nosotros"]
        return conjugation
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return "habíamos " + conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return "habíamos " + conjugation

def indicative_past_perfect_second_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["past_perfect"]["tu"]
        return conjugation
    except:
        if root_verb[-2:] == "ar":
                conjugation = root_verb[:-2] + "ado"
                return "habías " + conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return "habías " + conjugation

def indicative_past_perfect_second_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["past_perfect"]["vosotros"]
        return conjugation
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return "habíais " + conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return "habíais " + conjugation

def indicative_past_perfect_third_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["past_perfect"]["usted"]
        return conjugation
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return "había " + conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return "había " + conjugation

def indicative_past_perfect_third_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["past_perfect"]["ustedes"]
        return conjugation
    except:
        if root_verb[-2:] == "ar":
            conjugation = root_verb[:-2] + "ado"
            return "habían " + conjugation
        if root_verb[-2:] == "er" or "ir":
            conjugation = root_verb[:-2] + "ido"
            return "habían " + conjugation

def indicative_past_perfect(root_verb, pronoun):
    if pronoun == "yo":
        return indicative_past_perfect_first_person_singular(root_verb)

    elif pronoun == "tu":
        return indicative_past_perfect_second_person_singular(root_verb)
        
    elif pronoun == "usted" or pronoun == "el" or pronoun == "ella":
        return indicative_past_perfect_third_person_singular(root_verb)
        
    elif pronoun == "nosotros":
        return indicative_past_perfect_first_person_plural(root_verb)
        
    elif pronoun == "vosotros":
        return indicative_past_perfect_second_person_plural(root_verb)
        
    elif pronoun == "ustedes" or pronoun == "ellos" or pronoun == "ellas":
        return indicative_past_perfect_third_person_plural(root_verb)

    else:
        # no pronoun is given
        _dict = {'el/ella/usted': indicative_past_perfect_third_person_singular(root_verb), \
                 'ellos/ellas/ustedes':indicative_past_perfect_third_person_plural(root_verb),\
                 'tu':indicative_past_perfect_second_person_singular(root_verb),\
                 'vosotros':indicative_past_perfect_second_person_plural(root_verb),\
                 'yo':indicative_past_perfect_first_person_singular(root_verb),\
                 'nosotros':indicative_past_perfect_first_person_plural(root_verb)\
                }
        return _dict
       