# -*- coding: iso-8859-15 -*-

# --------------------------------- Importing Tenses From Files ---------------------------- #
from spanishconjugator.tenses.indicative.preterite import indicative_preterite
from spanishconjugator.tenses.indicative.present import indicative_present
from spanishconjugator.tenses.indicative.imperfect import indicative_imperfect
from spanishconjugator.tenses.indicative.future import indicative_future
from spanishconjugator.tenses.indicative.present_perfect import (
    indicative_present_perfect,
)
from spanishconjugator.tenses.indicative.past_perfect import indicative_past_perfect
from spanishconjugator.tenses.indicative.past_anterior import indicative_past_anterior
from spanishconjugator.tenses.indicative.future_perfect import indicative_future_perfect

from spanishconjugator.tenses.conditional.simple_conditional import (
    conditional_simple_conditional,
)
from spanishconjugator.tenses.conditional.perfect import conditional_perfect

from spanishconjugator.tenses.imperative.affirmative import affirmative
from spanishconjugator.tenses.imperative.negative import negative

from spanishconjugator.tenses.subjunctive.present import subjunctive_present
from spanishconjugator.tenses.subjunctive.present_perfect import (
    subjunctive_present_perfect,
)
from spanishconjugator.tenses.subjunctive.pluperfect import subjunctive_pluperfect
from spanishconjugator.tenses.subjunctive.future_perfect import (
    subjunctive_future_perfect,
)
from spanishconjugator.tenses.subjunctive.imperfect import subjunctive_imperfect
from spanishconjugator.tenses.subjunctive.imperfect_se import subjunctive_imperfect_se
from spanishconjugator.tenses.subjunctive.future import subjunctive_future

# --------------------------------- Irregulars --------------------------------------------- #
from spanishconjugator.irregulars.irregular_dict import irregulars_dictionary

# --------------------------------- Conjugator --------------------------------------------- #


class Conjugator:
    def conjugate(self, root_verb, tense, mood, pronoun=None):
        tense = tense.lower()
        mood = mood.lower()
        try:
            if pronoun:
                pronoun = pronoun.lower()

                try:
                    conjugation = irregulars_dictionary[root_verb][mood][tense][pronoun]
                    return conjugation
                except:
                    # root_verb does not have an irregular conjugation with the given pronoun
                    return self.conjugate_tense_mood(root_verb, tense, mood, pronoun)
            else:
                # in case no pronoun is passed
              return self.conjugate_tense_mood(root_verb, tense, mood, None)     

        except:
            # --------------------------------- Catch Missed Conjugations ------------------------------- #
            return "Error - verb not found"
                

    def conjugate_tense_mood(self, root_verb, tense, mood, pronoun=None):
        # --------------------------------- The Indicatives ---------------------------------------- #

        # --------------------------------- Present Indicative ------------------------------------- #
                    if tense == "present":
                        if mood == "indicative":
                            conjugation = indicative_present(root_verb, pronoun)
                            return conjugation

        # --------------------------------- Imperfect Indicative ----------------------------------- #

                    if tense == "imperfect":
                        if mood == "indicative":
                            conjugation = indicative_imperfect(root_verb, pronoun)
                            return conjugation

        # --------------------------------- Preterite Indicative ----------------------------------- #
                    
                    if tense == "preterite":
                        if mood == "indicative":
                            conjugation = indicative_preterite(root_verb, pronoun)
                            return conjugation

        # --------------------------------- Future Simple Indicative ------------------------------- #
                    
                    if tense == "future":
                        if mood == "indicative":
                            conjugation = indicative_future(root_verb, pronoun)
                            return conjugation
                            
        # --------------------------------- Present Perfect Compound Tense -------------------------- #
                    
                    if tense == "present_perfect":
                        if mood == "indicative":
                            conjugation = indicative_present_perfect(root_verb, pronoun)
                            return conjugation
                            
        # --------------------------------- Past Perfect Compound Tense ----------------------------- #

                    if tense == "past_perfect":
                        if mood == "indicative":
                            conjugation = indicative_past_perfect(root_verb, pronoun)
                            return conjugation
                        
        # --------------------------------- Past Anterior Compound Tense ---------------------------- #

                    if tense == "past_anterior":
                        if mood == "indicative":
                            conjugation = indicative_past_anterior(root_verb, pronoun)
                            return conjugation

        # --------------------------------- Future Perfect Compound Tense --------------------------- #

                    if tense == "future_perfect":
                        if mood == "indicative":
                            conjugation = indicative_future_perfect(root_verb, pronoun)
                            return conjugation


        # --------------------------------- The Conditional ----------------------------------------- #

        #---------------------------------- Simple Conditional -------------------------------------- #

                    if tense == "simple_conditional":
                        if mood == "conditional":
                            conjugation = conditional_simple_conditional(root_verb, pronoun)
                            return conjugation

        #---------------------------------- Perfect Conditional -------------------------------------- #

                    if tense == "perfect":
                        if mood == "conditional":
                            conjugation = conditional_perfect(root_verb, pronoun)
                            return conjugation

        # --------------------------------- The Imperative ----------------------------------------- #

        #---------------------------------- Affirmative Imperative -------------------------------------- #

                    if tense == "affirmative":
                        if mood == "imperative":
                            conjugation = affirmative(root_verb, pronoun)
                            return conjugation

        #---------------------------------- Negative Imperative -------------------------------------- #

                    if tense == "negative":
                        if mood == "imperative":
                            conjugation = negative(root_verb, pronoun)
                            return conjugation

        # --------------------------------- The Subjunctive ----------------------------------------- #

        #---------------------------------- Present Subjunctive ------------------------------------- #

                    if tense == "present":
                        if mood == "subjunctive":
                            conjugation = subjunctive_present(root_verb, pronoun)
                            return conjugation

        #---------------------------------- Present Perfect Subjunctive ----------------------------- #

                    if tense == "present_perfect":
                        if mood == "subjunctive":
                            conjugation = subjunctive_present_perfect(root_verb, pronoun)
                            return conjugation

        #---------------------------------- Pluperfect Subjunctive ---------------------------------- #

                    if tense == "pluperfect":
                        if mood == "subjunctive":
                            conjugation = subjunctive_pluperfect(root_verb, pronoun)
                            return conjugation

        #---------------------------------- Future Perfect Subjunctive ------------------------------ #

                    if tense == "future_perfect":
                        if mood == "subjunctive":
                            conjugation = subjunctive_future_perfect(root_verb, pronoun)
                            return conjugation

        #---------------------------------- Imperfect Subjunctive -------------------------------------- #

                    if tense == "imperfect":
                        if mood == "subjunctive":
                            conjugation = subjunctive_imperfect(root_verb, pronoun)
                            return conjugation

        #---------------------------------- imperfect se Subjunctive -------------------------------------- #

                    if tense == "imperfect_se":
                        if mood == "subjunctive":
                            conjugation = subjunctive_imperfect_se(root_verb, pronoun)
                            return conjugation

        #---------------------------------- Future Subjunctive -------------------------------------- #

                    if tense == "future":
                        if mood == "subjunctive":
                            conjugation = subjunctive_future(root_verb, pronoun)
                            return conjugation