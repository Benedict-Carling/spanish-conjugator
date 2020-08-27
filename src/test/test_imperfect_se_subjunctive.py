# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ----------------------------------- Present Indicitive ----------------------------------- #

def test_imperfect_se_subjunctive_yo_ar():
    expected = "hablase"
    assert Conjugator().conjugate('hablar','imperfect_se','subjunctive','yo') == expected

def test_imperfect_se_subjunctive_tu_ar():
    expected = "hablases"
    assert Conjugator().conjugate('hablar','imperfect_se','subjunctive','tu') == expected

def test_imperfect_se_subjunctive_usted_ar():
    expected = "hablase"
    assert Conjugator().conjugate('hablar','imperfect_se','subjunctive','usted') == expected

def test_imperfect_se_subjunctive_nosotros_ar():
    expected = 'hablásemos'
    assert str(Conjugator().conjugate('hablar','imperfect_se','subjunctive','nosotros')) == expected

def test_imperfect_se_subjunctive_vosotros_ar():
    expected = "hablaseis"
    assert Conjugator().conjugate('hablar','imperfect_se','subjunctive','vosotros') == expected

def test_imperfect_se_subjunctive_ustedes_ar():
    expected = "hablasen"
    assert Conjugator().conjugate('hablar','imperfect_se','subjunctive','ustedes') == expected