# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

# ------------------------------ Present Perfect Compound Tense ------------------------------- #


def test_perfect_conditional_yo_ar():
    expected = "habría hablado"
    assert Conjugator().conjugate("hablar", "perfect", "conditional", "yo") == expected


def test_perfect_conditional_tu_ar():
    expected = "habrías hablado"
    assert Conjugator().conjugate("hablar", "perfect", "conditional", "tu") == expected


def test_perfect_conditional_usted_ar():
    expected = "habría hablado"
    assert (
        Conjugator().conjugate("hablar", "perfect", "conditional", "usted") == expected
    )


def test_perfect_conditional_nosotros_ar():
    expected = "habríamos hablado"
    assert (
        Conjugator().conjugate("hablar", "perfect", "conditional", "nosotros")
        == expected
    )


def test_perfect_conditional_vosotros_ar():
    expected = "habríais hablado"
    assert (
        Conjugator().conjugate("hablar", "perfect", "conditional", "vosotros")
        == expected
    )


def test_perfect_conditional_ustedes_ar():
    expected = "habrían hablado"
    assert (
        Conjugator().conjugate("hablar", "perfect", "conditional", "ustedes")
        == expected
    )


def test_perfect_conditional_yo_er():
    expected = "habría bebido"
    assert Conjugator().conjugate("beber", "perfect", "conditional", "yo") == expected


def test_perfect_conditional_tu_ir():
    expected = "habrías vivido"
    assert Conjugator().conjugate("vivir", "perfect", "conditional", "tu") == expected


def test_perfect_conditional_usted_er():
    expected = "habría bebido"
    assert (
        Conjugator().conjugate("beber", "perfect", "conditional", "usted") == expected
    )


def test_perfect_conditional_nosotros_ir():
    expected = "habríamos vivido"
    assert (
        Conjugator().conjugate("vivir", "perfect", "conditional", "nosotros")
        == expected
    )


def test_perfect_conditional_vosotros_er():
    expected = "habríais bebido"
    assert (
        Conjugator().conjugate("beber", "perfect", "conditional", "vosotros")
        == expected
    )


def test_perfect_conditional_ustedes_ir():
    expected = "habrían vivido"
    assert (
        Conjugator().conjugate("vivir", "perfect", "conditional", "ustedes") == expected
    )
