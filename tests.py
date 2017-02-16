import unittest
import deck

class TestNewCard(unittest.TestCase):

    def testCardInit(self):
        self.card = deck.Card('heart','A',1, self)
        self.assertEqual(self.card.suit, 'heart')
        self.assertEqual(self.card.rank, 'A')
        self.assertEqual(self.card.value, 1)
        self.assertFalse(self.card.dealt)
        self.assertFalse(self.card.discarded)
        


class TestNewDeck(unittest.TestCase):

    def setUp(self):
        self.deck1 = deck.Deck()

    def testDeckLength(self):
        self.assertEqual(len(self.deck1.cards), 52)

    def testCardSuits(self):
        self.assertEqual(self.deck1.cards[0].suit, 'club')
        self.assertEqual(self.deck1.cards[1].suit, 'club')
        self.assertEqual(self.deck1.cards[2].suit, 'club')
        self.assertEqual(self.deck1.cards[3].suit, 'club')
        self.assertEqual(self.deck1.cards[4].suit, 'club')
        self.assertEqual(self.deck1.cards[5].suit, 'club')
        self.assertEqual(self.deck1.cards[6].suit, 'club')
        self.assertEqual(self.deck1.cards[7].suit, 'club')
        self.assertEqual(self.deck1.cards[8].suit, 'club')
        self.assertEqual(self.deck1.cards[9].suit, 'club')
        self.assertEqual(self.deck1.cards[10].suit, 'club')
        self.assertEqual(self.deck1.cards[11].suit, 'club')
        self.assertEqual(self.deck1.cards[12].suit, 'club')
        self.assertEqual(self.deck1.cards[13].suit, 'diamond')
        self.assertEqual(self.deck1.cards[14].suit, 'diamond')
        self.assertEqual(self.deck1.cards[15].suit, 'diamond')
        self.assertEqual(self.deck1.cards[16].suit, 'diamond')
        self.assertEqual(self.deck1.cards[17].suit, 'diamond')
        self.assertEqual(self.deck1.cards[18].suit, 'diamond')
        self.assertEqual(self.deck1.cards[19].suit, 'diamond')
        self.assertEqual(self.deck1.cards[20].suit, 'diamond')
        self.assertEqual(self.deck1.cards[21].suit, 'diamond')
        self.assertEqual(self.deck1.cards[22].suit, 'diamond')
        self.assertEqual(self.deck1.cards[23].suit, 'diamond')
        self.assertEqual(self.deck1.cards[24].suit, 'diamond')
        self.assertEqual(self.deck1.cards[25].suit, 'diamond')
        self.assertEqual(self.deck1.cards[26].suit, 'heart')
        self.assertEqual(self.deck1.cards[27].suit, 'heart')
        self.assertEqual(self.deck1.cards[28].suit, 'heart')
        self.assertEqual(self.deck1.cards[29].suit, 'heart')
        self.assertEqual(self.deck1.cards[30].suit, 'heart')
        self.assertEqual(self.deck1.cards[31].suit, 'heart')
        self.assertEqual(self.deck1.cards[32].suit, 'heart')
        self.assertEqual(self.deck1.cards[33].suit, 'heart')
        self.assertEqual(self.deck1.cards[34].suit, 'heart')
        self.assertEqual(self.deck1.cards[35].suit, 'heart')
        self.assertEqual(self.deck1.cards[36].suit, 'heart')
        self.assertEqual(self.deck1.cards[37].suit, 'heart')
        self.assertEqual(self.deck1.cards[38].suit, 'heart')
        self.assertEqual(self.deck1.cards[39].suit, 'spade')
        self.assertEqual(self.deck1.cards[40].suit, 'spade')
        self.assertEqual(self.deck1.cards[41].suit, 'spade')
        self.assertEqual(self.deck1.cards[42].suit, 'spade')
        self.assertEqual(self.deck1.cards[43].suit, 'spade')
        self.assertEqual(self.deck1.cards[44].suit, 'spade')
        self.assertEqual(self.deck1.cards[45].suit, 'spade')
        self.assertEqual(self.deck1.cards[46].suit, 'spade')
        self.assertEqual(self.deck1.cards[47].suit, 'spade')
        self.assertEqual(self.deck1.cards[48].suit, 'spade')
        self.assertEqual(self.deck1.cards[49].suit, 'spade')
        self.assertEqual(self.deck1.cards[50].suit, 'spade')
        self.assertEqual(self.deck1.cards[51].suit, 'spade')


    def testCardRanks(self):
        self.assertEqual(self.deck1.cards[0].rank, '2')
        self.assertEqual(self.deck1.cards[1].rank, '3')
        self.assertEqual(self.deck1.cards[2].rank, '4')
        self.assertEqual(self.deck1.cards[3].rank, '5')
        self.assertEqual(self.deck1.cards[4].rank, '6')
        self.assertEqual(self.deck1.cards[5].rank, '7')
        self.assertEqual(self.deck1.cards[6].rank, '8')
        self.assertEqual(self.deck1.cards[7].rank, '9')
        self.assertEqual(self.deck1.cards[8].rank, '10')
        self.assertEqual(self.deck1.cards[9].rank, 'J')
        self.assertEqual(self.deck1.cards[10].rank, 'Q')
        self.assertEqual(self.deck1.cards[11].rank, 'K')
        self.assertEqual(self.deck1.cards[12].rank, 'A')
        self.assertEqual(self.deck1.cards[13].rank, '2')
        self.assertEqual(self.deck1.cards[14].rank, '3')
        self.assertEqual(self.deck1.cards[15].rank, '4')
        self.assertEqual(self.deck1.cards[16].rank, '5')
        self.assertEqual(self.deck1.cards[17].rank, '6')
        self.assertEqual(self.deck1.cards[18].rank, '7')
        self.assertEqual(self.deck1.cards[19].rank, '8')
        self.assertEqual(self.deck1.cards[20].rank, '9')
        self.assertEqual(self.deck1.cards[21].rank, '10')
        self.assertEqual(self.deck1.cards[22].rank, 'J')
        self.assertEqual(self.deck1.cards[23].rank, 'Q')
        self.assertEqual(self.deck1.cards[24].rank, 'K')
        self.assertEqual(self.deck1.cards[25].rank, 'A')
        self.assertEqual(self.deck1.cards[26].rank, '2')
        self.assertEqual(self.deck1.cards[27].rank, '3')
        self.assertEqual(self.deck1.cards[28].rank, '4')
        self.assertEqual(self.deck1.cards[29].rank, '5')
        self.assertEqual(self.deck1.cards[30].rank, '6')
        self.assertEqual(self.deck1.cards[31].rank, '7')
        self.assertEqual(self.deck1.cards[32].rank, '8')
        self.assertEqual(self.deck1.cards[33].rank, '9')
        self.assertEqual(self.deck1.cards[34].rank, '10')
        self.assertEqual(self.deck1.cards[35].rank, 'J')
        self.assertEqual(self.deck1.cards[36].rank, 'Q')
        self.assertEqual(self.deck1.cards[37].rank, 'K')
        self.assertEqual(self.deck1.cards[38].rank, 'A')
        self.assertEqual(self.deck1.cards[39].rank, '2')
        self.assertEqual(self.deck1.cards[40].rank, '3')
        self.assertEqual(self.deck1.cards[41].rank, '4')
        self.assertEqual(self.deck1.cards[42].rank, '5')
        self.assertEqual(self.deck1.cards[43].rank, '6')
        self.assertEqual(self.deck1.cards[44].rank, '7')
        self.assertEqual(self.deck1.cards[45].rank, '8')
        self.assertEqual(self.deck1.cards[46].rank, '9')
        self.assertEqual(self.deck1.cards[47].rank, '10')
        self.assertEqual(self.deck1.cards[48].rank, 'J')
        self.assertEqual(self.deck1.cards[49].rank, 'Q')
        self.assertEqual(self.deck1.cards[50].rank, 'K')
        self.assertEqual(self.deck1.cards[51].rank, 'A')


    def testCardValues(self):
        self.assertEqual(self.deck1.cards[0].value, 2)
        self.assertEqual(self.deck1.cards[1].value, 3)
        self.assertEqual(self.deck1.cards[2].value, 4)
        self.assertEqual(self.deck1.cards[3].value, 5)
        self.assertEqual(self.deck1.cards[4].value, 6)
        self.assertEqual(self.deck1.cards[5].value, 7)
        self.assertEqual(self.deck1.cards[6].value, 8)
        self.assertEqual(self.deck1.cards[7].value, 9)
        self.assertEqual(self.deck1.cards[8].value, 10)
        self.assertEqual(self.deck1.cards[9].value, 10)
        self.assertEqual(self.deck1.cards[10].value, 10)
        self.assertEqual(self.deck1.cards[11].value, 10)
        self.assertEqual(self.deck1.cards[12].value, 1)
        self.assertEqual(self.deck1.cards[13].value, 2)
        self.assertEqual(self.deck1.cards[14].value, 3)
        self.assertEqual(self.deck1.cards[15].value, 4)
        self.assertEqual(self.deck1.cards[16].value, 5)
        self.assertEqual(self.deck1.cards[17].value, 6)
        self.assertEqual(self.deck1.cards[18].value, 7)
        self.assertEqual(self.deck1.cards[19].value, 8)
        self.assertEqual(self.deck1.cards[20].value, 9)
        self.assertEqual(self.deck1.cards[21].value, 10)
        self.assertEqual(self.deck1.cards[22].value, 10)
        self.assertEqual(self.deck1.cards[23].value, 10)
        self.assertEqual(self.deck1.cards[24].value, 10)
        self.assertEqual(self.deck1.cards[25].value, 1)
        self.assertEqual(self.deck1.cards[26].value, 2)
        self.assertEqual(self.deck1.cards[27].value, 3)
        self.assertEqual(self.deck1.cards[28].value, 4)
        self.assertEqual(self.deck1.cards[29].value, 5)
        self.assertEqual(self.deck1.cards[30].value, 6)
        self.assertEqual(self.deck1.cards[31].value, 7)
        self.assertEqual(self.deck1.cards[32].value, 8)
        self.assertEqual(self.deck1.cards[33].value, 9)
        self.assertEqual(self.deck1.cards[34].value, 10)
        self.assertEqual(self.deck1.cards[35].value, 10)
        self.assertEqual(self.deck1.cards[36].value, 10)
        self.assertEqual(self.deck1.cards[37].value, 10)
        self.assertEqual(self.deck1.cards[38].value, 1)
        self.assertEqual(self.deck1.cards[39].value, 2)
        self.assertEqual(self.deck1.cards[40].value, 3)
        self.assertEqual(self.deck1.cards[41].value, 4)
        self.assertEqual(self.deck1.cards[42].value, 5)
        self.assertEqual(self.deck1.cards[43].value, 6)
        self.assertEqual(self.deck1.cards[44].value, 7)
        self.assertEqual(self.deck1.cards[45].value, 8)
        self.assertEqual(self.deck1.cards[46].value, 9)
        self.assertEqual(self.deck1.cards[47].value, 10)
        self.assertEqual(self.deck1.cards[48].value, 10)
        self.assertEqual(self.deck1.cards[49].value, 10)
        self.assertEqual(self.deck1.cards[50].value, 10)
        self.assertEqual(self.deck1.cards[51].value, 1)


