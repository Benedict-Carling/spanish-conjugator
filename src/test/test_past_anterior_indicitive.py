# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ------------------------------ Past anterior Compound Tense ------------------------------- #

def test_past_anterior_indicative_yo_ar():
    expected = "hube hablado"
    assert Conjugator().conjugate('hablar','past_anterior','indicative','yo') == expected

def test_past_anterior_indicative_tu_ar():
    expected = "hubiste hablado"
    assert Conjugator().conjugate('hablar','past_anterior','indicative','tu') == expected

def test_past_anterior_indicative_usted_ar():
    expected = "hubo hablado"
    assert Conjugator().conjugate('hablar','past_anterior','indicative','usted') == expected

def test_past_anterior_indicative_nosotros_ar():
    expected = "hubimos hablado"
    assert Conjugator().conjugate('hablar','past_anterior','indicative','nosotros') == expected

def test_past_anterior_indicative_vosotros_ar():
    expected = "hubisteis hablado"
    assert Conjugator().conjugate('hablar','past_anterior','indicative','vosotros') == expected

def test_past_anterior_indicative_ustedes_ar():
    expected = "hubieron hablado"
    assert Conjugator().conjugate('hablar','past_anterior','indicative','ustedes') == expected

def test_past_anterior_indicative_yo_er():
    expected = "hube bebido"
    assert Conjugator().conjugate('beber','past_anterior','indicative','yo') == expected

def test_past_anterior_indicative_tu_ir():
    expected = "hubiste vivido"
    assert Conjugator().conjugate('vivir','past_anterior','indicative','tu') == expected

def test_past_anterior_indicative_usted_er():
    expected = "hubo bebido"
    assert Conjugator().conjugate('beber','past_anterior','indicative','usted') == expected

def test_past_anterior_indicative_nosotros_ir():
    expected = "hubimos vivido"
    assert Conjugator().conjugate('vivir','past_anterior','indicative','nosotros') == expected

def test_past_anterior_indicative_vosotros_er():
    expected = "hubisteis bebido"
    assert Conjugator().conjugate('beber','past_anterior','indicative','vosotros') == expected

def test_past_anterior_indicative_ustedes_ir():
    expected = "hubieron vivido"
    assert Conjugator().conjugate('vivir','past_anterior','indicative','ustedes') == expected
