# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ----------------------------------- Imperfect Indicative ----------------------------------- #


def test_imperfect_indicative_yo_ar():
    expected = "hablaba"
    assert Conjugator().conjugate("hablar", "imperfect", "indicative", "yo") == expected


def test_imperfect_indicative_tu_ar():
    expected = "hablabas"
    assert Conjugator().conjugate("hablar", "imperfect", "indicative", "tu") == expected


def test_imperfect_indicative_usted_ar():
    expected = "hablaba"
    assert (
        Conjugator().conjugate("hablar", "imperfect", "indicative", "usted") == expected
    )


def test_imperfect_indicative_nosotros_ar():
    expected = "hablábamos"
    assert (
        str(Conjugator().conjugate("hablar", "imperfect", "indicative", "nosotros"))
        == expected
    )


def test_imperfect_indicative_vosotros_ar():
    expected = "hablabais"
    assert (
        Conjugator().conjugate("hablar", "imperfect", "indicative", "vosotros")
        == expected
    )


def test_imperfect_indicative_ustedes_ar():
    expected = "hablaban"
    assert (
        Conjugator().conjugate("hablar", "imperfect", "indicative", "ustedes")
        == expected
    )


def test_imperfect_indicative_yo_ar_3():
    expected = "charlaba"
    assert (
        Conjugator().conjugate("charlar", "imperfect", "indicative", "yo") == expected
    )


def test_imperfect_indicative_yo_ar_4():
    expected = "era"
    assert Conjugator().conjugate("ser", "imperfect", "indicative", "yo") == expected
