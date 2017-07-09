#!/usr/bin/env python

import csv
import os
import random
import re
from itertools import islice


CODE_DIR = os.path.split(__file__)[0]
DATA_PATH =  os.path.join(CODE_DIR, '..', 'data', 'devops_against_humanity.csv')


def clean_card(card):
    card = re.sub('"', '', card.strip())
    card = re.sub('____+', '_____', card)
    return card


def parse_data(csvfile):
    black_cards = []
    white_cards = []

    reader = csv.reader(csvfile, delimiter=',')
    for row in islice(reader, 3, None):
        if len(row) >= 2:
            white_card = clean_card(row[0])
            black_card = clean_card(row[1])
            if white_card:
                white_cards.append(white_card)
            if black_card:
                black_cards.append(black_card)

    return (black_cards, white_cards)


def draw_cards(black_cards, white_cards):
    random_black_card = random.choice(black_cards)
    gaps = random_black_card.count('_____')
    random_white_cards = random.sample(white_cards, gaps)
    return random_black_card, random_white_cards


def format_output(black_card, white_cards):
    for card in white_cards:
        black_card = black_card.replace('_____', '[{0}]'.format(card), 1)
    return black_card


def play_devops_agains_humanity():
    try:
        csvfile = open(DATA_PATH, encoding="utf-8")
    except TypeError:
        csvfile = open(DATA_PATH)

    black_cards, white_cards = parse_data(csvfile)
    random_black_card, random_white_cards = draw_cards(black_cards, white_cards)
    result = format_output(random_black_card, random_white_cards)
    print(result)


if __name__ == '__main__':
    play_devops_agains_humanity()
