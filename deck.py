# module to construct and utilise the deck of cards


from random import shuffle

cardSuits = ('club', 'diamond', 'heart', 'spade')

# fixed card ranks and corresponding hard values in a 2D tuple
# TODO make a named tuple so clearer labels
cardRanksValues = (('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6),
                   ('7', 7), ('8', 8), ('9', 9), ('10', 10),
                   ('J', 10), ('Q', 10), ('K', 10), ('A', 1))


class Card:
    ''' a card must have a suit, rank and value '''
    def __init__(self, suit, rank, value, parent):
        # passing the parent Deck into the card so that parent-level
        # attributes (e.g. discardedCount) can be updated during
        # child-level functions (e.g. discard())
        self.parent = parent
        self.suit = suit
        self.rank = rank
        self.value = value
        self.dealt = False
        self.discarded = False

    def discard(self):
        self.discarded = True
        self.parent.discardedCount = self.parent.discardedCount + 1
        # TODO exception if attempt to discard a card that's already discarded
        # and if all cards already discarded.


class Deck:
    ''' creating a new deck must have a card for each suit & rank '''
    def __init__(self):
        self.cards = []
        self.dealtCount = 0
        self.discardedCount = 0
        for suit in cardSuits:
            for index, value in cardRanksValues:
                self.cards.append(Card(suit, index, value, self))

    def shuffleDeck(self):
        shuffle(self.cards)

    ''' dealing a card means marking the first card as dealt
    and adding 1 to the number of dealt cards. The dealtCardCount
    is used as the index of the card to be dealt next'''

    def deal(self, hand, faceUp=True):
        # add the card to the hand's card list and increment dealt counter
        hand.cards.append(self.cards[self.dealtCount])
        self.cards[self.dealtCount].faceUp = faceUp
        self.cards[self.dealtCount].dealt = True
        self.dealtCount = self.dealtCount + 1

        # TODO exception if no more cards to deal or deal a dealt card


class Hand:
    ''' for a player or dealer, the cards they have been dealt '''
    def __init__(self, type):
        # TODO is type redundant if separate player and dealer objects?
        self.type = type
        self.cards = []
        self.hardTotal = 0
        self.softTotal = 0

    def valueHand(self):
        self.hardTotal = 0
        self.softTotal = 0
        self.hasAce = False
        for card in self.cards:
            self.hardTotal = self.hardTotal + card.value

            # as iterate through cards, check if any an Ace
            # if so create a soft Total for hand
            if card.rank == 'A':
                self.hasAce = True
                # Note: no Else option as otherwise would override True
                # with false on next card!

        # if Ace found when iterating, check if can have a soft Total,
        # or would take over 21
        # if can have softTotal add 10 to hardTotal,
        # else softTotal and hardTotal are the same
        if self.hasAce and ((self.hardTotal + 10) <= 21):
                self.softTotal = self.hardTotal + 10
        else:
            self.softTotal = self.hardTotal

    def displayHand(self):
        self.valueHand()
        handDetails = ''
        for card in self.cards:
            handDetails = handDetails + " %r of %r" % (card.rank, card.suit)
        if self.hardTotal == self.softTotal:
            handDetails = handDetails + " totalling: %r" % self.hardTotal
        else:
            handDetails = handDetails + " totalling: %r / %r " % (
                self.hardTotal, self.softTotal)

        return handDetails

    def checkBlackjack(self):
        # Blackjack if two cards adding up to 21 (soft value as must have ace)
        self.valueHand()
        if len(self.cards) == 2 and self.softTotal == 21:
            return True
        else:
            return False


class Player:
    ''' player class to contain the hand of cards, and the actions allowed'''

    # TODO likely will end up with table positions, when player initialises,
    # will choose from remaining positions. then when round starts,
    # will be added to round in position order
    def __init__(self, position):
        self.position = position
        self.hand = Hand('player')
        self.blackjack = False

    # TODO the deal function is on the deck, so to get this to work needed
    # to pass the deck to the player object so the player can utilise it.
    # Seems weird, so probably wrong
    def hit(self, deck):
        deck.deal(self.hand)
        self.hand.valueHand()
        if self.hand.hardTotal <= 21:
            self.isBust = False
        else:
            self.isBust = True

    def playerChoice(self, round):
        playerTurn = True

        # value hand and end player's turn if 21 (Blackjack)
        # TODO how to test without having to initialise a round
        # (with shuffled deck!) -or separate shuffle from round init
        if self.hand.checkBlackjack():
            print("The player has" + self.hand.displayHand())
            print("The player has Blackjack")
            playerTurn = False
            self.blackjack = True
            return

        # otherwise, loop the "hit or stick" until player hits 21, busts or
        # sticks
        # TODO a way of testing this to ensure all paths through are as
        # expected for hard/soft totals
        else:
            self.hand.valueHand()
            while playerTurn:
                print("The player has" + self.hand.displayHand())
                playerAction = input("Hit (h) or stick (s)?")

                if playerAction.upper() == 'H':
                    self.hit(round.deck)
                    self.hand.valueHand()
                    print("The player now has" + self.hand.displayHand())
                    if self.hand.softTotal >= 21:
                        playerTurn = False
                elif playerAction.upper() == 'S':
                    print("Player's turn has ended")
                    playerTurn = False
                    return
                else:
                    # TODO better exception handling
                    print("Invalid input, try again")

        if self.isBust:
            print("The player has busted, clearing cards")
            for card in self.hand.cards:
                card.discard()


class Dealer:
    ''' dealer class to contain the hand of cards and the dealer actions'''

    def __init__(self, position):
        self.position = position
        self.hand = Hand('dealer')
        self.blackjack = False

    def turnOverCard(self):
        self.hand.cards[1].faceUp = True

    # TODO test
    def dealerInitialCard(self):
        # returns the details of the faceup card the dealer is showing
        return("The dealer is showing %r of %r" % (self.hand.cards[0].rank,
                                                   self.hand.cards[0].suit))

    # TODO test ("assertraises?")
    def dealerRevealCard(self):
        # reveals the dealer's hidden card
        self.turnOverCard()
        print ("The dealer has" + self.hand.displayHand())
        if self.hand.checkBlackjack:
            self.blackjack = True


class Round:
    ''' A round has a number of players plus dealer'''

    def __init__(self, players):
        self.players = []

        # TODO change this, so players exist independent of round and get
        # added into round based on the player's position (which may change).
        # So player's bankroll etc persist between rounds
        self.numberOfPlayers = players
        # TODO each round getting a new deck, think about way of same deck
        # persisting between rounds i.e. only getting put back together and
        # shuffled after 3 rounds
        self.deck = Deck()
        self.deck.shuffleDeck()

        # need to create a player object for the number of players
        # n will start at 0 and end at numberOfPlayers-1 (as how range works)
        for n in range(self.numberOfPlayers):
            self.players.append(Player(n))

        # the dealer's position is equivalent to numberOfPlayers as players
        # positions start at 0
        self.dealer = Dealer(self.numberOfPlayers)

    def dealNewRound(self):
        # TODO position may be redundant, if iterate players in order in list
        # need to deal one card to each player in order, then to dealer,
        # then to each player and dealer again

        # need to deal to everyone twice
        for i in range(2):

            # deal once to each player
            for n in range(len(self.players)):
                self.deck.deal(self.players[n].hand)

            # second card to dealer has to be facedown
            if i == 0:
                dealerCardFaceUp = True
            else:
                dealerCardFaceUp = False

            # deal to dealer, faceup based on whether first or second card
            self.deck.deal(self.dealer.hand, dealerCardFaceUp)

    def resolveBlackjack(self, dealer, player):
        # pass dealer and player and work out player's result

        if dealer.blackjack:
            if player.blackjack:
                return 'push'
            else:
                return 'loss'
        else:
            if player.blackjack:
                return 'win'
            else:
                return

    def checkTableBlackjack(self):
        # check dealer against each player and resolve blackjacks
        for player in self.players:
            player.result = self.resolveBlackjack(self.dealer, player)
            print ("player has %r" % player.result)

    # def dealerTurn(self):
    # if any player still standing need to:
    # check if player has blackjack, if so, if dealer doesn't have blackjack
    # then that player wins
    # if no blackjack, then dealer hits until gets to 17, or busts
    # if busts, all players win, if not then player > dealer wins,
    # player==dealer draw
    # player < dealer lose


def main():
    ''' script for the game'''

    # TODO add function to get number of players from input. Until then,
    # start with 2 players
    round1 = Round(2)
    round1.dealNewRound()

    # show dealer's card
    dealer = round1.dealer
    print(dealer.dealerInitialCard())
    # then iterate through each player giving hit or stick options
    for player in round1.players:
        player.playerChoice(round1)

    # when players turns are complete, dealer reveals second card
    dealer.dealerRevealCard()
    round1.checkTableBlackjack()

    # resolve blackjacks first
    # if dealer has blackjack, then all players lose unless they also have
    # blackjack else if player has blackjack they win
    # if player has blackjack, then if dealer has blackjack push, else
    # player wins then player's hand is discarded


if __name__ == "__main__":
    main()
