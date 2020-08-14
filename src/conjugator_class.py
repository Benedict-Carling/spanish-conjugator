# -*- coding: iso-8859-15 -*-
class Spanish_conjugator():

    # Present Conjugations

    # Past Conjugations

    def conjugate(self,root_verb,tense,mood,pronoun):
        tense = tense.lower()
        mood = mood.lower()
        pronoun = pronoun.lower()

        if tense == "imperfect":
            if mood == "imperitive":
                if pronoun == "yo":
                    if root_verb[-2:] == "ar":
                        conjugation = root_verb[:-2] + "aba"
                        return conjugation
                    if root_verb[-2:] == "er" or "ir":
                        conjugation = root_verb[:-2] + "ía"
                        return conjugation

        return conjugation

    # Future Conjugations

# Example test to run -- later to be turned into unit tests
#conjugator = Spanish_conjugator()
print(Spanish_conjugator().conjugate('hablar','imperfect','imperitive','yo'))
print(Spanish_conjugator().conjugate('charlar','imperfect','imperitive','yo'))
print(Spanish_conjugator().conjugate('comer','imperfect','imperitive','yo'))