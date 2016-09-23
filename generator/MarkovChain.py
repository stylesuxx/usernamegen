import random


class MarkovChain:
    def __init__(self, words, size):
        self.size = size
        self.starts = map(lambda word: word[:self.size], words)
        self.lookup = self._buildLookupTable(words)

    def _buildLookupTable(self, words):
        lookup = {}
        for word in words:
            for key, val in self._tuples(word):
                if key in lookup:
                    lookup[key].append(val)
                else:
                    lookup[key] = [val]

        return lookup

    def _tuples(self, word):
        if len(word) < self.size - 1:
            return

        word = word + "\n"
        for i in range(len(word) - self.size):
            yield (word[i:i + self.size], word[i + self.size])

    def getWord(self):
        key = random.choice(self.starts)
        word = key
        try:
            next = random.choice(self.lookup[key])
            while next != "\n":
                word = word + next
                key = key[1:] + next
                next = random.choice(self.lookup[key])
        except KeyError:
            pass

        return word

'''
def main():
    import argparse
    words = []

    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, metavar='WORDLIST',
                        help='File to use as basis for generating the words')
    parser.add_argument('-p', type=int, dest='prev_num', default=3,
                        help='Number of previous letters to base chain on')
    parser.add_argument('-n', type=int, dest='n', default=5,
                        help='Amount of generated words')
    args = parser.parse_args()

    file = open(args.path)
    file.seek(0)
    data = file.read()
    words = data.split("\n")
    file.close()

    markov = MarkovChain(words, args.prev_num)
    for i in range(0, args.n):
        print markov.getWord()

if __name__ == '__main__':
    main()
'''
