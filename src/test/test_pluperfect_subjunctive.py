# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ------------------------------ Pluperfect Subjunctive Tense ------------------------------- #


def test_pluperfect_subjunctive_yo_ar():
    expected = "hubiera hablado"
    assert (
        Conjugator().conjugate("hablar", "pluperfect", "subjunctive", "yo") == expected
    )


def test_pluperfect_subjunctive_tu_ar():
    expected = "hubieras hablado"
    assert (
        Conjugator().conjugate("hablar", "pluperfect", "subjunctive", "tu") == expected
    )


def test_pluperfect_subjunctive_usted_ar():
    expected = "hubiera hablado"
    assert (
        Conjugator().conjugate("hablar", "pluperfect", "subjunctive", "usted")
        == expected
    )


def test_pluperfect_subjunctive_nosotros_ar():
    expected = "hubiéramos hablado"
    assert (
        Conjugator().conjugate("hablar", "pluperfect", "subjunctive", "nosotros")
        == expected
    )


def test_pluperfect_subjunctive_vosotros_ar():
    expected = "hubierais hablado"
    assert (
        Conjugator().conjugate("hablar", "pluperfect", "subjunctive", "vosotros")
        == expected
    )


def test_pluperfect_subjunctive_ustedes_ar():
    expected = "hubieran hablado"
    assert (
        Conjugator().conjugate("hablar", "pluperfect", "subjunctive", "ustedes")
        == expected
    )


def test_pluperfect_subjunctive_yo_er():
    expected = "hubiera bebido"
    assert (
        Conjugator().conjugate("beber", "pluperfect", "subjunctive", "yo") == expected
    )


def test_pluperfect_subjunctive_tu_ir():
    expected = "hubieras vivido"
    assert (
        Conjugator().conjugate("vivir", "pluperfect", "subjunctive", "tu") == expected
    )


def test_pluperfect_subjunctive_usted_er():
    expected = "hubiera bebido"
    assert (
        Conjugator().conjugate("beber", "pluperfect", "subjunctive", "usted")
        == expected
    )


def test_pluperfect_subjunctive_nosotros_ir():
    expected = "hubiéramos vivido"
    assert (
        Conjugator().conjugate("vivir", "pluperfect", "subjunctive", "nosotros")
        == expected
    )


def test_pluperfect_subjunctive_vosotros_er():
    expected = "hubierais bebido"
    assert (
        Conjugator().conjugate("beber", "pluperfect", "subjunctive", "vosotros")
        == expected
    )


def test_pluperfect_subjunctive_ustedes_ir():
    expected = "hubieran vivido"
    assert (
        Conjugator().conjugate("vivir", "pluperfect", "subjunctive", "ustedes")
        == expected
    )
