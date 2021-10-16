# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ----------------------------------- Future Preterite Indicative ----------------------------------- #


def test_preterite_indicative_yo_ar():
    expected = "hablé"
    assert Conjugator().conjugate("hablar", "preterite", "indicative", "yo") == expected


def test_preterite_indicative_tu_ar():
    expected = "hablaste"
    assert Conjugator().conjugate("hablar", "preterite", "indicative", "tu") == expected


def test_preterite_indicative_usted_ar():
    expected = "habló"
    assert (
        Conjugator().conjugate("hablar", "preterite", "indicative", "usted") == expected
    )


def test_preterite_indicative_nosotros_ar():
    expected = "hablamos"
    assert (
        str(Conjugator().conjugate("hablar", "preterite", "indicative", "nosotros"))
        == expected
    )


def test_preterite_indicative_vosotros_ar():
    expected = "hablasteis"
    assert (
        Conjugator().conjugate("hablar", "preterite", "indicative", "vosotros")
        == expected
    )


def test_preterite_indicative_ustedes_ar():
    expected = "hablaron"
    assert (
        Conjugator().conjugate("hablar", "preterite", "indicative", "ustedes")
        == expected
    )
