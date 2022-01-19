# Table Tenis Scoring

## Rules

1. There are two players in the game.
2. Every player gets to serve twice in a row.
3. The first to 11 points is declared the winner.
4. If the points are tied at 10-10, a player then has to strive for a two-point lead to win the game.
5. If the scores are tied at 20-20, the first player to reach 21 point wins the game


Assume each player winning the point randomly. If the random functions returns even, then first player wins the
point, if it returns odd, the second player wins the point

Display the score and the winning player.

## Code

- Created a class `Game` to drive the game and display the results
- Method `start_game` will deal with the generation of score and identifying the winner
- Method `display_results` will display the end results once game is finished
