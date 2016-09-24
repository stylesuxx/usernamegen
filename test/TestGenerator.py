from nose.tools import assert_equal, raises
import usernamegen
import re


class TestGenerator:

    @raises(Exception)
    def test_raise_exception_without_formatter(self):
        minLength = 8
        gen = usernamegen.Generator(words, 3, minLength)
        string = gen.getString()

    def test_check_min_length(self):
        minLength = 8
        words = ['f', 'foo', 'foobar', 'foobarbla', 'foobarblafasel']
        formatters = [{'format': usernamegen.Formatter.Join().format,
                      'weight': 2}]
        gen = usernamegen.Generator(words, 3, minLength)
        gen.setFormatters(formatters)
        string = gen.getString()

        assert len(string) >= 8