class TestCardDeal(unittest.TestCase):

    def setUp(self):
        self.deck1 = deck.Deck()
        self.playerHand = deck.Hand('player')
        self.dealerHand = deck.Hand('dealer')


    def testCardDeal(self):
        # deal first card to player
        self.assertEqual(self.deck1.dealtCount, 0)
        self.deck1.deal(self.playerHand)
        self.assertEqual(len(self.playerHand.cards), 1)
        self.assertEqual(self.deck1.dealtCount, 1)
        self.assertTrue(self.deck1.cards[0].dealt)
        self.assertEqual(self.playerHand.cards[0].suit, 'club')
        self.assertEqual(self.playerHand.cards[0].rank, '2')
        self.assertEqual(self.playerHand.cards[0].value, 2)
        self.assertTrue(self.playerHand.cards[0].faceUp)
        
        self.deck1.deal(self.dealerHand)
        self.assertEqual(len(self.dealerHand.cards), 1)
        self.assertEqual(self.deck1.dealtCount, 2)
        self.assertTrue(self.deck1.cards[1].dealt)
        self.assertEqual(self.dealerHand.cards[0].suit, 'club')
        self.assertEqual(self.dealerHand.cards[0].rank, '3')
        self.assertEqual(self.dealerHand.cards[0].value, 3)
        self.assertTrue(self.dealerHand.cards[0].faceUp)
        # TODO add more, and test for exception when all 52 cards dealt and attempt to deal again
        # TODO exception if attempt to deal a card already dealt

    def testDealHand(self):
        self.deck1.deal(self.playerHand)
        self.assertEqual(self.deck1.dealtCount, 1)
        self.assertTrue(self.deck1.cards[0].dealt)
        self.assertEqual(len(self.playerHand.cards), 1)
        # check optional faceUp False for dealer
        self.deck1.deal(self.dealerHand, False)
        self.assertEqual(self.deck1.dealtCount, 2)
        self.assertTrue(self.deck1.cards[1].dealt)
        self.assertEqual(len(self.dealerHand.cards), 1)
        self.assertFalse(self.dealerHand.cards[0].faceUp)

