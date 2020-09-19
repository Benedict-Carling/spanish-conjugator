# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ----------------------------------- Present Indicitive ----------------------------------- #

def test_future_subjunctive_yo_ar():
    expected = "hablare"
    assert Conjugator().conjugate('hablar','future','subjunctive','yo') == expected

def test_future_subjunctive_tu_ar():
    expected = "hablares"
    assert Conjugator().conjugate('hablar','future','subjunctive','tu') == expected

def test_future_subjunctive_usted_ar():
    expected = "hablare"
    assert Conjugator().conjugate('hablar','future','subjunctive','usted') == expected

def test_future_subjunctive_nosotros_ar():
    expected = 'habláremos'
    assert str(Conjugator().conjugate('hablar','future','subjunctive','nosotros')) == expected

def test_future_subjunctive_vosotros_ar():
    expected = "hablareis"
    assert Conjugator().conjugate('hablar','future','subjunctive','vosotros') == expected

def test_future_subjunctive_ustedes_ar():
    expected = "hablaren"
    assert Conjugator().conjugate('hablar','future','subjunctive','ustedes') == expected