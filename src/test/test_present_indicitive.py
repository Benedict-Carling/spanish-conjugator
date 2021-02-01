# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ----------------------------------- Present Indicative ----------------------------------- #

def test_present_indicative_yo_ar():
    expected = "hablo"
    assert Conjugator().conjugate('hablar','present','indicative','yo') == expected

def test_present_indicative_tu_ar():
    expected = "hablas"
    assert Conjugator().conjugate('hablar','present','indicative','tu') == expected

def test_present_indicative_usted_ar():
    expected = "habla"
    assert Conjugator().conjugate('hablar','present','indicative','usted') == expected

def test_present_indicative_nosotros_ar():
    expected = 'hablamos'
    assert str(Conjugator().conjugate('hablar','present','indicative','nosotros')) == expected

def test_present_indicative_vosotros_ar():
    expected = "habláis"
    assert Conjugator().conjugate('hablar','present','indicative','vosotros') == expected

def test_present_indicative_ustedes_ar():
    expected = "hablan"
    assert Conjugator().conjugate('hablar','present','indicative','ustedes') == expected
