# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
prompt = ""
score = 0
dealer_val = ""
player_val = ""

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    #pos is given by top left corner
    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
    
            
    
# define hand class
class Hand:
    def __init__(self):
        self.cards=[]
        self.open=[]

    def __str__(self):
        result=""
        for card in self.cards:
            result+=str(card)+" "
        return result
    
    def add_card(self, card, open=True):
        self.cards.append(card)
        self.open.append(open)

    # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
    def get_value(self):
        value = 0
        i = 0
        for card in self.cards:
            value+=VALUES[card.get_rank()]
        for card in self.cards:
            if card.get_rank() == 'A' and value+10<22:
                value+=10
                break
        return value
            
    def busted(self):
        return self.get_value() > 21
    
    def draw(self, canvas, p):
        i = 0
        while i < len(self.cards) and i < 5:
            card = self.cards[i]
            
            if self.open[i]:
                card.draw(canvas, [p[0]+i*(CARD_SIZE[0]+20), p[1]])
            else:
                canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [p[0]+CARD_SIZE[0]/2+i*(CARD_SIZE[0]+20), p[1]+CARD_SIZE[1]/2],CARD_SIZE)
            i+=1
    
    def flip(self,index):
        self.open[index] = not self.open[index] 
    
# define deck class
class Deck:
    def __init__(self):
        self.cards=[]
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit,rank))
        random.shuffle(self.cards)

    # add cards back to deck and shuffle
    def shuffle(self):
        self.cards=[]
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit,rank))
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards)==0:
            for suit in SUITS:
                for rank in RANKS:
                    self.cards.append(Card(suit,rank))
            random.shuffle(self.cards)
        return self.cards.pop()


#define event handlers for buttons
def deal():
    global outcome,prompt,score,in_play,deck,player,dealer
    if in_play:
        score -= 1
    in_play = True
    deck = Deck()
    player = Hand()
    dealer = Hand()
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card(),False)
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    global dealer_val,player_val
    dealer_val = ""
    player_val = ""
    outcome = ""
    prompt = "Hit or Stand?"
    
def hit():
    global in_play,prompt,outcome,score
    global dealer_val,player_val
    if in_play:
        player.add_card(deck.deal_card())
        if player.busted():
            in_play = False
            prompt = "New deal?"
            outcome = "You went bust and lose."
            score -= 1
            dealer_val = str(dealer.get_value())
            player_val = str(player.get_value())
            dealer.flip(0)
        
def stand():
    global in_play,prompt,outcome,score
    global dealer_val,player_val
        
    if in_play:
        in_play = False
        dealer_value = dealer.get_value()
        while dealer_value < 17:
            dealer.add_card(deck.deal_card())
            dealer_value = dealer.get_value()
        if dealer_value >= player.get_value() and dealer_value <= 21:
            prompt = "New deal?"
            outcome = "You lose."
            score -= 1
        else:
            prompt = "New deal?"
            outcome = "You win."
            score += 1
        dealer.flip(0)
        dealer_val = str(dealer.get_value())
        player_val = str(player.get_value())
        
# draw handler    
def draw(canvas):
    global outcome,dealer,player
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack",[100,100],32,"aqua")
    canvas.draw_text("Dealer "+dealer_val,[75,175],24,"black")
    canvas.draw_text("Player "+player_val,[75,375],24,"black")
    canvas.draw_text(outcome,[230,175],24,"black")
    canvas.draw_text(prompt,[230,375],24,"black")
    canvas.draw_text("Score "+str(score),[400,100],24,"Black")
    dealer.draw(canvas,[75,200])
    player.draw(canvas,[75,400])
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# deal an initial hand
deal()

# get things rolling
frame.start()

# remember to review the gradic rubric