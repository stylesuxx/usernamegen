from nose.tools import assert_equal, raises
from generator import Formatter
from generator import Generator
import re


class TestGenerator:

    @raises(Exception)
    def test_raise_exception_without_formatter(self):
        minLength = 8
        generator = Generator.Generator(words, 3, minLength)
        string = generator.getString()

    def test_check_min_length(self):
        minLength = 8
        words = ['foo', 'foobar', 'foobarbla', 'foobarblafasel']
        formatters = [{'format': Formatter.Join().format, 'weight': 2}]
        generator = Generator.Generator(words, 3, minLength)
        generator.setFormatters(formatters)
        string = generator.getString()

        assert len(string) >= 8
