# module to construct and utilise the deck of cards


from random import shuffle

cardSuits = ('club', 'diamond', 'heart', 'spade')

# fixed card ranks and corresponding hard values in a 2D tuple
# TODO make a named tuple so clearer labels
cardRanksValues = (('2',2), ('3',3), ('4',4), ('5',5), ('6',6),
                   ('7',7), ('8',8), ('9',9), ('10',10),
                   ('J',10), ('Q',10), ('K',10), ('A',1))

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
        #TODO exception if attempt to discard a card that's already discarded
        # and if all cards already discarded.

class Deck:
    ''' creating a new deck must have a card for each suit & rank '''
    def __init__(self):
        self.cards = []
        self.dealtCount = 0
        self.discardedCount = 0
        for suit in cardSuits:
            for index, value in cardRanksValues:
                self.cards.append(Card(suit,index,value, self))

    def shuffleDeck(self):
        shuffle(self.cards)

    ''' dealing a card means marking the first card as dealt
    and adding 1 to the number of dealt cards. The dealtCardCount
    is used as the index of the card to be dealt next'''

    def deal(self, hand, faceUp = True):
        # add the card to the hand's card list and increment deck's dealt counter
        hand.cards.append(self.cards[self.dealtCount])
        self.cards[self.dealtCount].faceUp = faceUp
        self.cards[self.dealtCount].dealt = True
        self.dealtCount = self.dealtCount + 1
        
        #TODO exception if no more cards to deal or attempt to deal a dealt card


class Hand:
    ''' for a player or dealer, the cards they have been dealt '''
    def __init__(self, type):
        # TODO see if the type is redundant if have separate player and dealer objects
        self.type = type
        self.cards = []
        self.hardTotal = 0
        self.softTotal = 0

    def valueHand(self):
        self.hardTotal = 0
        self.softTotal = 0
        for card in self.cards:
            self.hardTotal = self.hardTotal + card.value

            # as iterate through cards, check if any an Ace so can create a soft Total for hand
            if card.rank == 'A':
                self.hasAce = True

            else:
                self.hasAce= False

        # if Ace found when iterating, check if can have a soft Total, or would take over 21
        if self.hasAce == True:
            if self.hardTotal + 10 <= 21:
                self.softTotal = self.hardTotal + 10
        else:
            self.softTotal = self.hardTotal
            

            
        

class Player:
    ''' player class to contain the hand of cards, and the actions players are allowed'''

    # TODO likely will end up with table positions, when player initialises, will choose
    # from remaining positions. then when round starts, will be added to round in position order
    def __init__(self, position):
        self.position = position
        self.hand = Hand('player')

    def hit(self, deck):
        deck.deal(self.hand)
        self.hand.valueHand()
        if self.hand.hardTotal <= 21:
            self.isBust = False
        else:
            self.isBust = True
        

class Dealer:
    ''' dealer class to contain the hand of cards and the actions the dealer is allowed'''

    def __init__(self, position):
        self.position = position
        self.hand = Hand('dealer')

    def turnOverCard(self):
        self.hand.cards[1].faceUp = True

class Round:
    ''' A round has a number of players plus dealer'''

    def __init__(self, players):
        self.players = []

        # TODO change this, so players exist independent of round and get added into round based
        # on the player's position (which may change). So player's bankroll etc persist between
        # rounds
        self.numberOfPlayers = players
        # TODO each round getting a new deck, think about way of same deck persisting between rounds
        # i.e. only getting put back together and shuffled after 3 rounds
        self.deck = Deck()
        self.deck.shuffleDeck()

        # need to create a player object for the number of players
        # n will start at 0 and end at numberOfPlayers-1 (due to range behaviour)
        for n in range(self.numberOfPlayers):
            self.players.append(Player(n))

        # the dealer's position is equivalent to numberOfPlayers as players positions start at 0
        self.dealer = Dealer(self.numberOfPlayers)        

    def dealNewRound(self):
        # TODO position may be redundant, if iterate players in order in list
        # need to deal one card to each player in order, then to dealer, then to each player and dealer again

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


