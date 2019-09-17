import wikipedia


class Wiki:
    # Class in charge of finding information from a wikipedia page

    def __init__(self, adresse):
        self.adresse = adresse

    def infos_sup(self):
        # Get the first three sentences of a wikipedia page
        wikipedia.set_lang("fr")
        infos_sup = wikipedia.summary(self.adresse, sentences=3)
        return infos_sup


if __name__ == '__main__':
    app = Wiki('Boulevard Carnot, Paris, France')
    print(app.infos_sup())
