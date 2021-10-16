# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ------------------------------ Past Perfect Compound Tense ------------------------------- #


def test_past_perfect_indicative_yo_ar():
    expected = "había hablado"
    assert (
        Conjugator().conjugate("hablar", "past_perfect", "indicative", "yo") == expected
    )


def test_past_perfect_indicative_tu_ar():
    expected = "habías hablado"
    assert (
        Conjugator().conjugate("hablar", "past_perfect", "indicative", "tu") == expected
    )


def test_past_perfect_indicative_usted_ar():
    expected = "había hablado"
    assert (
        Conjugator().conjugate("hablar", "past_perfect", "indicative", "usted")
        == expected
    )


def test_past_perfect_indicative_nosotros_ar():
    expected = "habíamos hablado"
    assert (
        Conjugator().conjugate("hablar", "past_perfect", "indicative", "nosotros")
        == expected
    )


def test_past_perfect_indicative_vosotros_ar():
    expected = "habíais hablado"
    assert (
        Conjugator().conjugate("hablar", "past_perfect", "indicative", "vosotros")
        == expected
    )


def test_past_perfect_indicative_ustedes_ar():
    expected = "habían hablado"
    assert (
        Conjugator().conjugate("hablar", "past_perfect", "indicative", "ustedes")
        == expected
    )


def test_past_perfect_indicative_yo_er():
    expected = "había bebido"
    assert (
        Conjugator().conjugate("beber", "past_perfect", "indicative", "yo") == expected
    )


def test_past_perfect_indicative_tu_ir():
    expected = "habías vivido"
    assert (
        Conjugator().conjugate("vivir", "past_perfect", "indicative", "tu") == expected
    )


def test_past_perfect_indicative_usted_er():
    expected = "había bebido"
    assert (
        Conjugator().conjugate("beber", "past_perfect", "indicative", "usted")
        == expected
    )


def test_past_perfect_indicative_nosotros_ir():
    expected = "habíamos vivido"
    assert (
        Conjugator().conjugate("vivir", "past_perfect", "indicative", "nosotros")
        == expected
    )


def test_past_perfect_indicative_vosotros_er():
    expected = "habíais bebido"
    assert (
        Conjugator().conjugate("beber", "past_perfect", "indicative", "vosotros")
        == expected
    )


def test_past_perfect_indicative_ustedes_ir():
    expected = "habían vivido"
    assert (
        Conjugator().conjugate("vivir", "past_perfect", "indicative", "ustedes")
        == expected
    )
