# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ------------------------------ Present Perfect Subjunctive Tense ------------------------------- #

def test_present_perfect_subjunctive_yo_ar():
    expected = "haya hablado"
    assert Conjugator().conjugate('hablar','present_perfect','subjunctive','yo') == expected

def test_present_perfect_subjunctive_tu_ar():
    expected = "hayas hablado"
    assert Conjugator().conjugate('hablar','present_perfect','subjunctive','tu') == expected

def test_present_perfect_subjunctive_usted_ar():
    expected = "haya hablado"
    assert Conjugator().conjugate('hablar','present_perfect','subjunctive','usted') == expected

def test_present_perfect_subjunctive_nosotros_ar():
    expected = "hayamos hablado"
    assert Conjugator().conjugate('hablar','present_perfect','subjunctive','nosotros') == expected

def test_present_perfect_subjunctive_vosotros_ar():
    expected = "hayáis hablado"
    assert Conjugator().conjugate('hablar','present_perfect','subjunctive','vosotros') == expected

def test_present_perfect_subjunctive_ustedes_ar():
    expected = "hayan hablado"
    assert Conjugator().conjugate('hablar','present_perfect','subjunctive','ustedes') == expected

def test_present_perfect_subjunctive_yo_er():
    expected = "haya bebido"
    assert Conjugator().conjugate('beber','present_perfect','subjunctive','yo') == expected

def test_present_perfect_subjunctive_tu_ir():
    expected = "hayas vivido"
    assert Conjugator().conjugate('vivir','present_perfect','subjunctive','tu') == expected

def test_present_perfect_subjunctive_usted_er():
    expected = "haya bebido"
    assert Conjugator().conjugate('beber','present_perfect','subjunctive','usted') == expected

def test_present_perfect_subjunctive_nosotros_ir():
    expected = "hayamos vivido"
    assert Conjugator().conjugate('vivir','present_perfect','subjunctive','nosotros') == expected

def test_present_perfect_subjunctive_vosotros_er():
    expected = "hayáis bebido"
    assert Conjugator().conjugate('beber','present_perfect','subjunctive','vosotros') == expected

def test_present_perfect_subjunctive_ustedes_ir():
    expected = "hayan vivido"
    assert Conjugator().conjugate('vivir','present_perfect','subjunctive','ustedes') == expected