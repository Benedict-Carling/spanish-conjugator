# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ----------------------------------- Present Subjunctive ----------------------------------- #


def test_present_subjunctive_yo_ar():
    expected = "hable"
    assert Conjugator().conjugate("hablar", "present", "subjunctive", "yo") == expected


def test_present_subjunctive_tu_ar():
    expected = "hables"
    assert Conjugator().conjugate("hablar", "present", "subjunctive", "tu") == expected


def test_present_subjunctive_usted_ar():
    expected = "hable"
    assert (
        Conjugator().conjugate("hablar", "present", "subjunctive", "usted") == expected
    )


def test_present_subjunctive_nosotros_ar():
    expected = "hablemos"
    assert (
        str(Conjugator().conjugate("hablar", "present", "subjunctive", "nosotros"))
        == expected
    )


def test_present_subjunctive_vosotros_ar():
    expected = "habléis"
    assert (
        Conjugator().conjugate("hablar", "present", "subjunctive", "vosotros")
        == expected
    )


def test_present_subjunctive_ustedes_ar():
    expected = "hablen"
    assert (
        Conjugator().conjugate("hablar", "present", "subjunctive", "ustedes")
        == expected
    )
