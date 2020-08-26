# -*- coding: iso-8859-15 -*-
# ------------------- Irregulars ------------------
irregulars = {
    'ir':{
        'indicitive':{
            'present':{
                'yo':'voy',
                'tu':'vas',
                'usted':'va',
                'nosotros':'vamos',
                'vosotros':'vais',
                'ustedes':'van'
            },
            'imperfect':{
                'yo':'iba',
                'tu':'ibas',
                'usted':'iba',
                'nosotros':'íbamos',
                'vosotros':'ibais',
                'ustedes':'iban'
            },
            'preterite':{
                'yo':'fui',
                'tu':'fuiste',
                'usted':'fue',
                'nosotros':'fuimos',
                'vosotros':'fuisteis',
                'ustedes':'fueron'
            }
        }
    },
    'ser':{
        'indicitive':{
            'present':{
                'yo':'soy',
                'tu':'eres',
                'usted':'es',
                'nosotros':'somos',
                'vosotros':'sois',
                'ustedes':'son'    
            },
            'imperfect':{
                'yo':'era',
                'tu':'eras',
                'usted':'era',
                'nosotros':'éramos',
                'vosotros':'erais',
                'ustedes':'eran'    
            },
            'preterite':{
                'yo':'fui',
                'tu':'fuiste',
                'usted':'fue',
                'nosotros':'fuimos',
                'vosotros':'fuisteis',
                'ustedes':'fueron'
            }
        }
    },
    'ver':{
        'indicitive':{
            'imperfect':{
                'yo':'veía',
                'tu':'veías',
                'usted':'veía',
                'nosotros':'veíamos',
                'vosotros':'veíais',
                'ustedes':'veían'
            }
        }
    },
}

# ----------------- Conjugator

class Conjugator():

    def conjugate(self,root_verb,tense,mood,pronoun):
        tense = tense.lower()
        mood = mood.lower()
        pronoun = pronoun.lower()

# ----------------------------------- Present Indicitive ----------------------------------- #

        if tense == "present":
            if mood == "indicitive":
                if pronoun == "yo":
                    if root_verb[-2:] == "ar":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "o"
                        return conjugation
                    if root_verb[-2:] == "er":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "o"
                        return conjugation
                    if root_verb[-2:] == "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "o"
                        return conjugation
                if pronoun == "tu":
                    if root_verb[-2:] == "ar":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "as"
                        return conjugation
                    if root_verb[-2:] == "er":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "es"
                        return conjugation
                    if root_verb[-2:] == "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "es"
                        return conjugation
                if pronoun == "usted":
                    if root_verb[-2:] == "ar":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "a"
                        return conjugation
                    if root_verb[-2:] == "er":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "e"
                        return conjugation
                    if root_verb[-2:] == "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "e"
                        return conjugation
                if pronoun == "nosotros":
                    if root_verb[-2:] == "ar":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "amos"
                        return conjugation
                    if root_verb[-2:] == "er":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "emos"
                        return conjugation
                    if root_verb[-2:] == "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "imos"
                        return conjugation
                if pronoun == "vosotros":
                    if root_verb[-2:] == "ar":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "áis"
                        return conjugation
                    if root_verb[-2:] == "er":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "éis"
                        return conjugation
                    if root_verb[-2:] == "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "ís"
                        return conjugation
                if pronoun == "ustedes":
                    if root_verb[-2:] == "ar":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "an"
                        return conjugation
                    if root_verb[-2:] == "er":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "en"
                        return conjugation
                    if root_verb[-2:] == "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "en"
                        return conjugation

# ----------------------------------- Imperfect Indicitive ----------------------------------- #

        if tense == "imperfect":
            if mood == "indicitive":
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

# ----------------------------------- Preterite Indicitive ----------------------------------- #
        if tense == "preterite":
            if mood == "indicitive":
                if pronoun == "yo":
                    if root_verb[-2:] == "ar":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "é"
                        return conjugation
                    if root_verb[-2:] == "er" or "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "í"
                        return conjugation
                if pronoun == "tu":
                    if root_verb[-2:] == "ar":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "aste"
                        return conjugation
                    if root_verb[-2:] == "er" or "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "iste"
                        return conjugation
                if pronoun == "usted":
                    if root_verb[-2:] == "ar":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "ó"
                        return conjugation
                    if root_verb[-2:] == "er" or "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "ió"
                        return conjugation
                if pronoun == "nosotros":
                    if root_verb[-2:] == "ar":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "amos"
                        return conjugation
                    if root_verb[-2:] == "er" or "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "imos"
                        return conjugation
                if pronoun == "vosotros":
                    if root_verb[-2:] == "ar":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "asteis"
                        return conjugation
                    if root_verb[-2:] == "er" or "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "isteis"
                        return conjugation
                if pronoun == "ustedes":
                    if root_verb[-2:] == "ar":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "aron"
                        return conjugation
                    if root_verb[-2:] == "er" or "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "ieron"
                        return conjugation

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
        
# ----------------------------------- imperfect Simple Indicitive ----------------------------------- #

        if tense == "imperfect":
            if mood == "indicitive":
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

# ----------------------------------- Present Perfect Compound Tense ----------------------------- #

        if tense == "present_perfect":
            if mood == "indicitive":
                if pronoun == "yo":
                    if root_verb[-2:] == "ar":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "ado"
                        return "he " + conjugation
                    if root_verb[-2:] == "er" or "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "ido"
                        return "he " + conjugation
                if pronoun == "tu":
                    if root_verb[-2:] == "ar":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "ado"
                        return "has " + conjugation
                    if root_verb[-2:] == "er" or "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "ido"
                        return "has " + conjugation
                if pronoun == "usted":
                    if root_verb[-2:] == "ar":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "ado"
                        return "ha " + conjugation
                    if root_verb[-2:] == "er" or "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "ido"
                        return "ha " + conjugation
                if pronoun == "nosotros":
                    if root_verb[-2:] == "ar":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "ado"
                        return "hemos " + conjugation
                    if root_verb[-2:] == "er" or "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "ido"
                        return "hemos " + conjugation
                if pronoun == "vosotros":
                    if root_verb[-2:] == "ar":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "ado"
                        return "habéis " + conjugation
                    if root_verb[-2:] == "er" or "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "ido"
                        return "habéis " + conjugation
                if pronoun == "ustedes":
                    if root_verb[-2:] == "ar":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "ado"
                        return "han " + conjugation
                    if root_verb[-2:] == "er" or "ir":
                        try:
                            conjugation = irregulars[root_verb][mood][tense][pronoun]
                        except:
                            conjugation = root_verb[:-2] + "ido"
                        return "han " + conjugation
        
# ----------------------------------- Past Perfect Compound Tense ----------------------------- #

        if tense == "past_perfect":
            if mood == "indicitive":
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
        
        

        return conjugation
        