from cell import Cell
from exceptions import BoardIntegrityError
from functools import reduce
from numpy import reshape


class Maze():
    """User-printable maze (walls and paths).
       converts user input into a maze."""

    WALL_INDICATOR = '1'
    PATH_MARK = '+'

    def __init__(self, cells_per_row, maze_raw_form):
        self._board = []
        self._columns = cells_per_row
        self._rows = int(len(maze_raw_form) / self._columns)
        self._maze_raw_form = maze_raw_form

        self._create_board()
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

    def _create_board(self):
        cells = self._create_cells()
        self._board = reshape(cells, (self._rows, self._columns))
    
    def _create_cells(self):
        cells = []
        for indicator in self._maze_raw_form:
            current_cell = Cell()
            if indicator == Maze.WALL_INDICATOR:
                current_cell.set_blocked()
            cells.append(current_cell)

        return cells

    def _validate_maze_is_legal(self):
        first_row = self._check_row_consistancy(0)
        last_row = self._check_row_consistancy(self._rows - 1)
        left_column = self._check_column_consistancy(0)
        right_column = self._check_column_consistancy(self._columns - 1)

        if not(first_row and last_row and left_column and right_column):
            raise BoardIntegrityError("not all borders are blocked")


    def _check_row_consistancy(self, row):
        return reduce(lambda x, y: x and y, map(lambda cell: cell.is_blocked(), self._board[row]))



    def _check_column_consistancy(self, column):
        return reduce(lambda x, y: x and y, map(lambda row: row[column].is_blocked(), self._board))

    def mark_cells_at_positions(self, positions):
        for position in positions:
            self._board[position.get_row()][position.get_column()].set_mark(Maze.PATH_MARK)