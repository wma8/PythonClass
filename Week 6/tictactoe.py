# Add imports and other changes necessary to implement a simple game of Tic Tac
# Toe (https://en.wikipedia.org/wiki/Tic-tac-toe).
#
# In particular, you'll want to add several members and maybe some methods to
# the two classes below.

class TicTacToeGame:
    """Basic game logic.
    
    This class encapsulates game logic, separate from UI concerns. In other
    words, this class controls how the game (Tic Tac Toe) is played. In
    understands the rules of the game, whose turn it is, how to tell if the game
    is over, and so on.
    
    There are (at least) two benefits to separating this from the UI. First, you
    can test the logic separately, without having to write a UI. You could even
    write this class in an environment like Jupyter where Tkinter doesn't work.
    Second, there's the usual benefit to encapsulating or abstracting logic in a
    class. Suppose you need to change the internal representation of your game
    (maybe to support a new feature like undoing moves or a bigger board size,
    or maybe just to use a more efficient or more advantageous data format). You
    can change the internals of this class, and as long as the class's outwards
    facing interface doesn't change, you won't need to change the UI.
    """
    def __init__(self):
        pass

    def get(self, x, y):
        pass  # Return "X", "O", or " ".

    def currPlayer(self):
        pass  # Return "X" or "O"

    # If the specified move is valid, apply it (so after this call, get(x, y)
    # will return the correct mark and currPlayer() returns the other player).
    # If the specified move is invalid, raise ValueError.
    def move(self, x, y):
        pass

    def isGameOver(self):
        pass  # Self-explanatory


class TicTacToeUI:
    """Game UI.
    
    Implement a Tic Tac Toe game UI using Tkinter. Hints: first, add components
    necessary to draw the board. Test your draw function by hard-coding a few
    game moves in the constructor of this class (so make calls like
    self.game.move(1,1) directly from the constructor) and make sure the board
    is draw correctly. Then, add handlers to call methods on self.game in
    response to user inputs.
    """
    def __init__(self, *args):
        self.game = TicTacToeGame()
        # set up window, UI widgets, callbacks, etc.
        pass

    # Private members like callbacks and helper functions

def main():
    TicTacToeUI()  # Start a game

if __name__ == '__main__':
    main()
