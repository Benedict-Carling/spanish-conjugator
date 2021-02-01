# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ----------------------------------- Present Imperative ----------------------------------- #

def test_affirmative_imperitive_tu_ar():
    expected = "habla"
    assert Conjugator().conjugate('hablar','affirmative','imperitive','tu') == expected

def test_affirmative_imperitive_usted_ar():
    expected = "hable"
    assert Conjugator().conjugate('hablar','affirmative','imperitive','usted') == expected

def test_affirmative_imperitive_nosotros_ar():
    expected = 'hablemos'
    assert str(Conjugator().conjugate('hablar','affirmative','imperitive','nosotros')) == expected

def test_affirmative_imperitive_vosotros_ar():
    expected = "hablad"
    assert Conjugator().conjugate('hablar','affirmative','imperitive','vosotros') == expected

def test_affirmative_imperitive_ustedes_ar():
    expected = "hablen"
    assert Conjugator().conjugate('hablar','affirmative','imperitive','ustedes') == expected
