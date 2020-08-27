# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ----------------------------------- Present Indicitive ----------------------------------- #

def test_present_indicitive_yo_ar():
    expected = "hablo"
    assert Conjugator().conjugate('hablar','present','indicitive','yo') == expected

def test_present_indicitive_tu_ar():
    expected = "hablas"
    assert Conjugator().conjugate('hablar','present','indicitive','tu') == expected

def test_present_indicitive_usted_ar():
    expected = "habla"
    assert Conjugator().conjugate('hablar','present','indicitive','usted') == expected

def test_present_indicitive_nosotros_ar():
    expected = 'hablamos'
    assert str(Conjugator().conjugate('hablar','present','indicitive','nosotros')) == expected

def test_present_indicitive_vosotros_ar():
    expected = "habláis"
    assert Conjugator().conjugate('hablar','present','indicitive','vosotros') == expected

def test_present_indicitive_ustedes_ar():
    expected = "hablan"
    assert Conjugator().conjugate('hablar','present','indicitive','ustedes') == expected
