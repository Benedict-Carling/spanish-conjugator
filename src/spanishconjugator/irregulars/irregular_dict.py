# -*- coding: iso-8859-15 -*-
haber_present = ["he", "has", "ha", "hemos", "habéis", "han"]
haber_past = ["había", "habías", "había", "habíamos", "habíais", "habían"]
participle = {
    'past': {
        'ir': "ido",
        "ver": "visto",
        "leer": "leído",
        "volver": "vuelto",
        "escribir": "escrito",
        "decir": "dicho"
    }
}
SPACE = " "
irregulars_dictionary = {
    'ir':{
        'indicative':{
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
            }, 
            'present_perfect' : {
                'yo':haber_present[0] + SPACE + participle["past"]["ir"],
                'tu':haber_present[1] + SPACE + participle["past"]["ir"],
                'usted':haber_present[2] + SPACE + participle["past"]["ir"],
                'nosotros':haber_present[3] + SPACE + participle["past"]["ir"],
                'vosotros':haber_present[4] + SPACE + participle["past"]["ir"],
                'ustedes':haber_present[5] + SPACE + participle["past"]["ir"]
            },
            'past_perfect' : {
                'yo':haber_past[0] + SPACE + participle["past"]["ir"],
                'tu':haber_past[1] + SPACE + participle["past"]["ir"],
                'usted':haber_past[2] + SPACE + participle["past"]["ir"],
                'nosotros':haber_past[3] + SPACE + participle["past"]["ir"],
                'vosotros':haber_past[4] + SPACE + participle["past"]["ir"],
                'ustedes':haber_past[5] + SPACE + participle["past"]["ir"]
            }
        }
    },
    'ser':{
        'indicative':{
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
        'indicative':{
            'present':{
                'yo':'veo',
                'tu':'ves',
                'usted':'ve',
                'nosotros':'vemos',
                'vosotros':'veis',
                'ustedes':'ven'
            },
            'imperfect':{
                'yo':'veía',
                'tu':'veías',
                'usted':'veía',
                'nosotros':'veíamos',
                'vosotros':'veíais',
                'ustedes':'veían'
            },
            'preterite':{
                'yo':'vi',
                'tu':'viste',
                'usted':'vio',
                'nosotros':'vimos',
                'vosotros':'visteis',
                'ustedes':'vieron'
            },
            'present_perfect' : {
                'yo':haber_present[0] + SPACE + participle["past"]["ver"],
                'tu':haber_present[1] + SPACE + participle["past"]["ver"],
                'usted':haber_present[2] + SPACE + participle["past"]["ver"],
                'nosotros':haber_present[3] + SPACE + participle["past"]["ver"],
                'vosotros':haber_present[4] + SPACE + participle["past"]["ver"],
                'ustedes':haber_present[5] + SPACE + participle["past"]["ver"]
            },
             'past_perfect' : {
                'yo':haber_past[0] + SPACE + participle["past"]["ver"],
                'tu':haber_past[1] + SPACE + participle["past"]["ver"],
                'usted':haber_past[2] + SPACE + participle["past"]["ver"],
                'nosotros':haber_past[3] + SPACE + participle["past"]["ver"],
                'vosotros':haber_past[4] + SPACE + participle["past"]["ver"],
                'ustedes':haber_past[5] + SPACE + participle["past"]["ver"]
            }
        }
    },
    'estar':{
        'indicative':{
            'present':{
                'yo':'estoy',
                'tu':'estás',
                'usted':'está',
                'ustedes':'están'
            },
            'preterite':{
                'yo':'estuve',
                'tu':'estuviste',
                'usted':'estuvo',
                'nosotros':'estuvimos',
                'vosotros':'estuvisteis',
                'ustedes':'estuvieron'
            }
        }
    },
    'venir':{
        'indicative':{
            'present':{
                'yo':'vengo',
                'tu':'vienes',
                'usted':'viene',
                'ustedes':'vienen'
            },
            'preterite':{
                'yo':'vine',
                'tu':'viniste',
                'usted':'vino',
                'nosotros':'vinimos',
                'vosotros':'vinisteis',
                'ustedes':'vinieron'
            }
        }
    },
    'volver':{
        'indicative':{
            'present':{
                'yo':'vuelvo',
                'tu':'vuelves',
                'usted':'vuelve',
                'ustedes':'vuelven'
            },
            'present_perfect' : {
                'yo':haber_present[0] + SPACE + participle["past"]["volver"],
                'tu':haber_present[1] + SPACE + participle["past"]["volver"],
                'usted':haber_present[2] + SPACE + participle["past"]["volver"],
                'nosotros':haber_present[3] + SPACE + participle["past"]["volver"],
                'vosotros':haber_present[4] + SPACE + participle["past"]["volver"],
                'ustedes':haber_present[5] + SPACE + participle["past"]["volver"]
            },
             'past_perfect' : {
                'yo':haber_past[0] + SPACE + participle["past"]["volver"],
                'tu':haber_past[1] + SPACE + participle["past"]["volver"],
                'usted':haber_past[2] + SPACE + participle["past"]["volver"],
                'nosotros':haber_past[3] + SPACE + participle["past"]["volver"],
                'vosotros':haber_past[4] + SPACE + participle["past"]["volver"],
                'ustedes':haber_past[5] + SPACE + participle["past"]["volver"]
            }
        }
    },
    'tener':{
        'indicative':{
            'present':{
                'yo':'tengo',
                'tu':'tienes',
                'usted':'tiene',
                'ustedes':'tienen'
            },
            'preterite':{
                'yo':'tuve',
                'tu':'tuviste',
                'usted':'tuvo',
                'nosotros':'tuvimos',
                'vosotros':'tuvisteis',
                'ustedes':'tuvieron'
            },
            'future':{
                'yo':'tendré',
                'tu':'tendrás',
                'usted':'tendrá',
                'nosotros':'tendremos',
                'vosotros':'tendréis',
                'ustedes':'tendrán'
            }
        },
        'conditional':{
            'simple_conditional':{
                'yo':'tendría',
                'tu':'tendrías',
                'usted':'tendría',
                'nosotros':'tendríamos',
                'vosotros':'tendríais',
                'ustedes':'tendrían'
            }
        }
    },
    'saber':{
        'indicative':{
            'present':{
                'yo':'sé'
            },
            'preterite':{
                'yo':'supe',
                'tu':'supiste',
                'usted':'supo',
                'nosotros':'supimos',
                'vosotros':'supisteis',
                'ustedes':'supieron'
            }
        }
    },
    'poder':{
        'indicative':{
            'present':{
                'yo':'puedo',
                'tu':'puedes',
                'usted':'puede',
                'ustedes':'pueden',
            },
            'preterite':{
                'yo':'pude',
                'tu':'pudiste',
                'usted':'pudo',
                'nosotros':'pudimos',
                'vosotros':'pudisteis',
                'ustedes':'pudieron'
            }
        },
        'conditional':{
            'simple_conditional':{
                'yo':'podría',
                'tu':'podrías',
                'usted':'podría',
                'ustedes':'podrían',
                'nosotros': 'podríamos',
                'vosotros': 'podríais'
            },
        }
    },
    'pedir':{
        'indicative':{
            'present':{
                'yo':'pido',
                'tu':'pides',
                'usted':'pide',
                'ustedes':'piden'
            }
        }
    },
    'querer':{
        'indicative':{
            'present':{
                'yo':'quiero',
                'tu':'quieres',
                'usted':'quiere',
                'ustedes':'quieren'
            },
            'preterite':{
                'yo':'quise',
                'tu':'quisiste',
                'usted':'quiso',
                'nosotros':'quisimos',
                'vosotros':'quisisteis',
                'ustedes':'quisieron'
            }
        }
    },
    'practicar':{
        'indicative':{
            'preterite':{
                'yo':'practiqué'
            }
        }
    },
    'leer': {
        'indicative': {
             'present_perfect' : {
                'yo':haber_present[0] + SPACE + participle["past"]["leer"],
                'tu':haber_present[1] + SPACE + participle["past"]["leer"],
                'usted':haber_present[2] + SPACE + participle["past"]["leer"],
                'nosotros':haber_present[3] + SPACE + participle["past"]["leer"],
                'vosotros':haber_present[4] + SPACE + participle["past"]["leer"],
                'ustedes':haber_present[5] + SPACE + participle["past"]["leer"]
            },
             'past_perfect' : {
                'yo':haber_past[0] + SPACE + participle["past"]["leer"],
                'tu':haber_past[1] + SPACE + participle["past"]["leer"],
                'usted':haber_past[2] + SPACE + participle["past"]["leer"],
                'nosotros':haber_past[3] + SPACE + participle["past"]["leer"],
                'vosotros':haber_past[4] + SPACE + participle["past"]["leer"],
                'ustedes':haber_past[5] + SPACE + participle["past"]["leer"]
            }
        }
    },
    "escribir": {
        "indicative": {
            'present_perfect' : {
                'yo':haber_present[0] + SPACE + participle["past"]["escribir"],
                'tu':haber_present[1] + SPACE + participle["past"]["escribir"],
                'usted':haber_present[2] + SPACE + participle["past"]["escribir"],
                'nosotros':haber_present[3] + SPACE + participle["past"]["escribir"],
                'vosotros':haber_present[4] + SPACE + participle["past"]["escribir"],
                'ustedes':haber_present[5] + SPACE + participle["past"]["escribir"]
            },
             'past_perfect' : {
                'yo':haber_past[0] + SPACE + participle["past"]["escribir"],
                'tu':haber_past[1] + SPACE + participle["past"]["escribir"],
                'usted':haber_past[2] + SPACE + participle["past"]["escribir"],
                'nosotros':haber_past[3] + SPACE + participle["past"]["escribir"],
                'vosotros':haber_past[4] + SPACE + participle["past"]["escribir"],
                'ustedes':haber_past[5] + SPACE + participle["past"]["escribir"]
            }
        }
        
    },
    "decir": {
        "indicative": {
            'present': {
                'yo': "digo",
                'tu': "dices",
                'usted': "dice",
                'ustedes': "dicen"
            },
            'preterite': {
                'yo': "dije",
                'tu': "dijiste",
                'usted': "dijo",
                'nosotros': "dijimos",
                'ustedes': "dijeron"
            },
            'present_perfect' : {
                'yo':haber_present[0] + SPACE + participle["past"]["decir"],
                'tu':haber_present[1] + SPACE + participle["past"]["decir"],
                'usted':haber_present[2] + SPACE + participle["past"]["decir"],
                'nosotros':haber_present[3] + SPACE + participle["past"]["decir"],
                'vosotros':haber_present[4] + SPACE + participle["past"]["decir"],
                'ustedes':haber_present[5] + SPACE + participle["past"]["decir"]
            },
             'past_perfect' : {
                'yo':haber_past[0] + SPACE + participle["past"]["decir"],
                'tu':haber_past[1] + SPACE + participle["past"]["decir"],
                'usted':haber_past[2] + SPACE + participle["past"]["decir"],
                'nosotros':haber_past[3] + SPACE + participle["past"]["decir"],
                'vosotros':haber_past[4] + SPACE + participle["past"]["decir"],
                'ustedes':haber_past[5] + SPACE + participle["past"]["decir"]
            }
        },
        'conditional':{
            'simple_conditional':{
                'yo':'diría',
                'tu':'dirías',
                'usted':'diría',
                'ustedes':'dirían',
                'nosotros': 'diríamos',
                'vosotros': 'diríais'
            },
        }
        
    },
    "caer":{
        "indicative": {
            "preterite": {
                "tu": "caíste",
                "usted": "cayó",
                "nosotros": "caímos",
                "vosotros": "caísteis",
                "ustedes": "cayeron"
            },
            "present": {
                "yo": "caigo"
            }
        }
    }, 
    "apagar": {
        "indicative": {
            "preterite": {
                "yo": "apagué"
            }
        }
    },
    "cerrar": {
        "indicative": {
            "present": {
                "yo": "cierro",
                "tu": "cierras",
                "usted": "cierra",
                "ustedes": "cierran"
            }
        }
    },
     "haber": {
        "indicative": {
            "present": {
                'yo':haber_present[0],
                'tu':haber_present[1],
                'usted':haber_present[2],
                'nosotros':haber_present[3],
                'vosotros':haber_present[4],
                'ustedes':haber_present[5]
            },
            "preterite": {
                'yo':"hube",
                'tu':"hubiste",
                'usted':"hubo",
                'nosotros':"hubimos",
                'vosotros':"hubisteis",
                'ustedes':"hubieron"
            }
        }
    },
    "salir": {
        "indicative": {
            "present": {
                'yo':"salgo",
            }
        }
    },
    'hacer':{
        'indicative':{
            'present':{
                'yo':'hago'
            },
            'preterite':{
                'yo':'hice',
                'tu':'hiciste',
                'usted':'hizo',
                'nosotros':'hicimos',
                'vosotros':'hicisteis',
                'ustedes':'hicieron'
            }, 
            'future' : {
                'yo':'haré',
                'tu':'harás',
                'usted':'hará',
                'nosotros':'haremos',
                'vosotros':'haréis',
                'ustedes':'harán'
            }
        }
    },
    "probar": {
        "indicative": {
            "present": {
                "yo": "pruebo",
                "tu": "pruebas",
                "usted": "prueba",
                "ustedes": "prueban"
            }
        }
    },
    "pensar": {
        "indicative": {
            "present": {
                "yo": "pienso",
                "tu": "piensas",
                "usted": "piensa",
                "ustedes": "piensan"
            }
        }
    },
    "encontrar": {
        "indicative": {
            "present": {
                "yo": "encuentro",
                "tu": "encuentras",
                "usted": "encuentra",
                "ustedes": "encuentran"
            }
        }
    },

}