class TestCardDiscard(unittest.TestCase):

    def setUp(self):
        self.deck1 = deck.Deck()
        self.card1 = self.deck1.cards[0]
        self.card2 = self.deck1.cards[1]

    def testdiscardCard(self):
        self.assertEqual(self.deck1.discardedCount, 0)
        self.assertFalse(self.card1.discarded)
        self.assertFalse(self.card2.discarded)
        self.card1.discard()
        self.assertEqual(self.deck1.discardedCount, 1)
        self.assertTrue(self.card1.discarded)
        self.card2.discard()
        self.assertEqual(self.deck1.discardedCount, 2)
        self.assertTrue(self.card2.discarded)
        # TODO exception test if attempt to discard a card already discarded
    

class TestHand(unittest.TestCase):

    def setUp(self):
        self.playerHand = deck.Hand('player')
        self.dealerHand = deck.Hand('dealer')

    def testHandInit(self):
        self.assertEqual(self.playerHand.type, 'player')
        self.assertEqual(self.dealerHand.type, 'dealer')
        self.assertEqual(len(self.playerHand.cards), 0)
        self.assertEqual(len(self.dealerHand.cards), 0)
        self.assertEqual(self.playerHand.hardTotal, 0)
        self.assertEqual(self.playerHand.softTotal, 0)
        self.assertEqual(self.dealerHand.hardTotal, 0)
        self.assertEqual(self.dealerHand.softTotal, 0)

