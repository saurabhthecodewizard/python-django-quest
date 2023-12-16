import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2,
          'Three': 3,
          'Four': 4,
          'Five': 5,
          'Six': 6,
          'Seven': 7,
          'Eight': 8,
          'Nine': 9,
          'Ten': 10,
          'Jack': 11,
          'Queen': 12,
          'King': 13,
          'Ace': 14}

playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win(self):
        self.total += self.bet

    def lose(self):
        self.total -= self.bet


def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except TypeError:
            print("Sorry, please provide integer")
        else:
            if chips.bet > chips.total:
                print(f'Not enough chips!!! {chips.total}')
            else:
                break


def hit(deck, hand):
    hand.add(deck.deal())
    hand.adjust_for_aces()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Hit or Stand? Enter H or S: ')

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands Dealer's Turn")
            playing = False
        else:
            print("Sorry, I did not understand the input. Please enter an H or an S")
            continue
        break


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win()


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose()


def push(player, dealer):
    print("Dealer and Player tie! It's a push.")


while True:

    print('Welcome To BlackJack')
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add(deck.deal())
    player_hand.add(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add(deck.deal())
    dealer_hand.add(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    print(f'Total chips left: {player_chips.total}')

    new_game = input('Would you like to play another hand? (y/n)')

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thank you for playing')
        break
