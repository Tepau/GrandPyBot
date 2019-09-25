from app.constantes import key
import googlemaps


class GoogleMap:
    """class who recovers informations about
     a place through the api "googlemap\""""

    def __init__(self):
        self.gmaps = googlemaps.Client(key=['KEY'])


    def find_adress(self, search):
        # Get the full adress of a place
        geocode_result = self.gmaps.geocode(search)
        adress = geocode_result[0]["formatted_address"]
        return adress


    def find_location(self, search):
        # Get the longitude and latitude of a place
        geocode_result = self.gmaps.geocode(search)
        latitude = geocode_result[0]["geometry"]["location"]["lat"]
        longitude = geocode_result[0]["geometry"]["location"]["lng"]
        return (latitude, longitude)

    def wiki_search(self, search):
        # Get informations needed for a wikipedia research
        geocode_result = self.gmaps.geocode(search)
        location = geocode_result[0]["address_components"][1]["long_name"]
        ville = geocode_result[0]["address_components"][2]["long_name"]
        if len(geocode_result[0]["address_components"]) > 5:
            pays = geocode_result[0]["address_components"][5]["long_name"]
            return location + ", " + ville + ", " + pays
        return location + ", " + ville


if __name__ == '__main__':
    app = GoogleMap()
    print(app.find_adress('openclassrooms paris'))
    print(app.find_location('openclassrooms paris'))
    print(app.wiki_search('openclassrooms paris'))