class TestNewPlayer(unittest.TestCase):

    def setUp(self):
        self.player1 = deck.Player(0)

    def testPlayer1Init(self):
        self.assertEqual(self.player1.position, 0)
        self.assertEqual(len(self.player1.hand.cards), 0)
        self.assertEqual(self.player1.hand.type, 'player')

    def testPlayer2Init(self):
        self.player2 = deck.Player(1)
        self.assertEqual(self.player2.position, 1)
        self.assertEqual(len(self.player2.hand.cards), 0)
        self.assertEqual(self.player2.hand.type, 'player')
        

class TestDealer(unittest.TestCase):

    def setUp(self):
        self.dealer = deck.Dealer(1)

    def testDealerInit(self):
        self.assertEqual(len(self.dealer.hand.cards), 0)
        self.assertEqual(self.dealer.hand.type, 'dealer')
        self.assertEqual(self.dealer.position, 1)


class TestRound(unittest.TestCase):

    def testOnePlayerRound(self):
        self.round1 = deck.Round(1)
        self.assertEqual(len(self.round1.players), 1)
        self.assertEqual(self.round1.players[0].position, 0)
        self.assertEqual(self.round1.dealer.position, 1)
        self.assertEqual(len(self.round1.deck.cards), 52)

    def testTwoPlayerRound(self):
        self.round2 = deck.Round(2)
        self.assertEqual(len(self.round2.players), 2)
        self.assertEqual(self.round2.players[0].position, 0)
        self.assertEqual(self.round2.players[1].position, 1)
        self.assertEqual(self.round2.dealer.position, 2)

    def testOnePlayerDeal(self):
        self.round3 = deck.Round(1)
        self.round3.dealNewRound()
        self.assertEqual(len(self.round3.players[0].hand.cards), 2)
        self.assertTrue(self.round3.players[0].hand.cards[0].faceUp)
        self.assertTrue(self.round3.players[0].hand.cards[1].faceUp)
        self.assertEqual(len(self.round3.dealer.hand.cards), 2)
        self.assertTrue(self.round3.dealer.hand.cards[0].faceUp)
        # second dealer's card is not face up
        self.assertFalse(self.round3.dealer.hand.cards[1].faceUp)

    def testTwoPlayerDeal(self):
        self.round4 = deck.Round(2)
        self.round4.dealNewRound()
        self.assertEqual(len(self.round4.players[0].hand.cards), 2)
        self.assertTrue(self.round4.players[0].hand.cards[0].faceUp)
        self.assertTrue(self.round4.players[0].hand.cards[1].faceUp)
        
        self.assertEqual(len(self.round4.players[1].hand.cards), 2)
        self.assertTrue(self.round4.players[1].hand.cards[0].faceUp)
        self.assertTrue(self.round4.players[1].hand.cards[1].faceUp)
        
        self.assertEqual(len(self.round4.dealer.hand.cards), 2)
        self.assertTrue(self.round4.dealer.hand.cards[0].faceUp)
        # second dealer's card is not face up
        self.assertFalse(self.round4.dealer.hand.cards[1].faceUp)


    def testDealerReveal(self):
        self.round5 = deck.Round(2)
        self.round5.dealNewRound()
        self.assertFalse(self.round5.dealer.hand.cards[1].faceUp)
        self.round5.dealer.turnOverCard()
        self.assertTrue(self.round5.dealer.hand.cards[1].faceUp)



