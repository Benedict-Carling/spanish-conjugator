# -*- coding: iso-8859-15 -*-
def indicitive_imperfect(root_verb, pronoun):
    if pronoun == "yo":
        if root_verb[-2:] == "ar":
            try:
                conjugation = irregulars[root_verb][mood][tense][pronoun]
            except:
                conjugation = root_verb[:-2] + "aba"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            try:
                conjugation = irregulars[root_verb][mood][tense][pronoun]
            except:
                conjugation = root_verb[:-2] + "ía"
            return conjugation
    if pronoun == "tu":
        if root_verb[-2:] == "ar":
            try:
                conjugation = irregulars[root_verb][mood][tense][pronoun]
            except:
                conjugation = root_verb[:-2] + "abas"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            try:
                conjugation = irregulars[root_verb][mood][tense][pronoun]
            except:
                conjugation = root_verb[:-2] + "ías"
            return conjugation
    if pronoun == "usted":
        if root_verb[-2:] == "ar":
            try:
                conjugation = irregulars[root_verb][mood][tense][pronoun]
            except:
                conjugation = root_verb[:-2] + "aba"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            try:
                conjugation = irregulars[root_verb][mood][tense][pronoun]
            except:
                conjugation = root_verb[:-2] + "ía"
            return conjugation
    if pronoun == "nosotros":
        if root_verb[-2:] == "ar":
            try:
                conjugation = irregulars[root_verb][mood][tense][pronoun]
            except:
                conjugation = root_verb[:-2] + "ábamos"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            try:
                conjugation = irregulars[root_verb][mood][tense][pronoun]
            except:
                conjugation = root_verb[:-2] + "íamos"
            return conjugation
    if pronoun == "vosotros":
        if root_verb[-2:] == "ar":
            try:
                conjugation = irregulars[root_verb][mood][tense][pronoun]
            except:
                conjugation = root_verb[:-2] + "abais"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            try:
                conjugation = irregulars[root_verb][mood][tense][pronoun]
            except:
                conjugation = root_verb[:-2] + "íais"
            return conjugation
    if pronoun == "ustedes":
        if root_verb[-2:] == "ar":
            try:
                conjugation = irregulars[root_verb][mood][tense][pronoun]
            except:
                conjugation = root_verb[:-2] + "aban"
            return conjugation
        if root_verb[-2:] == "er" or "ir":
            try:
                conjugation = irregulars[root_verb][mood][tense][pronoun]
            except:
                conjugation = root_verb[:-2] + "ían"
            return conjugation