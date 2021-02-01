# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ----------------------------------- Future Simple Indicative ----------------------------------- #

def test_future_indicative_yo_ar():
    expected = "hablaré"
    assert Conjugator().conjugate('hablar','future','indicative','yo') == expected

def test_future_indicative_tu_ar():
    expected = "hablarás"
    assert Conjugator().conjugate('hablar','future','indicative','tu') == expected

def test_future_indicative_usted_ar():
    expected = "hablará"
    assert Conjugator().conjugate('hablar','future','indicative','usted') == expected

def test_future_indicative_nosotros_ar():
    expected = 'hablaremos'
    assert str(Conjugator().conjugate('hablar','future','indicative','nosotros')) == expected

def test_future_indicative_vosotros_ar():
    expected = "hablaréis"
    assert Conjugator().conjugate('hablar','future','indicative','vosotros') == expected

def test_future_indicative_ustedes_ar():
    expected = "hablarán"
    assert Conjugator().conjugate('hablar','future','indicative','ustedes') == expected

def test_future_indicative_ustedes_second_exp():
    expected = "charlarán"
    assert Conjugator().conjugate('charlar','future','indicative','ustedes') == expected