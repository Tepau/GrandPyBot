# coding: utf8
from app.wiki import WikipediaInformation
from app.geocode import GoogleMap
from app.parser import Parser


google_replace = [ {'address_components': [ {'long_name': '7', 'short_name': '7', 'types': [ 'street_number' ]},
                                          {'long_name': 'Cité Paradis', 'short_name': 'Cité Paradis',
                                           'types': [ 'route' ]}, {'long_name': 'Paris', 'short_name': 'Paris',
                                                                   'types': [ 'locality', 'political' ]},
                                          {'long_name': 'Arrondissement de Paris',
                                           'short_name': 'Arrondissement de Paris',
                                           'types': [ 'administrative_area_level_2', 'political' ]},
                                          {'long_name': 'Île-de-France', 'short_name': 'Île-de-France',
                                           'types': [ 'administrative_area_level_1', 'political' ]},
                                          {'long_name': 'France', 'short_name': 'FR',
                                           'types': [ 'country', 'political' ]},
                                          {'long_name': '75010', 'short_name': '75010', 'types': [ 'postal_code' ]} ],
                  'formatted_address': '7 Cité Paradis, 75010 Paris, France',
                  'geometry': {'location': {'lat': 48.8748465, 'lng': 2.3504873}, 'location_type': 'ROOFTOP',
                               'viewport': {'northeast': {'lat': 48.8761954802915, 'lng': 2.351836280291502},
                                            'southwest': {'lat': 48.8734975197085, 'lng': 2.349138319708498}}},
                  'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8',
                  'plus_code': {'compound_code': 'V9F2+W5 Paris, France', 'global_code': '8FW4V9F2+W5'},
                  'types': [ 'establishment', 'point_of_interest' ]} ]


def test_wiki(monkeypatch):
    """ Test function 'summary_informations' with Boulevard Carnot, Paris, France """

    result = "Le boulevard Carnot est une voie située dans le quartier du Bel-Air dans le 12e arrondissement de " \
             "Paris.   Le boulevard Carnot est desservi par la ligne   à la station Porte de Vincennes, ainsi que par " \
             "les lignes de bus RATP  29 56 86.   Cette avenue doit son nom au général Lazare Carnot, « général, " \
             "homme d'État et savant français », membre de la Convention nationale, surnommé l'« organisateur de la " \
             "victoire de 1793 » ou « le grand Carnot »."

    remplace = "Le boulevard Carnot est une voie située dans le quartier du Bel-Air dans le 12e arrondissement de " \
               "Paris. == Situation et accès == Le boulevard Carnot est desservi par la ligne   à la station Porte " \
               "de Vincennes, ainsi que par les lignes de bus RATP  29 56 86. == Origine du nom == Cette avenue " \
               "doit son nom au général Lazare Carnot, « général, homme d'État et savant français », membre de la " \
               "Convention nationale, surnommé l'« organisateur de la victoire de 1793 » ou « le grand Carnot »."

    def mock_summary(content, sentences):
        return remplace

    monkeypatch.setattr("app.wiki.wikipedia.summary", mock_summary)
    api = WikipediaInformation('Boulevard Carnot, Paris, France')
    assert api.summary_informations() == result


def test_find_location(monkeypatch):
    """ test function 'findLocation' with Openclassrooms Paris """

    result_location = (48.8748465, 2.3504873)

    def mockreturn(position, test):
        return google_replace

    monkeypatch.setattr("app.geocode.googlemaps.Client.geocode", mockreturn)
    api = GoogleMap()
    assert api.find_location('Openclassrooms Paris') == result_location


def test_find_adress(monkeypatch):
    """ test function 'find_adress' with Openclassrooms Paris """

    result_adress = "7 Cité Paradis, 75010 Paris, France"

    def mockreturn(position, test):
        return google_replace

    monkeypatch.setattr('app.geocode.googlemaps.Client.geocode', mockreturn)
    api = GoogleMap()
    assert api.find_adress('Openclassrooms Paris') == result_adress


def test_wiki_search(monkeypatch):
    """ test function 'wiki_search' with Openclassrooms Paris """

    result_wiki_search = "Cité Paradis, Paris, France"

    def mockreturn(position, test):
        return google_replace

    monkeypatch.setattr('app.geocode.googlemaps.Client.geocode', mockreturn)
    api = GoogleMap()
    assert api.wiki_search('Openclassrooms Paris') == result_wiki_search


def test_clear_sentence():
    """ test my parser with an example """
    sentence = Parser().clean_sentence('est-ce que tu connais l\'adresse d\'openclassrooms paris ?')
    assert sentence == 'openclassrooms paris'
