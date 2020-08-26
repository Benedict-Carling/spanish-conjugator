# -*- coding: iso-8859-15 -*-
import spanishconjugator
from spanishconjugator.spanishconjugator import Conjugator

# ----------------------------------- imperfect Indicitive ----------------------------------- #

def test_imperfect_indicitive_yo_ar():
    expected = "hablaba"
    assert Conjugator().conjugate('hablar','imperfect','indicitive','yo') == expected

def test_imperfect_indicitive_tu_ar():
    expected = "hablabas"
    assert Conjugator().conjugate('hablar','imperfect','indicitive','tu') == expected

def test_imperfect_indicitive_usted_ar():
    expected = "hablaba"
    assert Conjugator().conjugate('hablar','imperfect','indicitive','usted') == expected

def test_imperfect_indicitive_nosotros_ar():
    expected = 'hablábamos'
    assert str(Conjugator().conjugate('hablar','imperfect','indicitive','nosotros')) == expected

def test_imperfect_indicitive_vosotros_ar():
    expected = "hablabais"
    assert Conjugator().conjugate('hablar','imperfect','indicitive','vosotros') == expected

def test_imperfect_indicitive_ustedes_ar():
    expected = "hablaban"
    assert Conjugator().conjugate('hablar','imperfect','indicitive','ustedes') == expected

# ----------------------------------- Present Indicitive ----------------------------------- #

def test_present_indicitive_yo_ar():
    expected = "hablo"
    assert Conjugator().conjugate('hablar','present','indicitive','yo') == expected

def test_present_indicitive_tu_ar():
    expected = "hablas"
    assert Conjugator().conjugate('hablar','present','indicitive','tu') == expected

def test_present_indicitive_usted_ar():
    expected = "habla"
    assert Conjugator().conjugate('hablar','present','indicitive','usted') == expected

def test_present_indicitive_nosotros_ar():
    expected = 'hablamos'
    assert str(Conjugator().conjugate('hablar','present','indicitive','nosotros')) == expected

def test_present_indicitive_vosotros_ar():
    expected = "habláis"
    assert Conjugator().conjugate('hablar','present','indicitive','vosotros') == expected

def test_present_indicitive_ustedes_ar():
    expected = "hablan"
    assert Conjugator().conjugate('hablar','present','indicitive','ustedes') == expected

# ----------------------------------- Imperfect Indicitive ----------------------------------- #

def test_imperfect_indicitive_yo_ar_3():
    expected = "charlaba"
    assert Conjugator().conjugate('charlar','imperfect','indicitive','yo') == expected

def test_imperfect_indicitive_yo_ar_4():
    expected = "era"
    assert Conjugator().conjugate('ser','imperfect','indicitive','yo') == expected

def test_preterite_indicitive_yo_ar():
    expected = "hablé"
    assert Conjugator().conjugate('hablar','preterite','indicitive','yo') == expected

def test_preterite_indicitive_tu_ar():
    expected = "hablaste"
    assert Conjugator().conjugate('hablar','preterite','indicitive','tu') == expected

def test_preterite_indicitive_usted_ar():
    expected = "habló"
    assert Conjugator().conjugate('hablar','preterite','indicitive','usted') == expected

def test_preterite_indicitive_nosotros_ar():
    expected = 'hablamos'
    assert str(Conjugator().conjugate('hablar','preterite','indicitive','nosotros')) == expected

def test_preterite_indicitive_vosotros_ar():
    expected = "hablasteis"
    assert Conjugator().conjugate('hablar','preterite','indicitive','vosotros') == expected

def test_preterite_indicitive_ustedes_ar():
    expected = "hablaron"
    assert Conjugator().conjugate('hablar','preterite','indicitive','ustedes') == expected

# ----------------------------------- Future Simple Indicitive ----------------------------------- #

def test_future_indicitive_yo_ar():
    expected = "hablaré"
    assert Conjugator().conjugate('hablar','future','indicitive','yo') == expected

