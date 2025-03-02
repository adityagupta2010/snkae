import random

def roll_dice():
    """Simulates rolling a dice. Occasionally allows two dice for an extra challenge."""
    if random.random() < 0.2:  # 20% chance to roll two dice
        return random.randint(1, 6) + random.randint(1, 6)
    return random.randint(1, 6)

class SnakeAndLadder:
    def __init__(self, players):
        self.board_size = 100
        self.players = {player: 1 for player in players}
        self.snakes = {97: 78, 94: 54, 88: 24, 62: 18, 48: 26, 36: 6, 32: 10}
        self.ladders = {3: 22, 8: 30, 28: 76, 58: 77, 75: 96}
        print("Game initialized with players:", self.players)
    
    def move_player(self, player):
        roll = roll_dice()
        print(f"{player} rolled a {roll}")
        new_position = self.players[player] + roll
        print(f"{player} moves from {self.players[player]} to {new_position}")
        
        if new_position > self.board_size:
            print(f"{player} stays at {self.players[player]} (too high)")
            return
        
        if new_position in self.snakes:
            penalty = random.choice([2, 5, 10])
            print(f"Oh no! {player} hit a snake! Sliding down to {self.snakes[new_position]} with penalty -{penalty}.")
            new_position = max(1, self.snakes[new_position] - penalty)
        elif new_position in the ladders:
            print(f"Yay! {player} climbed a ladder to {self.ladders[new_position]}.")
            new_position = self.ladders[new_position]
        
        self.players[player] = new_position
        print(f"{player} is now at {new_position}")
    
    def play(self):
        while True:
            for player in self.players.keys():
                input(f"{player}'s turn! Press Enter to roll...")
                self.move_player(player)
                print(f"Current positions: {self.players}")
                if self.players[player] == self.board_size:
                    print(f"🎉 {player} wins the game! 🎉")
                    return

# Start Game
players = ["Player 1", "Player 2"]
game = SnakeAndLadder(players)
game.play()
