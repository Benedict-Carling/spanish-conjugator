# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ------------------------------ Past Perfect Compound Tense ------------------------------- #

def test_past_perfect_indicitive_yo_ar():
    expected = "había hablado"
    assert Conjugator().conjugate('hablar','past_perfect','indicitive','yo') == expected

def test_past_perfect_indicitive_tu_ar():
    expected = "habías hablado"
    assert Conjugator().conjugate('hablar','past_perfect','indicitive','tu') == expected

def test_past_perfect_indicitive_usted_ar():
    expected = "había hablado"
    assert Conjugator().conjugate('hablar','past_perfect','indicitive','usted') == expected

def test_past_perfect_indicitive_nosotros_ar():
    expected = "habíamos hablado"
    assert Conjugator().conjugate('hablar','past_perfect','indicitive','nosotros') == expected

def test_past_perfect_indicitive_vosotros_ar():
    expected = "habíais hablado"
    assert Conjugator().conjugate('hablar','past_perfect','indicitive','vosotros') == expected

def test_past_perfect_indicitive_ustedes_ar():
    expected = "habían hablado"
    assert Conjugator().conjugate('hablar','past_perfect','indicitive','ustedes') == expected

def test_past_perfect_indicitive_yo_er():
    expected = "había bebido"
    assert Conjugator().conjugate('beber','past_perfect','indicitive','yo') == expected

def test_past_perfect_indicitive_tu_ir():
    expected = "habías vivido"
    assert Conjugator().conjugate('vivir','past_perfect','indicitive','tu') == expected

def test_past_perfect_indicitive_usted_er():
    expected = "había bebido"
    assert Conjugator().conjugate('beber','past_perfect','indicitive','usted') == expected

def test_past_perfect_indicitive_nosotros_ir():
    expected = "habíamos vivido"
    assert Conjugator().conjugate('vivir','past_perfect','indicitive','nosotros') == expected

def test_past_perfect_indicitive_vosotros_er():
    expected = "habíais bebido"
    assert Conjugator().conjugate('beber','past_perfect','indicitive','vosotros') == expected

def test_past_perfect_indicitive_ustedes_ir():
    expected = "habían vivido"
    assert Conjugator().conjugate('vivir','past_perfect','indicitive','ustedes') == expected