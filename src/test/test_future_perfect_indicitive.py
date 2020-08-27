# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ------------------------------ Future Perfect Compound Tense ------------------------------- #

def test_future_perfect_indicitive_yo_ar():
    expected = "habré hablado"
    assert Conjugator().conjugate('hablar','future_perfect','indicitive','yo') == expected

def test_future_perfect_indicitive_tu_ar():
    expected = "habrás hablado"
    assert Conjugator().conjugate('hablar','future_perfect','indicitive','tu') == expected

def test_future_perfect_indicitive_usted_ar():
    expected = "habrá hablado"
    assert Conjugator().conjugate('hablar','future_perfect','indicitive','usted') == expected

def test_future_perfect_indicitive_nosotros_ar():
    expected = "habremos hablado"
    assert Conjugator().conjugate('hablar','future_perfect','indicitive','nosotros') == expected

def test_future_perfect_indicitive_vosotros_ar():
    expected = "habréis hablado"
    assert Conjugator().conjugate('hablar','future_perfect','indicitive','vosotros') == expected

def test_future_perfect_indicitive_ustedes_ar():
    expected = "habrán hablado"
    assert Conjugator().conjugate('hablar','future_perfect','indicitive','ustedes') == expected

def test_future_perfect_indicitive_yo_er():
    expected = "habré bebido"
    assert Conjugator().conjugate('beber','future_perfect','indicitive','yo') == expected

def test_future_perfect_indicitive_tu_ir():
    expected = "habrás vivido"
    assert Conjugator().conjugate('vivir','future_perfect','indicitive','tu') == expected

def test_future_perfect_indicitive_usted_er():
    expected = "habrá bebido"
    assert Conjugator().conjugate('beber','future_perfect','indicitive','usted') == expected

def test_future_perfect_indicitive_nosotros_ir():
    expected = "habremos vivido"
    assert Conjugator().conjugate('vivir','future_perfect','indicitive','nosotros') == expected

def test_future_perfect_indicitive_vosotros_er():
    expected = "habréis bebido"
    assert Conjugator().conjugate('beber','future_perfect','indicitive','vosotros') == expected

def test_future_perfect_indicitive_ustedes_ir():
    expected = "habrán vivido"
    assert Conjugator().conjugate('vivir','future_perfect','indicitive','ustedes') == expected