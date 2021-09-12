# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ----------------------------------- Present Imperative ----------------------------------- #


def test_negative_imperative_tu_ar():
    expected = "hables"
    assert Conjugator().conjugate("hablar", "negative", "imperative", "tu") == expected


def test_negative_imperative_usted_ar():
    expected = "hable"
    assert (
        Conjugator().conjugate("hablar", "negative", "imperative", "usted") == expected
    )


def test_negative_imperative_nosotros_ar():
    expected = "hablemos"
    assert (
        str(Conjugator().conjugate("hablar", "negative", "imperative", "nosotros"))
        == expected
    )


def test_negative_imperative_vosotros_ar():
    expected = "habléis"
    assert (
        Conjugator().conjugate("hablar", "negative", "imperative", "vosotros")
        == expected
    )


def test_negative_imperative_ustedes_ar():
    expected = "hablen"
    assert (
        Conjugator().conjugate("hablar", "negative", "imperative", "ustedes")
        == expected
    )
