from cell import Cell

class Maze():
    def __init__(self, cells_per_row, cells_per_column, cell_desired_state):
        self.board = []
        self.cells_per_row = cells_per_row
        self.cells_per_column = cells_per_column
        self.cell_desired_state = cell_desired_state

        self.create_board_cells()


    def create_board_cells(self):
        cell_index = 0
        for row_num in range(self.cells_per_row):
            self.board.append([])
            for column_num in range(self.cells_per_column):
                current_cell = Cell()
                current_cell.set_blocked(self.cell_desired_state[cell_index])
                cell_index += 1
                self.board[row_num].append(current_cell)

    def print_maze_representation(self):
        row_content = ""
        for row in self.board:
            for cell in row:
                row_content += cell.get_cell_representation()

            print(row_content)
            row_content = ""
        