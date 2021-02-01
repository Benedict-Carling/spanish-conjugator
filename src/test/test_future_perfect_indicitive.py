# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ------------------------------ Future Perfect Compound Tense ------------------------------- #

def test_future_perfect_indicative_yo_ar():
    expected = "habré hablado"
    assert Conjugator().conjugate('hablar','future_perfect','indicative','yo') == expected

def test_future_perfect_indicative_tu_ar():
    expected = "habrás hablado"
    assert Conjugator().conjugate('hablar','future_perfect','indicative','tu') == expected

def test_future_perfect_indicative_usted_ar():
    expected = "habrá hablado"
    assert Conjugator().conjugate('hablar','future_perfect','indicative','usted') == expected

def test_future_perfect_indicative_nosotros_ar():
    expected = "habremos hablado"
    assert Conjugator().conjugate('hablar','future_perfect','indicative','nosotros') == expected

def test_future_perfect_indicative_vosotros_ar():
    expected = "habréis hablado"
    assert Conjugator().conjugate('hablar','future_perfect','indicative','vosotros') == expected

def test_future_perfect_indicative_ustedes_ar():
    expected = "habrán hablado"
    assert Conjugator().conjugate('hablar','future_perfect','indicative','ustedes') == expected

def test_future_perfect_indicative_yo_er():
    expected = "habré bebido"
    assert Conjugator().conjugate('beber','future_perfect','indicative','yo') == expected

def test_future_perfect_indicative_tu_ir():
    expected = "habrás vivido"
    assert Conjugator().conjugate('vivir','future_perfect','indicative','tu') == expected

def test_future_perfect_indicative_usted_er():
    expected = "habrá bebido"
    assert Conjugator().conjugate('beber','future_perfect','indicative','usted') == expected

def test_future_perfect_indicative_nosotros_ir():
    expected = "habremos vivido"
    assert Conjugator().conjugate('vivir','future_perfect','indicative','nosotros') == expected

def test_future_perfect_indicative_vosotros_er():
    expected = "habréis bebido"
    assert Conjugator().conjugate('beber','future_perfect','indicative','vosotros') == expected

def test_future_perfect_indicative_ustedes_ir():
    expected = "habrán vivido"
    assert Conjugator().conjugate('vivir','future_perfect','indicative','ustedes') == expected