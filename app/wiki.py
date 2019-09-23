import wikipedia
import re


class WikipediaInformation:
    # Class in charge of finding information from a wikipedia page

    def __init__(self, adress):
        self.adress = adress

    @staticmethod
    def remove_odd_index(list_to_sort):
        list_without_odd = []
        for element in list_to_sort:
            if list_to_sort.index(element) % 2 == 0:
                list_without_odd.append(element)
        list_to_string = " ".join(list_without_odd)
        return list_to_string

    def summary_informations(self):
        # Get the first three sentences of a wikipedia page
        wikipedia.set_lang("fr")
        regex = re.compile(r'[\n]')
        informations = wikipedia.summary(self.adress, sentences=3)
        informations = regex.sub("", informations)
        if informations.split("==") is not False:
            informations = self.remove_odd_index(informations.split("=="))
        return informations


if __name__ == '__main__':
    app = WikipediaInformation('Boulevard Carnot, Paris, France')
    print(app.summary_informations())