class TestHandTotals(unittest.TestCase):
    def setUp(self):
        self.playerHand = deck.Hand('player')
        self.deck1 = deck.Deck()

    def testHandTotals1(self):
        self.playerHand.cards.append(self.deck1.cards[0])
        self.playerHand.cards.append(self.deck1.cards[1])
        self.playerHand.valueHand()
        self.assertEqual(self.playerHand.hardTotal, 5)
        self.assertEqual(self.playerHand.softTotal, 5)
        self.playerHand.cards.append(self.deck1.cards[12])
        self.playerHand.valueHand()
        self.assertEqual(self.playerHand.hardTotal, 6)
        self.assertEqual(self.playerHand.softTotal, 16)
        self.playerHand.cards.append(self.deck1.cards[25])
        self.playerHand.valueHand()
        self.assertEqual(self.playerHand.hardTotal, 7)
        self.assertEqual(self.playerHand.softTotal, 17)
        self.playerHand.cards.append(self.deck1.cards[8])
        self.playerHand.valueHand()
        self.assertEqual(self.playerHand.hardTotal, 17)
        self.assertEqual(self.playerHand.softTotal, 17)
                                     
class TestPlayerHit(unittest.TestCase):
    def setUp(self):
        self.player1 = deck.Player(0)
        self.deck1 = deck.Deck()
        self.deck1.deal(self.player1.hand)
        self.deck1.deal(self.player1.hand)

    def testHit(self):
        self.player1.hit(self.deck1)
        self.assertEqual(len(self.player1.hand.cards), 3)
        self.assertEqual(self.player1.hand.hardTotal, 9)
        self.assertFalse(self.player1.isBust)
        self.player1.hit(self.deck1)
        self.assertEqual(len(self.player1.hand.cards), 4)
        self.assertEqual(self.player1.hand.hardTotal, 14)
        self.assertFalse(self.player1.isBust)
        self.player1.hit(self.deck1)
        self.assertEqual(len(self.player1.hand.cards), 5)
        self.assertEqual(self.player1.hand.hardTotal, 20)
        self.assertFalse(self.player1.isBust)
        self.player1.hit(self.deck1)
        self.assertEqual(len(self.player1.hand.cards), 6)
        self.assertEqual(self.player1.hand.hardTotal, 27)
        self.assertTrue(self.player1.isBust)
        
    #TODO create a new unit test with custom deck of cards, so correct cards to test
        # that player busts at exactly 22
    

