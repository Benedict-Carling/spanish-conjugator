# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ----------------------------------- Future Simple Indicitive ----------------------------------- #

def test_future_indicitive_yo_ar():
    expected = "hablaré"
    assert Conjugator().conjugate('hablar','future','indicitive','yo') == expected

def test_future_indicitive_tu_ar():
    expected = "hablarás"
    assert Conjugator().conjugate('hablar','future','indicitive','tu') == expected

def test_future_indicitive_usted_ar():
    expected = "hablará"
    assert Conjugator().conjugate('hablar','future','indicitive','usted') == expected

def test_future_indicitive_nosotros_ar():
    expected = 'hablaremos'
    assert str(Conjugator().conjugate('hablar','future','indicitive','nosotros')) == expected

def test_future_indicitive_vosotros_ar():
    expected = "hablaréis"
    assert Conjugator().conjugate('hablar','future','indicitive','vosotros') == expected

def test_future_indicitive_ustedes_ar():
    expected = "hablarán"
    assert Conjugator().conjugate('hablar','future','indicitive','ustedes') == expected

def test_future_indicitive_ustedes_second_exp():
    expected = "charlarán"
    assert Conjugator().conjugate('charlar','future','indicitive','ustedes') == expected