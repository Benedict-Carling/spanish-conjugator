# -*- coding: iso-8859-15 -*-
def indicitive_past_perfect(root_verb, pronoun):
    if pronoun == "yo":
        if root_verb[-2:] == "ar":
            try:
                conjugation = irregulars[root_verb][mood][tense][pronoun]
            except:
                conjugation = root_verb[:-2] + "ado"
            return "había " + conjugation
        if root_verb[-2:] == "er" or "ir":
            try:
                conjugation = irregulars[root_verb][mood][tense][pronoun]
            except:
                conjugation = root_verb[:-2] + "ido"
            return "había " + conjugation
    if pronoun == "tu":
        if root_verb[-2:] == "ar":
            try:
                conjugation = irregulars[root_verb][mood][tense][pronoun]
            except:
                conjugation = root_verb[:-2] + "ado"
            return "habías " + conjugation
        if root_verb[-2:] == "er" or "ir":
            try:
                conjugation = irregulars[root_verb][mood][tense][pronoun]
            except:
                conjugation = root_verb[:-2] + "ido"
            return "habías " + conjugation
    if pronoun == "usted":
        if root_verb[-2:] == "ar":
            try:
                conjugation = irregulars[root_verb][mood][tense][pronoun]
            except:
                conjugation = root_verb[:-2] + "ado"
            return "había " + conjugation
        if root_verb[-2:] == "er" or "ir":
            try:
                conjugation = irregulars[root_verb][mood][tense][pronoun]
            except:
                conjugation = root_verb[:-2] + "ido"
            return "había " + conjugation
    if pronoun == "nosotros":
        if root_verb[-2:] == "ar":
            try:
                conjugation = irregulars[root_verb][mood][tense][pronoun]
            except:
                conjugation = root_verb[:-2] + "ado"
            return "habíamos " + conjugation
        if root_verb[-2:] == "er" or "ir":
            try:
                conjugation = irregulars[root_verb][mood][tense][pronoun]
            except:
                conjugation = root_verb[:-2] + "ido"
            return "habíamos " + conjugation
    if pronoun == "vosotros":
        if root_verb[-2:] == "ar":
            try:
                conjugation = irregulars[root_verb][mood][tense][pronoun]
            except:
                conjugation = root_verb[:-2] + "ado"
            return "habíais " + conjugation
        if root_verb[-2:] == "er" or "ir":
            try:
                conjugation = irregulars[root_verb][mood][tense][pronoun]
            except:
                conjugation = root_verb[:-2] + "ido"
            return "habíais " + conjugation
    if pronoun == "ustedes":
        if root_verb[-2:] == "ar":
            try:
                conjugation = irregulars[root_verb][mood][tense][pronoun]
            except:
                conjugation = root_verb[:-2] + "ado"
            return "habían " + conjugation
        if root_verb[-2:] == "er" or "ir":
            try:
                conjugation = irregulars[root_verb][mood][tense][pronoun]
            except:
                conjugation = root_verb[:-2] + "ido"
            return "habían " + conjugation