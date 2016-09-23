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

        return formatter(words)

'''
def main():
    import argparse
    from Formatter import (Join, Underscore, Capitalize, CapitalizeExceptFirst,
                           AppendNumber, CapitalizeAppendNumber)

    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, metavar='WORDLIST',
                        help='File to use as basis for generating the words')
    parser.add_argument('-p', type=int, dest='prev_num', default=3,
                        help='Number of previous letters to base chain on')
    parser.add_argument('-n', type=int, dest='n', default=5,
                        help='Amount of generated words')
    parser.add_argument('-m', type=int, dest='min', default=8,
                        help='Minimum word length')
    args = parser.parse_args()

    formatters = [
        {'format': Join().format, 'weight': 2},
        {'format': Underscore().format, 'weight': 2},
        {'format': Capitalize().format, 'weight': 2},
        {'format': CapitalizeExceptFirst().format, 'weight': 2},
        {'format': AppendNumber().format, 'weight': 1},
        {'format': CapitalizeAppendNumber().format, 'weight': 1}
    ]

    file = open(path)
    file.seek(0)
    data = file.read()
    words = data.split("\n")
    file.close()

    generator = Generator(args.path, words, args.prev_num, args.min)
    generator.setFormatters(formatters)
    for i in range(0, args.n):
        print generator.getString()

if __name__ == '__main__':
    main()
'''