class TestDisplayHand(unittest.TestCase):

    def setUp(self):
        self.player1 = deck.Player(0)
        self.deck1 = deck.Deck()
        self.deck1.deal(self.player1.hand)
        self.deck1.deal(self.player1.hand)


    def testDisplayHand(self):
        self.assertEqual(self.player1.hand.displayHand(),
                         " '2' of 'club' '3' of 'club' totalling: 5")

    #TODO custom deck so can test softHand total displays too
    
     
class TestCheckBlackjack(unittest.TestCase):

    def setUp(self):
        self.player1 = deck.Player(0)
        self.deck1 = deck.Deck()
        self.dealer = deck.Dealer(1)

    def testBlackjackTrue(self):
        # has 21 with two cards
        self.assertFalse(self.player1.hand.checkBlackjack())
        self.player1.hand.cards.append(self.deck1.cards[11])
        self.player1.hand.cards.append(self.deck1.cards[12])
        self.assertTrue(self.player1.hand.checkBlackjack())


    def testBlackjackFalse1(self):
        # has 21 with three cards
        self.assertFalse(self.player1.hand.checkBlackjack())
        self.player1.hand.cards.append(self.deck1.cards[11])
        self.player1.hand.cards.append(self.deck1.cards[3])
        self.player1.hand.cards.append(self.deck1.cards[4])
        self.assertFalse(self.player1.hand.checkBlackjack())

    def testBlackjackFalse2(self):
        # 2 cards but under 21
        self.assertFalse(self.player1.hand.checkBlackjack())
        self.player1.hand.cards.append(self.deck1.cards[11])
        self.player1.hand.cards.append(self.deck1.cards[10])
        self.assertFalse(self.player1.hand.checkBlackjack())

    def testBlackjackFalse3(self):
        # over 21
        self.assertFalse(self.player1.hand.checkBlackjack())
        self.player1.hand.cards.append(self.deck1.cards[11])
        self.player1.hand.cards.append(self.deck1.cards[4])
        self.player1.hand.cards.append(self.deck1.cards[10])
        self.assertFalse(self.player1.hand.checkBlackjack())
        
class TestResolveBlackjack(unittest.TestCase):
     def setUp(self):
        self.round = deck.Round(1)
        self.dealer = self.round.dealer
        self.player = self.round.players[0]

     def testDealerBlackjack(self):
        self.dealer.blackjack = True
        self.player.blackjack = False
        playerResult = self.round.resolveBlackjack(self.dealer, self.player)
        self.assertEqual(playerResult, 'loss')

     def testPlayerBlackjack(self):
        self.dealer.blackjack = False
        self.player.blackjack = True
        playerResult= self.round.resolveBlackjack(self.dealer, self.player)
        self.assertEqual(playerResult, 'win')

     def testBothBlackjack(self):
        self.dealer.blackjack = True
        self.player.blackjack = True
        playerResult = self.round.resolveBlackjack(self.dealer, self.player)
        self.assertEqual(playerResult, 'push')

     def testNeitherBlackjack(self):
        self.dealer.blackjack = False
        self.player.blackjack = False
        playerResult = self.round.resolveBlackjack(self.dealer, self.player)
        self.assertIsNone(playerResult)
 
            
            
        
    


if __name__ == '__main__':
    unittest.main()

    # test deck constructor - creates 52 card objects
    # with correct suits and ranks
    # 1 test card constructor - passes suit, rank & value
