# -*- coding: iso-8859-15 -*-
from tenses.indicitive.preterite import indicitive_preterite
from tenses.indicitive.present import indicitive_present
from tenses.indicitive.imperfect import indicitive_imperfect
# ------------------- Irregulars ------------------
from irregulars import irregulars

# ----------------- Conjugator --------------------

class Conjugator():

    def conjugate(self,root_verb,tense,mood,pronoun):
        tense = tense.lower()
        mood = mood.lower()
        pronoun = pronoun.lower()

# ----------------------------------- Present Indicitive ----------------------------------- #

        if tense == "present":
            if mood == "indicitive":
                try:
                    conjugation = irregulars[root_verb][mood][tense][pronoun]
                except:
                    conjugation = indicitive_present(root_verb, pronoun)

# ----------------------------------- Imperfect Indicitive ----------------------------------- #

        if tense == "imperfect":
            if mood == "indicitive":
                try:
                    conjugation = irregulars[root_verb][mood][tense][pronoun]
                except:
                    conjugation = indicitive_imperfect(root_verb, pronoun)

# ----------------------------------- Preterite Indicitive ----------------------------------- #
        if tense == "preterite":
            if mood == "indicitive":
                try:
                    conjugation = irregulars[root_verb][mood][tense][pronoun]
                except:
                    conjugation = indicitive_preterite(root_verb, pronoun)

# ----------------------------------- Future Simple Indicitive ----------------------------------- #
        if tense == "future":
            if mood == "indicitive":
                if pronoun == "yo":
                    if root_verb[-2:] == "ar" or "er" or "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb + "é"
                        return conjugation
                if pronoun == "tu":
                    if root_verb[-2:] == "ar" or "er" or "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb + "ás"
                        return conjugation
                if pronoun == "usted":
                    if root_verb[-2:] == "ar" or "er" or "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb + "á"
                        return conjugation
                if pronoun == "nosotros":
                    if root_verb[-2:] == "ar" or "er" or "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb + "emos"
                        return conjugation
                if pronoun == "vosotros":
                    if root_verb[-2:] == "ar" or "er" or "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb + "éis"
                        return conjugation
                if pronoun == "ustedes":
                    if root_verb[-2:] == "ar" or "er" or "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb + "án"
                        return conjugation
        return conjugation