import pydealer

RUNS = 20
CARDS_IN_PLAY = 20

Results = {}


def check():
    deck = pydealer.Deck()
    deck.shuffle()
    hand = deck.deal(20)
    hand.sort()
