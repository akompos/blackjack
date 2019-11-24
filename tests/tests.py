from main import Deck
import unittest

class TestBuildDeck(unittest.TestCase):
    def test_deck_has_52_cards(self):
        test_deck = Deck()
        self.assertEqual(len(test_deck.cards), 52)


if __name__ == '__main__':
    unittest.main()

