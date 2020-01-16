"""
https://www.codewars.com/kata/57680d0128ed87c94f000bfd/train/python

Write a function that determines whether a string is a valid guess in a Boggle
board, as per the rules of Boggle.

A Boggle board is a 2D array of individual characters, e.g.:

[ ["I","L","A","W"],
  ["B","N","G","E"],
  ["I","U","A","O"],
  ["A","S","R","L"] ]

Valid guesses are strings which can be formed by connecting adjacent cells
(horizontally, vertically, or diagonally) without re-using any previously
used cells.

For example, in the above board "BINGO", "LINGO", and "ILNBIA" would all be
valid guesses, while "BUNGIE", "BINS", and "SINUS" would not.

Your function should take two arguments (a 2D array and a string) and return
true or false depending on whether the string is found in the array as per
Boggle rules.

Test cases will provide various array and string sizes (squared arrays up to
150x150 and strings up to 150 uppercase letters). You do not have to check
whether the string is a real word or not, only if it's a valid guess.
"""
from collections import defaultdict


class Board:
    def __init__(self, board: list):
        assert isinstance(board, list), "Game board must be a 2d matrix."
        assert isinstance(board[0], list), "Game board must be a 2d matrix."

        self.board = board

        # Board dimensions.
        self.width = len(board[0])
        self.height = len(board)

        # Board must be rectangular.
        for row in board:
            if len(row) != self.width:
                raise ValueError('Board must be rectangular!')

        # Provide reverse lookup to query if one or more of a letter exists.
        # keys=letter and values=list of coordinates -- 'A': [(1, 2), (2, 4)]
        self._lookup = defaultdict(list)
        self._init_lookup()

    def _init_lookup(self):
        """Initializes lookup dictionary."""
        for y, row in enumerate(self.board):
            for x, letter in enumerate(row):
                self._lookup[letter].append((x, y))

    def _get_positions(self, letter):
        """
        Returns a list of coordinates (x,y) for each time the letter appears
        in the game board.
        """
        return self._lookup[letter]

    def _get_letter(self, coord: tuple):
        """
        Helper method so we don't mess up coordinate/matrix indexing since
        (x, y) = board[y][x]
        """
        return self.board[coord[1]][coord[0]]

    def _is_valid(self, coord: tuple):
        """Returns true if coordinate is within board dimensions."""
        x = coord[0]
        y = coord[1]
        if x < 0 or x > self.width - 1:
            return False
        if y < 0 or y > self.height - 1:
            return False
        return True

    def _get_neighbors(self, coord: tuple):
        """Returns a list of neighboring coordinates."""
        neighbors = []
        for x_offset in (-1, 0, 1):
            for y_offset in (-1, 0, 1):
                point = (coord[0] + x_offset, coord[1] + y_offset)
                if not self._is_valid(point) or point == coord:
                    continue
                else:
                    neighbors.append(point)
        return neighbors

    def find_word(self, word):
        """Returns True if the word can be found in the Boggle game board."""
        letters = list(word)
        current_letter = letters.pop(0)

        # Initialize candidates with every occurence of the first letter.
        candidates = [[x] for x in self._get_positions(current_letter)]

        while letters:
            current_letter = letters.pop(0)

            next_candidates = []

            for solution in candidates:
                letter_choices = self._get_positions(current_letter)

                for neighbor in self._get_neighbors(solution[-1]):
                    if neighbor in letter_choices and neighbor not in solution:
                        next_candidates.append(solution + [neighbor])

            candidates = next_candidates

        return True if candidates else False

    def _format_board_string(self, board: list):
        """Returns a printable string of the board."""
        return '\n'.join(
            [' '.join(row) for row in board]
        )

    def __str__(self):
        return self._format_board_string(self.board)

    def _debug_print(self, coordinates: list):
        """
        Prints the board only showing coordinates in the list.

        Helpful when you want to debug potential solutions or next steps along
        the way...

        Example:
            self._debug_print([(0, 2), (1, 1), (2, 2)])

        Output:
            . . . .
            . A . .
            B . R .

        """
        template = [['.' for _ in range(self.width)] for _ in range(self.height)]
        for coord in coordinates:
            template[coord[1]][coord[0]] = self._get_letter(coord)
        print(self._format_board_string(template))


def find_word(board, word):
    board = Board(board)
    return board.find_word(word)

if __name__ == '__main__':
    # [Y][X]
    test = [
      ["E","A","R","A"],
      ["N","L","E","C"],
      ["I","A","I","S"],
      ["B","Y","O","R"]
    ]

    b = Board(test)
    b.find_word("RSCAREIOYBAILNEA")
