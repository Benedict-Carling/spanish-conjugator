# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ------------------------------ Present Perfect Compound Tense ------------------------------- #

def test_present_perfect_indicitive_yo_ar():
    expected = "he hablado"
    assert Conjugator().conjugate('hablar','present_perfect','indicitive','yo') == expected

def test_present_perfect_indicitive_tu_ar():
    expected = "has hablado"
    assert Conjugator().conjugate('hablar','present_perfect','indicitive','tu') == expected

def test_present_perfect_indicitive_usted_ar():
    expected = "ha hablado"
    assert Conjugator().conjugate('hablar','present_perfect','indicitive','usted') == expected

def test_present_perfect_indicitive_nosotros_ar():
    expected = "hemos hablado"
    assert Conjugator().conjugate('hablar','present_perfect','indicitive','nosotros') == expected

def test_present_perfect_indicitive_vosotros_ar():
    expected = "habéis hablado"
    assert Conjugator().conjugate('hablar','present_perfect','indicitive','vosotros') == expected

def test_present_perfect_indicitive_ustedes_ar():
    expected = "han hablado"
    assert Conjugator().conjugate('hablar','present_perfect','indicitive','ustedes') == expected

def test_present_perfect_indicitive_yo_er():
    expected = "he bebido"
    assert Conjugator().conjugate('beber','present_perfect','indicitive','yo') == expected

def test_present_perfect_indicitive_tu_ir():
    expected = "has vivido"
    assert Conjugator().conjugate('vivir','present_perfect','indicitive','tu') == expected

def test_present_perfect_indicitive_usted_er():
    expected = "ha bebido"
    assert Conjugator().conjugate('beber','present_perfect','indicitive','usted') == expected

def test_present_perfect_indicitive_nosotros_ir():
    expected = "hemos vivido"
    assert Conjugator().conjugate('vivir','present_perfect','indicitive','nosotros') == expected

def test_present_perfect_indicitive_vosotros_er():
    expected = "habéis bebido"
    assert Conjugator().conjugate('beber','present_perfect','indicitive','vosotros') == expected

def test_present_perfect_indicitive_ustedes_ir():
    expected = "han vivido"
    assert Conjugator().conjugate('vivir','present_perfect','indicitive','ustedes') == expected