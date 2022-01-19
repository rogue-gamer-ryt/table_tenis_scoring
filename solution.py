import random


class Game:
    def __init__(self):
        """Dunder __init__ method"""
        self.score = [0, 0]

    def start_game(self):
        """Initiates a game, which will be played until a winner is declared"""
        while True:
            r = random.randint(0, 10)
            self.score[r % 2] += 1

            # If the score is 10 - 10 then a two point lead is needed for a player to win the game (so 11 - 10 won't
            # end the game)
            if max(self.score) >= 11 and abs(self.score[0] - self.score[1]) >= 2:
                return
            # End condition for whichever player first reaches the 21 point score
            elif max(self.score) == 21:
                return

    def display_results(self):
        """Display the end game results"""
        if max(self.score) > 0:
            print(f"Max Score: {max(self.score)}")
            print(f"Player {self.score.index(max(self.score)) + 1} Won")
            print(f"Final score board {self.score}")
        else:
            print("Please start the game first!")


if __name__ == "__main__":
    g = Game()
    g.start_game()
    g.display_results()
