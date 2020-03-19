from cell import Cell
from position import Position

class BoardIntegrityError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        return self.message


class Maze():
    def __init__(self, cells_per_row, cell_desired_state, start, finish):
        self.board = []
        self.columns = cells_per_row
        self.rows = int(len(cell_desired_state) / self.columns)
        self.cell_desired_state = cell_desired_state
        self.start = start
        self.finish = finish

        self.create_board_cells()
        self.is_maze_legal()

    def __str__(self):
        for row in self.board:
            for cell in row:
                print(cell, end='')
            print()
        return ""

    def create_board_cells(self):
        cell_index = 0
        for row in range(self.rows):
            self.board.append([])
            for column in range(self.columns):
                current_cell = Cell()
                if self.cell_desired_state[cell_index] == "1":
                    current_cell.set_blocked(True)
                else:
                    current_cell.set_blocked(False)
                cell_index += 1
                self.board[row].append(current_cell)
    
    def is_maze_legal(self):
        first_row = self.check_row_consistancy(0, True)
        last_row = self.check_row_consistancy(len(self.board) - 1, True)
        left_column = self.check_column_consistancy(0, True)
        right_column = self.check_column_consistancy(len(self.board[0]) - 1, True)

        if not (first_row is True and last_row is True and left_column is True and right_column is True):
            raise BoardIntegrityError("not all borders are blocked")

    def check_row_consistancy(self, row, desired_state):
        for cell in self.board[row]:
            if not cell.is_blocked() == desired_state:
                return False
        return True

    def check_column_consistancy(self, column, desired_state):
        for row in self.board:
            if not row[column].is_blocked() == desired_state:
                return False
        return True

    def has_up(self, position):
        try:
            return not self.board[position.get_row()+1][position.get_column()].is_blocked()
        except:
            # when trying to check non-existing cell
            return False

    def has_down(self, position):
        try:
            return not self.board[position.get_row()-1][position.get_column()].is_blocked()
        except:
            # when trying to check non-existing cell
            return False

    def has_left(self, position):
        try:
            return not self.board[position.get_row()][position.get_column()-1].is_blocked()
        except:
            # when trying to check non-existing cell
            return False

    def has_right(self, position):
        try:
            return not self.board[position.get_row()][position.get_column()+1].is_blocked()
        except:
            # when trying to check non-existing cell
            return False

    def get_cell_at_position(self, position):
        return self.board[position.get_row()][position.get_column()]    

