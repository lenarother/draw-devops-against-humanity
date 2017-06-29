#!/usr/bin/env python

import csv
import sys
from io import BytesIO, StringIO

from draw.draw import clean_card, draw_cards, format_output, parse_data


def test_clean_empty_card():
    assert clean_card('') == ''


def test_clean_card():
    card = '"To increase our ____ we implemented ____________" \t'
    expected_card = 'To increase our _____ we implemented _____'
    assert clean_card(card) == expected_card


def test_parse_data():
    f = StringIO()
    if sys.version_info < (3, 0):
        f = BytesIO()

    csv.writer(f, delimiter=',').writerows([
        ['headline1'],
        ['headline2'],
        ['headline3'],
        ['sushi', 'We solved _____ error with _____.'],
        ['ninja', 'Deploying with _____']
    ])
    f.seek(0)
    black_cards, white_cards = parse_data(f)
    assert white_cards == ['sushi', 'ninja']
    assert black_cards == [
        'We solved _____ error with _____.', 'Deploying with _____']


def test_draw_cards_no_gap():
    black_cards = ['No gap card.']
    white_cards = ['a', 'b', 'c', 'd', 'e']
    result_black_card, result_white_cards = draw_cards(
        black_cards, white_cards)
    assert result_black_card == black_cards[0]
    assert result_white_cards == []


def test_draw_cards_many_gaps():
    black_cards = ['It was _____ with _____ in _____, after _____ and _____.']
    white_cards = ['a', 'b', 'c', 'd', 'e']
    result_black_card, result_white_cards = draw_cards(
        black_cards, white_cards)
    assert result_black_card == black_cards[0]
    assert sorted(result_white_cards) == white_cards


def test_format_output():
    black_card = 'I use _____ after _____, but only befor _____.'
    white_cards = ['eggs', 'backon', 'bar']
    assert format_output(black_card, white_cards) == (
        'I use [eggs] after [backon], but only befor [bar].')
