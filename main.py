import random
class Minesweeper(object):
    def __init__(self):
        self.squares = []
        self.board = []

    def play(self):
        print "Creating Board..."
        self.createBoard()

        print "Placing Mines..."
        self.placeMines()

        # Example mines set to test (Comment Line 12 and uncomment Line 15):
        # self.mines = set([(2, 6), (7, 0), (3, 3), (5, 6), (4, 5), (1, 6), (4, 3), (0, 3), (6, 5), (5, 3)])

        print "To quit, enter q\n"
        self.printBoard()

        self.moves = set()
        move = raw_input("\nYour Move: ")

        while True:
            if move.lower() == "q":
                break

            square = tuple([int(x) for x in move.split(" ")])

            if square in self.mines:
                print "Mine Detected. Game Over!"
                break

            self.moves.add(square)

            self.board[square[0]][square[1]] = self.countMines(square)
            self.printBoard()

            if self.isOver():
                print "\nYou Win!! Game Over!"
                break

            move = raw_input("\nYour Move: ")

    def isOver(self):
        remSquares = set(self.squares)-self.moves
        mineSquares = remSquares - self.mines
        if not mineSquares:
            return True
        return False


    def countMines(self, square):
        count = 0
        adjacentSides = [(square[0]-1, square[1]), (square[0]+1, square[1]), (square[0], square[1]-1),
                         (square[0], square[1]+1), (square[0]-1, square[1]-1), (square[0]-1, square[1]+1),
                         (square[0]+1, square[1]-1), (square[0]+1, square[1]+1)]
        # up, down, left, right, upLeft, upRight, downLeft, downRight

        for side in adjacentSides:
            if side in self.mines:
                count += 1

        if count == 0:
            return "X"
        return str(count)

    def printBoard(self):
        print "\n\t0\t1\t2\t3\t4\t5\t6\t7"
        for i in range(0, 8):
            print i,
            for j in range(0, 8):
                print "\t" + self.board[i][j],
            print ""

    def createBoard(self):
        for i in range(0, 8):
            row = []
            for j in range(0, 8):
                self.squares.append((i, j))
                row.append(" ")
            self.board.append(row)

    def placeMines(self):
        mines = random.sample(self.squares, 10)
        self.mines = set(tuple(mine) for mine in mines)

mine = Minesweeper()
mine.play()