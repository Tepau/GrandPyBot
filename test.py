from app.wiki import Wiki
from app.geocode import GoogleMap
from app.parser import Parser

[{'address_components': [{'long_name': '26', 'short_name': '26', 'types': ['street_number']}, {'long_name': 'Boulevard Carnot', 'short_name': 'Boulevard Carnot', 'types': ['route']}, {'long_name': 'Pa
ris', 'short_name': 'Paris', 'types': ['locality', 'political']}, {'long_name': 'Arrondissement de Paris', 'short_name': 'Arrondissement de Paris', 'types': ['administrative_area_level_2', 'political'
]}, {'long_name': 'Île-de-France', 'short_name': 'Île-de-France', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}
, {'long_name': '75012', 'short_name': '75012', 'types': ['postal_code']}], 'formatted_address': '26 Boulevard Carnot, 75012 Paris, France', 'geometry': {'location': {'lat': 48.843112, 'lng': 2.412884
7}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 48.8444609802915, 'lng': 2.414233680291502}, 'southwest': {'lat': 48.8417630197085, 'lng': 2.411535719708498}}}, 'place_id': 'ChIJX1y3
RIhy5kcRJoLuiq87pTY', 'plus_code': {'compound_code': 'RCV7+65 Paris, France', 'global_code': '8FW4RCV7+65'}, 'types': ['establishment', 'point_of_interest']}]

def testWiki(monkeypatch):
    """ test wiki api with velodrome """

    result = ' '

    def mock_summary(content, sentences):
        return result

    monkeypatch.setattr('app.wiki.wikipedia.summary', mock_summary)
    api = Wiki('Velodrome')
    assert api.infos_sup() == result

def testFindLocation(monkeypatch):
    """ test gmap api with paris """

    resultLocation = (1, 2)

    def mockreturn(position):
        return resultLocation

    monkeypatch.setattr('app.geocode.GoogleMap.findLocation', mockreturn)
    api = GoogleMap('Openclassrooms Paris')
    assert api.findLocation() == resultLocation

def testFindAdress(monkeypatch):
    """ test gmap api with paris """

    resultAdress = "26 Boulevard Carnot, 75012 Paris, France"

    def mockreturn(position):
        return resultAdress

    monkeypatch.setattr('app.geocode.GoogleMap.findAdress', mockreturn)
    api = GoogleMap('Openclassrooms Paris')
    assert api.findAdress() == resultAdress

def testWikiSearch(monkeypatch):
    '''Test '''





def test_clearSentence():
    """ test my parser with an example """
    sentence = Parser().cleanSentence('est-ce que tu connais l\'adresse d\'openclassrooms paris ?')
    assert sentence == 'openclassrooms paris'