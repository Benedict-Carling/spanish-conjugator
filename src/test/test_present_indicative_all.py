import spanishconjugator
from spanishconjugator.SpanishConjugator import Conjugator

def test_present_indicative_ar():
	# expected = {"el/ella/usted": "habla", "ellos/ellas/ustedes": "hablan", "tu": "hablas", "vosotros": "habláis", "yo": "hablo", "nosotros": "hablamos"}
	expected_el = "habla"
	expected_ellos = "hablan"
	expected_tu = "hablas"
	expected_yo = "hablo"
	expected_nos = "hablamos"
	assert Conjugator().conjugate('hablar','present','indicative')["yo"] == expected_yo
	assert Conjugator().conjugate('hablar','present','indicative')["el/ella/usted"] == expected_el
	assert Conjugator().conjugate('hablar','present','indicative')["ellos/ellas/ustedes"] == expected_ellos
	assert Conjugator().conjugate('hablar','present','indicative')["tu"] == expected_tu
	assert Conjugator().conjugate('hablar','present','indicative')["nosotros"] == expected_nos



