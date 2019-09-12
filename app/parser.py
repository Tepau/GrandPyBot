import io


class Parser:
    '''Class that parses a string to retrieve a part'''

    def __init__(self):
        self.wordslist = \
            [line.strip() for line in io.open('stopwords.txt', encoding="utf8")]

    def dropIfNotAlpha(self, sentence):
        # Removes elements of a string that are not letters
        for letter in sentence:
            if not letter.isalpha():
                if letter != " ":
                    sentence = sentence.replace(letter, " ")
        return sentence

    def cleanSentence(self, sentence):
        # Returns words that are not in the file
        listSentence = self.dropIfNotAlpha(sentence).split(" ")
        listSentence = [word.lower() for word in listSentence if len(word) > 0]
        for word in listSentence:
            for words in self.wordslist:
                listSentence = [i for i in listSentence if i != words]

        return " ".join(listSentence)


if __name__ == '__main__':
    app = Parser()
    app.cleanSentence("Connais tu l'adresse d'openclassrooms paris ?")
