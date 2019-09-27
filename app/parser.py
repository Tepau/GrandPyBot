import io


class Parser:
    '''Class that parses a string to retrieve a part'''

    def __init__(self):
        self.wordslist = \
            [line.strip() for line in io.open('app/static/stopwords.txt', encoding="utf8")]

    @staticmethod
    def drop_if_not_alpha(sentence):
        # Removes elements of a string that are not letters
        for letter in sentence:
            if not letter.isalpha():
                if letter != " ":
                    sentence = sentence.replace(letter, " ")
        return sentence

    def clean_sentence(self, sentence):
        # Returns words that are not in the file
        list_sentence = self.drop_if_not_alpha(sentence).split(" ")
        list_sentence = [word.lower() for word in list_sentence if len(word) > 0]
        for word in list_sentence:
            for words in self.wordslist:
                list_sentence = [i for i in list_sentence if i != words]

        return " ".join(list_sentence)


if __name__ == '__main__':
    app = Parser()
    print(app.clean_sentence("connais tu l'adresse de l'Esperance reuilly paris"))

