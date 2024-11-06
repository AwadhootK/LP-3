class NQueens:
    def __init__(self, n, x, y):
        self.n = n
        self.x = x
        self.y = y
        self.board = [['_' for j in range(n)] for i in range(n)]
        self.left_row = [0] * n
        self.lower_diagonal = [0] * (2 * n - 1)
        self.upper_diagonal = [0] * (2 * n - 1)

    def print_mat(self, mat):
        for row in mat:
            print(" ".join(map(str, row)))

    def solve(self, col):
        if col == self.n:
            print("Solution:")
            self.print_mat(self.board)
            return True  # Found one solution

        found_solution = False
        for row in range(self.n):
            if (self.left_row[row] == 0 and
                    self.lower_diagonal[row + col] == 0 and
                    self.upper_diagonal[self.n - 1 + col - row] == 0):
                # Place queen
                self.board[row][col] = 'Q'
                self.left_row[row] = 1
                self.lower_diagonal[row + col] = 1
                self.upper_diagonal[self.n - 1 + col - row] = 1

                # Recur to place next queen
                found_solution = self.solve(col + 1) or found_solution

                # Backtrack
                self.board[row][col] = '_'
                self.left_row[row] = 0
                self.lower_diagonal[row + col] = 0
                self.upper_diagonal[self.n - 1 + col - row] = 0

        return found_solution

    def place_first_queen(self):
        if self.x < 0 or self.x >= self.n or self.y < 0 or self.y >= self.n:
            print('Invalid coordinates of first queen')
            return

        if self.n in [2, 3]:  # Known unsolvable cases
            print("No solution exists for N =", self.n)
            return

        # Place the first queen at the provided coordinates
        self.board[self.x][self.y] = 'Q'

        # Mark the initial position of the first queen
        self.left_row[self.x] = 1
        self.lower_diagonal[self.x + self.y] = 1
        self.upper_diagonal[self.n - 1 + self.y - self.x] = 1

        # Start solving from the next column
        can_place = self.solve(1)
        if not can_place:
            print('Cannot place queens for given input coordinates')


# Usage
n = int(input('Enter number of queens: '))
x, y = map(int, input('Enter coordinates of 1st Queen: ').split())

n_queens_solver = NQueens(n, x, y)
n_queens_solver.place_first_queen()
