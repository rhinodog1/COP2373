import random

# Card class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# Deck class
class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
                 "Jack", "Queen", "King", "Ace"]

        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


# Deal initial hand
def deal_hand(deck):
    hand = []
    for _ in range(5):
        hand.append(deck.deal_card())
    return hand


# Display hand
def show_hand(hand):
    for i, card in enumerate(hand, start=1):
        print(f"{i}: {card}")


# Replace selected cards
def replace_cards(hand, deck, indices):
    for i in indices:
        hand[i] = deck.deal_card()
    return hand


# Main game function
def play_game():
    deck = Deck()
    hand = deal_hand(deck)

    print("\nYour initial hand:")
    show_hand(hand)

    user_input = input(
        "\nEnter card numbers to replace (example: 1, 3, 5) or press Enter to keep all: "
    ).strip()

    if user_input:
        indices = [int(x) - 1 for x in user_input.split(",")]

        hand = replace_cards(hand, deck, indices)

        print("\nYour new hand:")
        show_hand(hand)
    else:
        print("\nYou kept your original hand:")
        show_hand(hand)


# Run game
play_game()