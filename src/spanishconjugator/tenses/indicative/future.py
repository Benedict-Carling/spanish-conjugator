# -*- coding: iso-8859-15 -*-
from spanishconjugator.irregulars.irregular_dict              import irregulars_dictionary
def indicative_future_first_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["future"]["yo"]
        return conjugation
    except:
        if root_verb[-2:] == "ar" or "er" or "ir":
            conjugation = root_verb + "é"
            return conjugation

def indicative_future_first_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["future"]["nosotros"]
        return conjugation
    except:
        if root_verb[-2:] == "ar" or "er" or "ir":
            conjugation = root_verb + "emos"
            return conjugation

def indicative_future_second_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["future"]["tu"]
        return conjugation
    except:
        if root_verb[-2:] == "ar" or "er" or "ir":
            conjugation = root_verb + "ás"
            return conjugation

def indicative_future_second_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["future"]["vosotros"]
        return conjugation
    except:
        if root_verb[-2:] == "ar" or "er" or "ir":
            conjugation = root_verb + "éis"
            return conjugation

def indicative_future_third_person_singular(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["future"]["usted"]
        return conjugation
    except:
        if root_verb[-2:] == "ar" or "er" or "ir":
            conjugation = root_verb + "á"
            return conjugation

def indicative_future_third_person_plural(root_verb):
    try:
        conjugation = irregulars_dictionary[root_verb]["indicative"]["future"]["ustedes"]
        return conjugation
    except:
        if root_verb[-2:] == "ar" or "er" or "ir":
            conjugation = root_verb + "án"
            return conjugation

def indicative_future(root_verb, pronoun):
    if pronoun == "yo":
        return indicative_future_first_person_singular(root_verb)

    elif pronoun == "tu":
        return indicative_future_second_person_singular(root_verb)
        
    elif pronoun == "usted" or pronoun == "el" or pronoun == "ella":
        return indicative_future_third_person_singular(root_verb)
        
    elif pronoun == "nosotros":
        return indicative_future_first_person_plural(root_verb)
        
    elif pronoun == "vosotros":
        return indicative_future_second_person_plural(root_verb)
        
    elif pronoun == "ustedes" or pronoun == "ellos" or pronoun == "ellas":
        return indicative_future_third_person_plural(root_verb)

    else:
        # no pronoun is given
        _dict = {'el/ella/usted': indicative_future_third_person_singular(root_verb), \
                 'ellos/ellas/ustedes':indicative_future_third_person_plural(root_verb),\
                 'tu':indicative_future_second_person_singular(root_verb),\
                 'vosotros':indicative_future_second_person_plural(root_verb),\
                 'yo':indicative_future_first_person_singular(root_verb),\
                 'nosotros':indicative_future_first_person_plural(root_verb)\
                }
        return _dict
        