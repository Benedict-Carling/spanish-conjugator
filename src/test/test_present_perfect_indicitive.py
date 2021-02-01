# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ------------------------------ Present Perfect Compound Tense ------------------------------- #

def test_present_perfect_indicative_yo_ar():
    expected = "he hablado"
    assert Conjugator().conjugate('hablar','present_perfect','indicative','yo') == expected

def test_present_perfect_indicative_tu_ar():
    expected = "has hablado"
    assert Conjugator().conjugate('hablar','present_perfect','indicative','tu') == expected

def test_present_perfect_indicative_usted_ar():
    expected = "ha hablado"
    assert Conjugator().conjugate('hablar','present_perfect','indicative','usted') == expected

def test_present_perfect_indicative_nosotros_ar():
    expected = "hemos hablado"
    assert Conjugator().conjugate('hablar','present_perfect','indicative','nosotros') == expected

def test_present_perfect_indicative_vosotros_ar():
    expected = "habéis hablado"
    assert Conjugator().conjugate('hablar','present_perfect','indicative','vosotros') == expected

def test_present_perfect_indicative_ustedes_ar():
    expected = "han hablado"
    assert Conjugator().conjugate('hablar','present_perfect','indicative','ustedes') == expected

def test_present_perfect_indicative_yo_er():
    expected = "he bebido"
    assert Conjugator().conjugate('beber','present_perfect','indicative','yo') == expected

def test_present_perfect_indicative_tu_ir():
    expected = "has vivido"
    assert Conjugator().conjugate('vivir','present_perfect','indicative','tu') == expected

def test_present_perfect_indicative_usted_er():
    expected = "ha bebido"
    assert Conjugator().conjugate('beber','present_perfect','indicative','usted') == expected

def test_present_perfect_indicative_nosotros_ir():
    expected = "hemos vivido"
    assert Conjugator().conjugate('vivir','present_perfect','indicative','nosotros') == expected

def test_present_perfect_indicative_vosotros_er():
    expected = "habéis bebido"
    assert Conjugator().conjugate('beber','present_perfect','indicative','vosotros') == expected

def test_present_perfect_indicative_ustedes_ir():
    expected = "han vivido"
    assert Conjugator().conjugate('vivir','present_perfect','indicative','ustedes') == expected