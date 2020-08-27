# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ----------------------------------- Future Preterite Indicitive ----------------------------------- #

def test_preterite_indicitive_yo_ar():
    expected = "hablé"
    assert Conjugator().conjugate('hablar','preterite','indicitive','yo') == expected

def test_preterite_indicitive_tu_ar():
    expected = "hablaste"
    assert Conjugator().conjugate('hablar','preterite','indicitive','tu') == expected

def test_preterite_indicitive_usted_ar():
    expected = "habló"
    assert Conjugator().conjugate('hablar','preterite','indicitive','usted') == expected

def test_preterite_indicitive_nosotros_ar():
    expected = 'hablamos'
    assert str(Conjugator().conjugate('hablar','preterite','indicitive','nosotros')) == expected

def test_preterite_indicitive_vosotros_ar():
    expected = "hablasteis"
    assert Conjugator().conjugate('hablar','preterite','indicitive','vosotros') == expected

def test_preterite_indicitive_ustedes_ar():
    expected = "hablaron"
    assert Conjugator().conjugate('hablar','preterite','indicitive','ustedes') == expected