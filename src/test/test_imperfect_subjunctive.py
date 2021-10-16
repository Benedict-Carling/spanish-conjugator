# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ----------------------------------- Imperfect Subjunctive ----------------------------------- #


def test_imperfect_subjunctive_yo_ar():
    expected = "hablara"
    assert (
        Conjugator().conjugate("hablar", "imperfect", "subjunctive", "yo") == expected
    )


def test_imperfect_subjunctive_tu_ar():
    expected = "hablaras"
    assert (
        Conjugator().conjugate("hablar", "imperfect", "subjunctive", "tu") == expected
    )


def test_imperfect_subjunctive_usted_ar():
    expected = "hablara"
    assert (
        Conjugator().conjugate("hablar", "imperfect", "subjunctive", "usted")
        == expected
    )


def test_imperfect_subjunctive_nosotros_ar():
    expected = "habláramos"
    assert (
        str(Conjugator().conjugate("hablar", "imperfect", "subjunctive", "nosotros"))
        == expected
    )


def test_imperfect_subjunctive_vosotros_ar():
    expected = "hablarais"
    assert (
        Conjugator().conjugate("hablar", "imperfect", "subjunctive", "vosotros")
        == expected
    )


def test_imperfect_subjunctive_ustedes_ar():
    expected = "hablaran"
    assert (
        Conjugator().conjugate("hablar", "imperfect", "subjunctive", "ustedes")
        == expected
    )
