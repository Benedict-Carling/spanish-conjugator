# -*- coding: iso-8859-15 -*-
from src.spanishconjugator import Conjugator

def test_imperfect_imperitive_yo_ar():
    expected = "hablaba"
    assert Conjugator().conjugate('hablar','imperfect','imperitive','yo') == expected

def test_imperfect_imperitive_tu_ar():
    expected = "hablabas"
    assert Conjugator().conjugate('hablar','imperfect','imperitive','tu') == expected

def test_imperfect_imperitive_usted_ar():
    expected = "hablaba"
    assert Conjugator().conjugate('hablar','imperfect','imperitive','usted') == expected

def test_imperfect_imperitive_nosotros_ar():
    expected = 'hablábamos'
    assert str(Conjugator().conjugate('hablar','imperfect','imperitive','nosotros')) == expected

def test_imperfect_imperitive_vosotros_ar():
    expected = "hablabais"
    assert Conjugator().conjugate('hablar','imperfect','imperitive','vosotros') == expected

def test_imperfect_imperitive_ustedes_ar():
    expected = "hablaban"
    assert Conjugator().conjugate('hablar','imperfect','imperitive','ustedes') == expected

def test_imperfect_imperitive_yo_ar_3():
    expected = "charlaba"
    assert Conjugator().conjugate('charlar','imperfect','imperitive','yo') == expected

def test_imperfect_imperitive_yo_ar_4():
    expected = "era"
    assert Conjugator().conjugate('ser','imperfect','imperitive','yo') == expected