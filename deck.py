# module to construct and utilise the deck of cards


from random import shuffle

cardSuits = ('club', 'diamond', 'heart', 'spade')

# fixed card ranks and corresponding hard values in a 2D tuple
cardRanksValues = (('2',2), ('3',3), ('4',4), ('5',5), ('6',6),
                   ('7',7), ('8',8), ('9',9), ('10',10),
                   ('J',10), ('Q',10), ('K',10), ('A',1))

class Card:
    ''' a card must have a suit, rank and value '''
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value
        self.dealt = False
        self.discard = False


class Deck:
    ''' creating a new deck must have a card for each suit & rank '''
    def __init__(self):
        self.cards=[]
        self.dealtCardCount = 0
        for suit in cardSuits:
            for index, value in cardRanksValues:
                self.cards.append(Card(suit,index,value))

    def shuffleDeck(self):
        shuffle(self.cards)

    ''' dealing a card means marking the first card as dealt
    and adding 1 to the number of dealt cards. The dealtCardCount
    is used as the index of the card to be dealt next'''
    # will need to add a location to card, i.e. player hand, dealer hand
    # when those objects exist
    def deal(self):
        self.cards[self.dealtCardCount].dealt = True
        self.dealtCardCount = self.dealtCardCount + 1
        # self.cards[].position = player/dealer (parameter)


