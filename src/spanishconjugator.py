# -*- coding: iso-8859-15 -*-
from irregulars import irregulars
class Conjugator():


    def conjugate(self,root_verb,tense,mood,pronoun):
        tense = tense.lower()
        mood = mood.lower()
        pronoun = pronoun.lower()

        if tense == "imperfect":
            if mood == "imperitive":
                if pronoun == "yo":
                    if root_verb[-2:] == "ar":
                        try:
                            conjugation = irregulars[root_verb][index][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "aba"
                        return conjugation
                    if root_verb[-2:] == "er" or "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "ía"
                        return conjugation

        return conjugation

# Example test to run -- later to be turned into unit tests
#conjugator = Spanish_conjugator()
print(Conjugator().conjugate('hablar','imperfect','imperitive','yo'))
print(Conjugator().conjugate('charlar','imperfect','imperitive','yo'))
print(Conjugator().conjugate('ver','imperfect','imperitive','yo'))