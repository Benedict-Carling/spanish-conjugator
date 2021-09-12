# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ----------------------------------- Present Imperative ----------------------------------- #


def test_affirmative_imperative_tu_ar():
    expected = "habla"
    assert (
        Conjugator().conjugate("hablar", "affirmative", "imperative", "tu") == expected
    )


def test_affirmative_imperative_usted_ar():
    expected = "hable"
    assert (
        Conjugator().conjugate("hablar", "affirmative", "imperative", "usted")
        == expected
    )


def test_affirmative_imperative_nosotros_ar():
    expected = "hablemos"
    assert (
        str(Conjugator().conjugate("hablar", "affirmative", "imperative", "nosotros"))
        == expected
    )


def test_affirmative_imperative_vosotros_ar():
    expected = "hablad"
    assert (
        Conjugator().conjugate("hablar", "affirmative", "imperative", "vosotros")
        == expected
    )


def test_affirmative_imperative_ustedes_ar():
    expected = "hablen"
    assert (
        Conjugator().conjugate("hablar", "affirmative", "imperative", "ustedes")
        == expected
    )