def test_future_indicitive_tu_ar():
    expected = "hablarás"
    assert Conjugator().conjugate('hablar','future','indicitive','tu') == expected

def test_future_indicitive_usted_ar():
    expected = "hablará"
    assert Conjugator().conjugate('hablar','future','indicitive','usted') == expected

def test_future_indicitive_nosotros_ar():
    expected = 'hablaremos'
    assert str(Conjugator().conjugate('hablar','future','indicitive','nosotros')) == expected

def test_future_indicitive_vosotros_ar():
    expected = "hablaréis"
    assert Conjugator().conjugate('hablar','future','indicitive','vosotros') == expected

def test_future_indicitive_ustedes_ar():
    expected = "hablarán"
    assert Conjugator().conjugate('hablar','future','indicitive','ustedes') == expected

def test_future_indicitive_ustedes_second_exp():
    expected = "charlarán"
    assert Conjugator().conjugate('charlar','future','indicitive','ustedes') == expected


# ------------------------------ Present Perfect Compound Tense ------------------------------- #

def test_present_perfect_indicitive_yo_ar():
    expected = "he hablado"
    assert Conjugator().conjugate('hablar','present_perfect','indicitive','yo') == expected

def test_present_perfect_indicitive_tu_ar():
    expected = "has hablado"
    assert Conjugator().conjugate('hablar','present_perfect','indicitive','tu') == expected

def test_present_perfect_indicitive_usted_ar():
    expected = "ha hablado"
    assert Conjugator().conjugate('hablar','present_perfect','indicitive','usted') == expected

def test_present_perfect_indicitive_nosotros_ar():
    expected = "hemos hablado"
    assert Conjugator().conjugate('hablar','present_perfect','indicitive','nosotros') == expected

def test_present_perfect_indicitive_vosotros_ar():
    expected = "habéis hablado"
    assert Conjugator().conjugate('hablar','present_perfect','indicitive','vosotros') == expected

def test_present_perfect_indicitive_ustedes_ar():
    expected = "han hablado"
    assert Conjugator().conjugate('hablar','present_perfect','indicitive','ustedes') == expected

def test_present_perfect_indicitive_yo_er():
    expected = "he bebido"
    assert Conjugator().conjugate('beber','present_perfect','indicitive','yo') == expected

def test_present_perfect_indicitive_tu_ir():
    expected = "has vivido"
    assert Conjugator().conjugate('vivir','present_perfect','indicitive','tu') == expected

def test_present_perfect_indicitive_usted_er():
    expected = "ha bebido"
    assert Conjugator().conjugate('beber','present_perfect','indicitive','usted') == expected

def test_present_perfect_indicitive_nosotros_ir():
    expected = "hemos vivido"
    assert Conjugator().conjugate('vivir','present_perfect','indicitive','nosotros') == expected

def test_present_perfect_indicitive_vosotros_er():
    expected = "habéis bebido"
    assert Conjugator().conjugate('beber','present_perfect','indicitive','vosotros') == expected

def test_present_perfect_indicitive_ustedes_ir():
    expected = "han vivido"
    assert Conjugator().conjugate('vivir','present_perfect','indicitive','ustedes') == expected


# ------------------------------ Past Perfect Compound Tense ------------------------------- #

def test_past_perfect_indicitive_yo_ar():
    expected = "había hablado"
    assert Conjugator().conjugate('hablar','past_perfect','indicitive','yo') == expected

def test_past_perfect_indicitive_tu_ar():
    expected = "habías hablado"
    assert Conjugator().conjugate('hablar','past_perfect','indicitive','tu') == expected

def test_past_perfect_indicitive_usted_ar():
    expected = "había hablado"
    assert Conjugator().conjugate('hablar','past_perfect','indicitive','usted') == expected

def test_past_perfect_indicitive_nosotros_ar():
    expected = "habíamos hablado"
    assert Conjugator().conjugate('hablar','past_perfect','indicitive','nosotros') == expected

def test_past_perfect_indicitive_vosotros_ar():
    expected = "habíais hablado"
    assert Conjugator().conjugate('hablar','past_perfect','indicitive','vosotros') == expected

