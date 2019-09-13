from constantes import key
import googlemaps


class GoogleMap:
    '''class who recovers informations about
     a place through the api "googlemap"'''

    def __init__(self, search):
        self.gmaps = googlemaps.Client(key=key)
        self.geocode_result = self.gmaps.geocode(search)

    def findAdress(self):
        # Get the full adress of a place
        adresse = self.geocode_result[0]["formatted_address"]
        return adresse

    def findLocation(self):
        # Get the longitude and latitude of a place
        lat = self.geocode_result[0]["geometry"]["location"]["lat"]
        lon = self.geocode_result[0]["geometry"]["location"]["lng"]
        return (lat, lon)

    def wikiSearch(self):
        # Get informations needed for a wikipedia search
        location = self.geocode_result[0]["address_components"][1]["long_name"]
        ville = self.geocode_result[0]["address_components"][2]["long_name"]
        pays = self.geocode_result[0]["address_components"][5]["long_name"]
        return location + ", " + ville + ", " + pays


if __name__ == '__main__':
    app = GoogleMap('esperance reuilly paris')
    print(app.findAdress())
    print(app.findLocation())
    print(app.wikiSearch())
