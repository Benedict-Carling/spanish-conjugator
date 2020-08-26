# -*- coding: iso-8859-15 -*-
from tenses.indicitive.preterite import indicitive_preterite
from tenses.indicitive.present import indicitive_present
from tenses.indicitive.imperfect import indicitive_imperfect
from tenses.indicitive.future import indicitive_future
from tenses.indicitive.present_perfect import indicitive_present_perfect
from tenses.indicitive.past_perfect import indicitive_past_perfect
from tenses.indicitive.past_anterior import indicitive_past_anterior
# ------------------- Irregulars ------------------
from irregulars.irregular_dict import irregulars_dictionary

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
                    conjugation = irregulars_dictionary[root_verb][mood][tense][pronoun]
                except:
                    conjugation = indicitive_present(root_verb, pronoun)
                return conjugation

# ----------------------------------- Imperfect Indicitive ----------------------------------- #

        if tense == "imperfect":
            if mood == "indicitive":
                try:
                    conjugation = irregulars_dictionary[root_verb][mood][tense][pronoun]
                except:
                    conjugation = indicitive_imperfect(root_verb, pronoun)
                return conjugation

# ----------------------------------- Preterite Indicitive ----------------------------------- #
        if tense == "preterite":
            if mood == "indicitive":
                try:
                    conjugation = irregulars_dictionary[root_verb][mood][tense][pronoun]
                except:
                    conjugation = indicitive_preterite(root_verb, pronoun)
                return conjugation

# ----------------------------------- Future Simple Indicitive ----------------------------------- #
        if tense == "future":
            if mood == "indicitive":
                try:
                    conjugation = irregulars_dictionary[root_verb][mood][tense][pronoun]
                except:
                    conjugation = indicitive_future(root_verb, pronoun)
                return conjugation
                
# ----------------------------------- Present Perfect Compound Tense ----------------------------- #
        if tense == "present_perfect":
            if mood == "indicitive":
                try:
                    conjugation = irregulars_dictionary[root_verb][mood][tense][pronoun]
                except:
                    conjugation = indicitive_present_perfect(root_verb, pronoun)
                return conjugation
                
# ----------------------------------- Past Perfect Compound Tense ----------------------------- #

        if tense == "past_perfect":
            if mood == "indicitive":
                try:
                    conjugation = irregulars_dictionary[root_verb][mood][tense][pronoun]
                except:
                    conjugation = indicitive_past_perfect(root_verb, pronoun)
                return conjugation
            
# ----------------------------------- Past Anterior Compound Tense ----------------------------- #

        if tense == "past_anterior":
            if mood == "indicitive":
                try:
                    conjugation = irregulars_dictionary[root_verb][mood][tense][pronoun]
                except:
                    conjugation = indicitive_past_anterior(root_verb, pronoun)
                return conjugation


# ----------------------------------- Catch missed conjugations ------------------------------- #
        return "Error - verb not found"