def test_past_perfect_indicitive_ustedes_ar():
    expected = "habían hablado"
    assert Conjugator().conjugate('hablar','past_perfect','indicitive','ustedes') == expected

def test_past_perfect_indicitive_yo_er():
    expected = "había bebido"
    assert Conjugator().conjugate('beber','past_perfect','indicitive','yo') == expected

def test_past_perfect_indicitive_tu_ir():
    expected = "habías vivido"
    assert Conjugator().conjugate('vivir','past_perfect','indicitive','tu') == expected

def test_past_perfect_indicitive_usted_er():
    expected = "había bebido"
    assert Conjugator().conjugate('beber','past_perfect','indicitive','usted') == expected

def test_past_perfect_indicitive_nosotros_ir():
    expected = "habíamos vivido"
    assert Conjugator().conjugate('vivir','past_perfect','indicitive','nosotros') == expected

def test_past_perfect_indicitive_vosotros_er():
    expected = "habíais bebido"
    assert Conjugator().conjugate('beber','past_perfect','indicitive','vosotros') == expected

def test_past_perfect_indicitive_ustedes_ir():
    expected = "habían vivido"
    assert Conjugator().conjugate('vivir','past_perfect','indicitive','ustedes') == expected

# ------------------------------ Past anterior Compound Tense ------------------------------- #

def test_past_anterior_indicitive_yo_ar():
    expected = "hube hablado"
    assert Conjugator().conjugate('hablar','past_anterior','indicitive','yo') == expected

def test_past_anterior_indicitive_tu_ar():
    expected = "hubiste hablado"
    assert Conjugator().conjugate('hablar','past_anterior','indicitive','tu') == expected

def test_past_anterior_indicitive_usted_ar():
    expected = "hubo hablado"
    assert Conjugator().conjugate('hablar','past_anterior','indicitive','usted') == expected

def test_past_anterior_indicitive_nosotros_ar():
    expected = "hubimos hablado"
    assert Conjugator().conjugate('hablar','past_anterior','indicitive','nosotros') == expected

def test_past_anterior_indicitive_vosotros_ar():
    expected = "hubisteis hablado"
    assert Conjugator().conjugate('hablar','past_anterior','indicitive','vosotros') == expected

def test_past_anterior_indicitive_ustedes_ar():
    expected = "hubieron hablado"
    assert Conjugator().conjugate('hablar','past_anterior','indicitive','ustedes') == expected

def test_past_anterior_indicitive_yo_er():
    expected = "hube bebido"
    assert Conjugator().conjugate('beber','past_anterior','indicitive','yo') == expected

def test_past_anterior_indicitive_tu_ir():
    expected = "hubiste vivido"
    assert Conjugator().conjugate('vivir','past_anterior','indicitive','tu') == expected

def test_past_anterior_indicitive_usted_er():
    expected = "hubo bebido"
    assert Conjugator().conjugate('beber','past_anterior','indicitive','usted') == expected

def test_past_anterior_indicitive_nosotros_ir():
    expected = "hubimos vivido"
    assert Conjugator().conjugate('vivir','past_anterior','indicitive','nosotros') == expected

def test_past_anterior_indicitive_vosotros_er():
    expected = "hubisteis bebido"
    assert Conjugator().conjugate('beber','past_anterior','indicitive','vosotros') == expected

def test_past_anterior_indicitive_ustedes_ir():
    expected = "hubieron vivido"
    assert Conjugator().conjugate('vivir','past_anterior','indicitive','ustedes') == expected

# ------------------------------ Future Perfect Compound Tense ------------------------------- #

def test_future_perfect_indicitive_yo_ar():
    expected = "habré hablado"
    assert Conjugator().conjugate('hablar','future_perfect','indicitive','yo') == expected

def test_future_perfect_indicitive_tu_ar():
    expected = "habrás hablado"
    assert Conjugator().conjugate('hablar','future_perfect','indicitive','tu') == expected

