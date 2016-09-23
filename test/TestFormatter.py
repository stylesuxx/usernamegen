from nose.tools import assert_equal
from generator import Formatter
import re


class TestFormatter:
    def test_join(self):
        formatter = Formatter.Join()
        string = formatter.format(['foo', 'bar'])

        assert_equal(string, 'foobar')

    def test_underscore(self):
        formatter = Formatter.Underscore()
        string = formatter.format(['foo', 'bar'])

        assert_equal(string, 'foo_bar')

    def test_capitalize(self):
        formatter = Formatter.Capitalize()
        string = formatter.format(['foo', 'bar'])

        assert_equal(string, 'FooBar')

    def test_capitalize_except_first(self):
        formatter = Formatter.CapitalizeExceptFirst()
        string = formatter.format(['foo', 'bar'])

        assert_equal(string, 'fooBar')

    def test_append_number(self):
        formatter = Formatter.AppendNumber()

        string = formatter.format(['foo', 'bar', 'year'])
        assert re.match('^foobar\d{4}$', string)

        string = formatter.format(['foo', 'bar', 'asd'])
        assert re.match('^foobarasd\d{1,3}$', string)

    def test_capitalize_append_number(self):
        formatter = Formatter.CapitalizeAppendNumber()

        string = formatter.format(['foo', 'bar', 'year'])
        assert re.match('^FooBar\d{4}$', string)

        string = formatter.format(['foo', 'bar', 'asd'])
        assert re.match('^FooBarAsd\d{1,3}$', string)
