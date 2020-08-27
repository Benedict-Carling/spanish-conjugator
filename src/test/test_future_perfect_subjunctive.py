# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ------------------------------ Future Perfect Subjunctive Tense ------------------------------- #

def test_future_perfect_subjunctive_yo_ar():
    expected = "hubiere hablado"
    assert Conjugator().conjugate('hablar','future_perfect','subjunctive','yo') == expected

def test_future_perfect_subjunctive_tu_ar():
    expected = "hubieres hablado"
    assert Conjugator().conjugate('hablar','future_perfect','subjunctive','tu') == expected

def test_future_perfect_subjunctive_usted_ar():
    expected = "hubiere hablado"
    assert Conjugator().conjugate('hablar','future_perfect','subjunctive','usted') == expected

def test_future_perfect_subjunctive_nosotros_ar():
    expected = "hubiéremos hablado"
    assert Conjugator().conjugate('hablar','future_perfect','subjunctive','nosotros') == expected

def test_future_perfect_subjunctive_vosotros_ar():
    expected = "hubiereis hablado"
    assert Conjugator().conjugate('hablar','future_perfect','subjunctive','vosotros') == expected

def test_future_perfect_subjunctive_ustedes_ar():
    expected = "hubieren hablado"
    assert Conjugator().conjugate('hablar','future_perfect','subjunctive','ustedes') == expected

def test_future_perfect_subjunctive_yo_er():
    expected = "hubiere bebido"
    assert Conjugator().conjugate('beber','future_perfect','subjunctive','yo') == expected

def test_future_perfect_subjunctive_tu_ir():
    expected = "hubieres vivido"
    assert Conjugator().conjugate('vivir','future_perfect','subjunctive','tu') == expected

def test_future_perfect_subjunctive_usted_er():
    expected = "hubiere bebido"
    assert Conjugator().conjugate('beber','future_perfect','subjunctive','usted') == expected

def test_future_perfect_subjunctive_nosotros_ir():
    expected = "hubiéremos vivido"
    assert Conjugator().conjugate('vivir','future_perfect','subjunctive','nosotros') == expected

def test_future_perfect_subjunctive_vosotros_er():
    expected = "hubiereis bebido"
    assert Conjugator().conjugate('beber','future_perfect','subjunctive','vosotros') == expected

def test_future_perfect_subjunctive_ustedes_ir():
    expected = "hubieren vivido"
    assert Conjugator().conjugate('vivir','future_perfect','subjunctive','ustedes') == expected