def test_future_perfect_indicitive_usted_ar():
    expected = "habrá hablado"
    assert Conjugator().conjugate('hablar','future_perfect','indicitive','usted') == expected

def test_future_perfect_indicitive_nosotros_ar():
    expected = "habremos hablado"
    assert Conjugator().conjugate('hablar','future_perfect','indicitive','nosotros') == expected

def test_future_perfect_indicitive_vosotros_ar():
    expected = "habréis hablado"
    assert Conjugator().conjugate('hablar','future_perfect','indicitive','vosotros') == expected

def test_future_perfect_indicitive_ustedes_ar():
    expected = "habrán hablado"
    assert Conjugator().conjugate('hablar','future_perfect','indicitive','ustedes') == expected

def test_future_perfect_indicitive_yo_er():
    expected = "habré bebido"
    assert Conjugator().conjugate('beber','future_perfect','indicitive','yo') == expected

def test_future_perfect_indicitive_tu_ir():
    expected = "habrás vivido"
    assert Conjugator().conjugate('vivir','future_perfect','indicitive','tu') == expected

def test_future_perfect_indicitive_usted_er():
    expected = "habrá bebido"
    assert Conjugator().conjugate('beber','future_perfect','indicitive','usted') == expected

def test_future_perfect_indicitive_nosotros_ir():
    expected = "habremos vivido"
    assert Conjugator().conjugate('vivir','future_perfect','indicitive','nosotros') == expected

def test_future_perfect_indicitive_vosotros_er():
    expected = "habréis bebido"
    assert Conjugator().conjugate('beber','future_perfect','indicitive','vosotros') == expected

def test_future_perfect_indicitive_ustedes_ir():
    expected = "habrán vivido"
    assert Conjugator().conjugate('vivir','future_perfect','indicitive','ustedes') == expected

# ------------------------------ Simple Conditional Conditional Tense ------------------------------- #

def test_simple_conditional_conditional_yo_ar():
    expected = "hablaría"
    assert Conjugator().conjugate('hablar','simple_conditional','conditional','yo') == expected

def test_simple_conditional_conditional_tu_ar():
    expected = "hablarías"
    assert Conjugator().conjugate('hablar','simple_conditional','conditional','tu') == expected

def test_simple_conditional_conditional_usted_ar():
    expected = "hablaría"
    assert Conjugator().conjugate('hablar','simple_conditional','conditional','usted') == expected

def test_simple_conditional_conditional_nosotros_ar():
    expected = "hablaríamos"
    assert Conjugator().conjugate('hablar','simple_conditional','conditional','nosotros') == expected

def test_simple_conditional_conditional_vosotros_ar():
    expected = "hablaríais"
    assert Conjugator().conjugate('hablar','simple_conditional','conditional','vosotros') == expected

def test_simple_conditional_conditional_ustedes_ar():
    expected = "hablarían"
    assert Conjugator().conjugate('hablar','simple_conditional','conditional','ustedes') == expected

def test_simple_conditional_conditional_yo_er():
    expected = "bebería"
    assert Conjugator().conjugate('beber','simple_conditional','conditional','yo') == expected

def test_simple_conditional_conditional_tu_ir():
    expected = "vivirías"
    assert Conjugator().conjugate('vivir','simple_conditional','conditional','tu') == expected

def test_simple_conditional_conditional_usted_er():
    expected = "bebería"
    assert Conjugator().conjugate('beber','simple_conditional','conditional','usted') == expected

def test_simple_conditional_conditional_nosotros_ir():
    expected = "viviríamos"
    assert Conjugator().conjugate('vivir','simple_conditional','conditional','nosotros') == expected

def test_simple_conditional_conditional_vosotros_er():
    expected = "beberíais"
    assert Conjugator().conjugate('beber','simple_conditional','conditional','vosotros') == expected

def test_simple_conditional_conditional_ustedes_ir():
    expected = "vivirían"
    assert Conjugator().conjugate('vivir','simple_conditional','conditional','ustedes') == expected

