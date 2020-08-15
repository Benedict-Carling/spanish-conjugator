# -*- coding: iso-8859-15 -*-
from src.spanishconjugator import Conjugator

def test_imperfect_indicitive_yo_ar():
    expected = "hablaba"
    assert Conjugator().conjugate('hablar','imperfect','indicitive','yo') == expected

def test_imperfect_indicitive_tu_ar():
    expected = "hablabas"
    assert Conjugator().conjugate('hablar','imperfect','indicitive','tu') == expected

def test_imperfect_indicitive_usted_ar():
    expected = "hablaba"
    assert Conjugator().conjugate('hablar','imperfect','indicitive','usted') == expected

def test_imperfect_indicitive_nosotros_ar():
    expected = 'hablábamos'
    assert str(Conjugator().conjugate('hablar','imperfect','indicitive','nosotros')) == expected

def test_imperfect_indicitive_vosotros_ar():
    expected = "hablabais"
    assert Conjugator().conjugate('hablar','imperfect','indicitive','vosotros') == expected

def test_imperfect_indicitive_ustedes_ar():
    expected = "hablaban"
    assert Conjugator().conjugate('hablar','imperfect','indicitive','ustedes') == expected

def test_imperfect_indicitive_yo_ar_3():
    expected = "charlaba"
    assert Conjugator().conjugate('charlar','imperfect','indicitive','yo') == expected

def test_imperfect_indicitive_yo_ar_4():
    expected = "era"
    assert Conjugator().conjugate('ser','imperfect','indicitive','yo') == expected