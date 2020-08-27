# -*- coding: iso-8859-15 -*-

# --------------------------------- Importing Tenses From Files ---------------------------- #
from spanishconjugator.tenses.indicitive.preterite            import indicitive_preterite
from spanishconjugator.tenses.indicitive.present              import indicitive_present
from spanishconjugator.tenses.indicitive.imperfect            import indicitive_imperfect
from spanishconjugator.tenses.indicitive.future               import indicitive_future
from spanishconjugator.tenses.indicitive.present_perfect      import indicitive_present_perfect
from spanishconjugator.tenses.indicitive.past_perfect         import indicitive_past_perfect
from spanishconjugator.tenses.indicitive.past_anterior        import indicitive_past_anterior
from spanishconjugator.tenses.indicitive.future_perfect       import indicitive_future_perfect

from spanishconjugator.tenses.conditional.simple_conditional  import conditional_simple_conditional

# --------------------------------- Irregulars --------------------------------------------- #
from spanishconjugator.irregulars.irregular_dict              import irregulars_dictionary

# --------------------------------- Conjugator --------------------------------------------- #

class Conjugator():

    def conjugate(self,root_verb,tense,mood,pronoun):
        tense = tense.lower()
        mood = mood.lower()
        pronoun = pronoun.lower()

        try: 
            conjugation = irregulars_dictionary[root_verb][mood][tense][pronoun]
            return conjugation

        except:

# --------------------------------- The Indicatives ---------------------------------------- #

# --------------------------------- Present Indicitive ------------------------------------- #

            if tense == "present":
                if mood == "indicitive":
                    conjugation = indicitive_present(root_verb, pronoun)
                    return conjugation

# --------------------------------- Imperfect Indicitive ----------------------------------- #

            if tense == "imperfect":
                if mood == "indicitive":
                    conjugation = indicitive_imperfect(root_verb, pronoun)
                    return conjugation

# --------------------------------- Preterite Indicitive ----------------------------------- #
            
            if tense == "preterite":
                if mood == "indicitive":
                    conjugation = indicitive_preterite(root_verb, pronoun)
                    return conjugation

# --------------------------------- Future Simple Indicitive ------------------------------- #
            
            if tense == "future":
                if mood == "indicitive":
                    conjugation = indicitive_future(root_verb, pronoun)
                    return conjugation
                    
# --------------------------------- Present Perfect Compound Tense -------------------------- #
            
            if tense == "present_perfect":
                if mood == "indicitive":
                    conjugation = indicitive_present_perfect(root_verb, pronoun)
                    return conjugation
                    
# --------------------------------- Past Perfect Compound Tense ----------------------------- #

            if tense == "past_perfect":
                if mood == "indicitive":
                    conjugation = indicitive_past_perfect(root_verb, pronoun)
                    return conjugation
                
# --------------------------------- Past Anterior Compound Tense ---------------------------- #

            if tense == "past_anterior":
                if mood == "indicitive":
                    conjugation = indicitive_past_anterior(root_verb, pronoun)
                    return conjugation

# --------------------------------- Future Perfect Compound Tense --------------------------- #

            if tense == "future_perfect":
                if mood == "indicitive":
                    conjugation = indicitive_future_perfect(root_verb, pronoun)
                    return conjugation


# --------------------------------- The Conditional ----------------------------------------- #

#---------------------------------- Simple Conditional -------------------------------------- #

            if tense == "simple_conditional":
                if mood == "conditional":
                    conjugation = conditional_simple_conditional(root_verb, pronoun)
                    return conjugation


# --------------------------------- Catch Missed Conjugations ------------------------------- #

        return "Error - verb not found"