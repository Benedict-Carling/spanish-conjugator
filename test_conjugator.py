from src.spanishconjugator import Conjugator

def test_imperfect_imperitive_yo_ar():
    expected = "hablaba"
    assert Conjugator().conjugate('hablar','imperfect','imperitive','yo') == expected