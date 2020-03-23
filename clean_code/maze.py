from cell import Cell
from exceptions import BoardIntegrityError

WALL = '1'


class Maze():
    """User-printable maze (walls and paths).
       converts user input into a maze."""
    def __init__(self, cells_per_row, maze_raw_form):
        self._board = []
        self._columns = cells_per_row
        self._rows = int(len(maze_raw_form) / self._columns)
        self._maze_raw_form = maze_raw_form

        self._create_board_cells()
        self._validate_maze_is_legal()

    def __str__(self):
        display = ""
        for row in self._board:
            for cell in row:
                display += str(cell)
            display += "\n"
        return display

    def get_rows(self):
        return self._rows

    def get_columns(self):
        return self._columns

    def get_board(self):
        return self._board

    def _create_board_cells(self):
        cell_index = 0
        for row in range(self._rows):
            self._board.append([])
            for _ in range(self._columns):
                current_cell = Cell()
                if self._maze_raw_form[cell_index] == WALL:
                    current_cell.set_blocked()

                cell_index += 1
                self._board[row].append(current_cell)
    
    def _validate_maze_is_legal(self):
        first_row = self._check_row_consistancy(0, True)
        last_row = self._check_row_consistancy(self._rows - 1, True)
        left_column = self._check_column_consistancy(0, True)
        right_column = self._check_column_consistancy(self._columns - 1, True)

        if not(first_row and last_row and left_column and right_column):
            raise BoardIntegrityError("not all borders are blocked")


    def _check_row_consistancy(self, row, desired_state):
        for cell in self._board[row]:
            if not cell.is_blocked() == desired_state:
                return False
        return True

    def _check_column_consistancy(self, column, desired_state):
        for row in self._board:
            if not row[column].is_blocked() == desired_state:
                return False
        return True

    def mark_cells_at_positions(self, positions):
        for position in positions:
            self._board[position.get_row()][position.get_column()].set_mark("+")

