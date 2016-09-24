from abc import ABCMeta, abstractmethod, abstractproperty
import random


class Formatter:
    __metaclass__ = ABCMeta

    @abstractmethod
    def transform(self, words):
        raise NotImplementedError

    def format(self, words):
        return ''.join(self.transform(words))


class Join(Formatter):
    def transform(self, words):
        return words


class Underscore(Formatter):
    def transform(self, words):
        return list(''.join(l + '_' * (n < len(words) - 1)
                    for n, l in enumerate(words)))


class Capitalize(Formatter):
    def transform(self, words):
        return map(lambda word: word.capitalize(), words)


class CapitalizeExceptFirst(Formatter):
    def transform(self, words):
        words = Capitalize().transform(words)
        words[0] = words[0][:1].lower() + words[0][1:]
        return words


class AppendNumber(Formatter):
    def transform(self, words):
        last = words.pop()
        if len(last) is 4:
            words.append(str(random.randint(1600, 2300)))
        else:
            words.append(last)
            words.append(str(random.randint(0, 999)))

        return words


class CapitalizeAppendNumber(Formatter):
    def transform(self, words):
        words = Capitalize().transform(words)
        words = AppendNumber().transform(words)
        return words
