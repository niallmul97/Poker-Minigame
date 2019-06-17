import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    #def faceCardSwitchCase(self, i):
        #faceCards = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
        #return faceCards.get(i, str(i))

    def show(self):
        if self.value == 11 or self.value == '11':
            print('J of {}'.format(self.suit))
        elif self.value == 12:
            print('Q of {}'.format(self.suit))
        elif self.value == 13:
            print('K of {}'.format(self.suit))
        elif self.value == 14:
            print('A of {}'.format(self.suit))
        else:
            print('{} of {}'.format(self.value, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.hand = []
        self.build()

    def build(self):
        for s in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
            for v in range(2,14):
                self.cards.append(Card(v,s))

    def show(self):
        for c in self.cards:
            c.show()

        for c in self.hand:
            c.show()

    def shuffle(self):
        random.shuffle(self.cards)

    def drawCard(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.finalHand = ''
        self.hand = []

    def draw(self, deck):
        for i in range(0,5):
            self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        print(self.name +"'s hand:")
        for card in self.hand:
            card.show()

    def faceCardSwitchCase(self, i):
        faceCards = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
        return faceCards.get(i, str(i))

    def scoreHand(self):
        handDict = {}
        suitDict = {}
        score = 0
        twoPairMod = 0
        fourOakMod = 1
        handList = [False] * 9
        finalHand = ''
        sortedHandByValue = sorted(self.hand, key=lambda card: card.value)
        sortedHandBySuit = sorted(self.hand, key=lambda card: card.suit)

        #adding all cards in hand to a dict in which the value is the key, aids in checking for pairs/three of a kind/four of a kind
        for i in sortedHandByValue:
            key = i.value
            if key in handDict:
                handDict[key] +=1
            else:
                handDict[key] = 1

        #adding all cards in hand to a dict in which the vsuit is the key, aids in checking for a flush
        for i in sortedHandBySuit:
            key = i.suit
            if key in suitDict:
                suitDict[key] += 1
            else:
                suitDict[key] = 1

        #finding of pairs
        for key in handDict.keys():

            #pair
            if len(handDict) == 4 and handDict.get(key) == 2:
                strPair = "Pair of {}'s".format(self.faceCardSwitchCase(int(key)))
                finalHand = finalHand + strPair
                handList[1] = True

        #3oak and Two Pair
        if len(handDict) == 3:
            for key in handDict.keys():
                if handDict.get(key) == 2:
                    twoPairMod +=2
                elif handDict.get(key) == 3:
                    twoPairMod +=1

            #Two Pair
            if twoPairMod % 2 == 0:
                strPair = "Two pair"
                finalHand = finalHand + strPair
                handList[2] = True

            #3oak
            else:
                strTrips = "Triple {}'s".format(self.faceCardSwitchCase(int(key)))
                finalHand = finalHand + strTrips
                handList[3] = True

        #4oak/Full House
        if len(handDict) == 2:
            for key in handDict.keys():
                if handDict.get(key) == 4:
                    fourOakMod +=1

            #4oak
            if fourOakMod & 2 == 0:
                strQuads = "Quad of {}'s".format(self.faceCardSwitchCase(int(key)))
                finalHand = finalHand + strQuads
                handList[7] = True

            #Full House
            else:
                strFH = 'Full House'
                finalHand = finalHand + strFH
                handList[6] = True

        #straight
        if len(handDict) == 5 and list(handDict.keys())[4] - list(handDict.keys())[0] == 4:
            print('Straight')
            handList[4] = True

        #Straight for Ace low
        if list(handDict.keys()) == [2, 3, 4, 5, 14]:
            print('Straight')
            handList[4] = True

        #flush
        if len(suitDict) == 1:
            print(' Flush')
            handList[5] = True

        #Straight flush
        if handList[4] == True and handList[5] == True:
            print('Straight Flush')
            handList[8] = True

        #Royal Flush
        if list(handDict.keys()) == [10, 11, 12, 13, 14] and len(suitDict) == 1:
            strRoyal = 'Royal Flush'
            finalHand = finalHand + strRoyal
            handList[9] = True

        #Hand Score
        for i in reversed(handList):
            if i == True:
                score = handList.index(i)
                break

        print(finalHand)
        print(score)

deck = Deck()
deck.shuffle()

p1 = Player('Player1')
p1.draw(deck)
p1.showHand()
print('')
p1.scoreHand()
print('')

p2 = Player('Player2')
p2.draw(deck)
p2.showHand()
print('')
p2.scoreHand()
print('')

#if p2.score == p1.score:
#    print("Draw!")
#elif p2.score > p1.score:
#    print("Player2 Wins!")
#else:
#    print("Player1 Wins!")

#card = deck.drawCard()
#card.show()
#deck.show()
