# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ------------------------------ Simple Conditional Conditional Tense ------------------------------- #

def test_simple_conditional_conditional_yo_ar():
    expected = "hablaría"
    assert Conjugator().conjugate('hablar','simple_conditional','conditional','yo') == expected

def test_simple_conditional_conditional_tu_ar():
    expected = "hablarías"
    assert Conjugator().conjugate('hablar','simple_conditional','conditional','tu') == expected

def test_simple_conditional_conditional_usted_ar():
    expected = "hablaría"
    assert Conjugator().conjugate('hablar','simple_conditional','conditional','usted') == expected

def test_simple_conditional_conditional_nosotros_ar():
    expected = "hablaríamos"
    assert Conjugator().conjugate('hablar','simple_conditional','conditional','nosotros') == expected

def test_simple_conditional_conditional_vosotros_ar():
    expected = "hablaríais"
    assert Conjugator().conjugate('hablar','simple_conditional','conditional','vosotros') == expected

def test_simple_conditional_conditional_ustedes_ar():
    expected = "hablarían"
    assert Conjugator().conjugate('hablar','simple_conditional','conditional','ustedes') == expected

def test_simple_conditional_conditional_yo_er():
    expected = "bebería"
    assert Conjugator().conjugate('beber','simple_conditional','conditional','yo') == expected

def test_simple_conditional_conditional_tu_ir():
    expected = "vivirías"
    assert Conjugator().conjugate('vivir','simple_conditional','conditional','tu') == expected

def test_simple_conditional_conditional_usted_er():
    expected = "bebería"
    assert Conjugator().conjugate('beber','simple_conditional','conditional','usted') == expected

def test_simple_conditional_conditional_nosotros_ir():
    expected = "viviríamos"
    assert Conjugator().conjugate('vivir','simple_conditional','conditional','nosotros') == expected

def test_simple_conditional_conditional_vosotros_er():
    expected = "beberíais"
    assert Conjugator().conjugate('beber','simple_conditional','conditional','vosotros') == expected

def test_simple_conditional_conditional_ustedes_ir():
    expected = "vivirían"
    assert Conjugator().conjugate('vivir','simple_conditional','conditional','ustedes') == expected

