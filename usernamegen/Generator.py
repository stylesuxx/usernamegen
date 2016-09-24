from MarkovChain import MarkovChain
import random


class Generator():
    def __init__(self, words, size, min):
        self.size = size
        self.min = min
        self.formatters = []

        self.markov = MarkovChain(words, size)

    def getWords(self):
        words = []
        length = 0
        while length < self.min:
            word = self.markov.getWord()
            words.append(word)
            length += len(word)

        return words

    def setFormatters(self, formatters):
        self.formatters = []
        for i in range(0, len(formatters)):
            formatter = formatters[i]
            for j in range(0, formatter['weight']):
                self.formatters.append(formatter['format'])

    def getString(self):
        words = self.getWords()

        try:
            formatter = random.choice(self.formatters)
        except IndexError:
            raise Exception('At least one formatter needs to be provided')

        return formatter().format(words)
