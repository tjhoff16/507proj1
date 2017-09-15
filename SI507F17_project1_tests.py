# Do not change import statements.
import unittest
from SI507F17_project1_cards import *

# Write your unit tests to test the cards code here.
# You should test to ensure that everything explained in the code description
#file works as that file says.
# If you have correctly written the tests, at least 3 tests should fail.
#If more than 3 tests fail, it should be because multiple of the test methods
#address the same problem in the code.
# You may write as many TestSuite subclasses as you like, but you should try
#to make these tests well-organized and easy to read the output.
# You should invoke the tests with verbosity=2 (make sure you invoke them!)


###########

class Problem1(unittest.TestCase):
    def test_card_rank_suit(self):
        cd = Card(3, 9)
        c = Card(3, 11)
        self.assertEqual(cd.suit, "Spades")
        self.assertEqual(cd.rank, 9)
        self.assertEqual(c.rank, "Jack")

    def test_deck_init(self):
        d = Deck()
        self.assertEqual(len(d.cards), 52)
        self.assertEqual(type(d.cards), list)
        self.assertIsInstance(d, type(Deck()))
        self.assertEqual(type(print(d)), str)

    def test_pop_card(self):
        d = Deck()
        d.pop_card(2)
        self.assertEqual(len(d.cards), 51)

    def test_pop_card_2(self):
        d = Deck()
        cd = d.cards[2]
        d.pop_card(2)
        self.assertNotEqual(d.cards[2], cd)

    def test_shuffle(self):
        d = Deck()
        cd = d.cards[2]
        d.shuffle()
        self.assertNotEqual(d.cards[2], cd)

    def test_sort_cards(self):
        d = Deck()
        d.sort_cards()
        self.assertEqual(d.cards[0].suit, "Diamonds")
        self.assertEqual(d.cards[13].suit, "Clubs")
        self.assertEqual(d.cards[26].suit, "Hearts")
        self.assertEqual(d.cards[39].suit, "Spades")

    def test_deal_hand(self):
        d = Deck()
        hd = d.deal_hand(5)
        self.assertEqual(len(hd), 5)
        self.assertEqual(len(d.cards), 47)

    def test_war_game(self):
        pwg = play_war_game(testing=True)
        self.assertEqual(type(pwg), tuple)
        self.assertEqual(type(pwg[0]), str)
        self.assertEqual(type(pwg[2]), int)
        self.assertEqual(len(pwg), 3)
        self.assertTrue(pwg[0] in "Player1 Player2 Tie")

    def test_show_song(self):
        ss = show_song()
        sng = show_song("Thriller")
        self.assertIsInstance(ss, type(Song()))

unittest.main(verbosity=2)
