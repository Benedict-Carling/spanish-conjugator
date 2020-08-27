# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ----------------------------------- Present Indicitive ----------------------------------- #

def test_negative_imperitive_tu_ar():
    expected = "hables"
    assert Conjugator().conjugate('hablar','negative','imperitive','tu') == expected

def test_negative_imperitive_usted_ar():
    expected = "hable"
    assert Conjugator().conjugate('hablar','negative','imperitive','usted') == expected

def test_negative_imperitive_nosotros_ar():
    expected = 'hablemos'
    assert str(Conjugator().conjugate('hablar','negative','imperitive','nosotros')) == expected

def test_negative_imperitive_vosotros_ar():
    expected = "habléis"
    assert Conjugator().conjugate('hablar','negative','imperitive','vosotros') == expected

def test_negative_imperitive_ustedes_ar():
    expected = "hablen"
    assert Conjugator().conjugate('hablar','negative','imperitive','ustedes') == expected