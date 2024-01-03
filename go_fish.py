import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def display(self):
        return f"  _______\n | {self.rank:^2}     |\n |   {self.suit}   |\n |     {self.rank:^2} |\n  -------"

class Deck:
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self):
        self.cards = [Card(rank, suit) for rank in self.RANKS for suit in self.SUITS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if self.cards:
            return self.cards.pop()
        else:
            return None

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def display_hand(self):
        print(f"{self.name}'s Hand:")
        for card in self.hand:
            print(card.display())

def go_fish_game():
    # Initialize deck and players
    deck = Deck()
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    players = [player1, player2]
    current_player_index = 0

    # Deal initial cards
    for _ in range(5):
        for player in players:
            player.add_card(deck.deal_card())

    # Main game loop
    while True:
        current_player = players[current_player_index]
        other_player = players[1 - current_player_index]

        # Display current player's hand
        current_player.display_hand()

        # Ask the other player for a rank
        rank_to_ask = random.choice(Deck.RANKS)
        print(f"\n{current_player.name}, do you have any {rank_to_ask}s?")
        input("Press Enter to continue...")

        # Check if the other player has the requested rank
        matching_cards = [card for card in other_player.hand if card.rank == rank_to_ask]

        if matching_cards:
            print(f"\n{other_player.name} gives {current_player.name} {len(matching_cards)} {rank_to_ask}s!")
            for card in matching_cards:
                current_player.add_card(card)
                other_player.hand.remove(card)
        else:
            print(f"\n{other_player.name} says 'Go Fish!'")
            drawn_card = deck.deal_card()
            if drawn_card:
                print(f"{current_player.name} draws a card:")
                print(drawn_card.display())
                current_player.add_card(drawn_card)
            else:
                print("The deck is empty!")

        # Check for sets of four cards in the current player's hand
        sets_found = []
        for rank in Deck.RANKS:
            if current_player.hand.count(Card(rank, '')) == 4:
                sets_found.append(rank)

        # Remove sets from the hand
        for rank in sets_found:
            current_player.hand = [card for card in current_player.hand if card.rank != rank]

        # Display sets found
        if sets_found:
            print(f"\n{current_player.name} books a set of {', '.join(sets_found)}s!")

        # Check for a winner
        if not deck.cards and all(len(player.hand) == 0 for player in players):
            print("\nGame Over! No more cards in the deck and both players are out of cards.")
            if len(player1.hand) > len(player2.hand):
                print(f"{player1.name} wins!")
            elif len(player1.hand) < len(player2.hand):
                print(f"{player2.name} wins!")
            else:
                print("It's a tie!")
            break

        # Switch to the other player's turn
        current_player_index = 1 - current_player_index

if __name__ == "__main__":
    go_fish_game()
