from cell import Cell

class Maze():
    def __init__(self, cells_per_row, cell_desired_state):
        self.board = []
        self.row_length = cells_per_row
        self.column_length = int(len(cell_desired_state) / self.row_length)
        self.cell_desired_state = cell_desired_state

        self.create_board_cells()


    def create_board_cells(self):
        cell_index = 0
        for columns in range(self.column_length):
            self.board.append([])
            for rows in range(self.row_length):
                current_cell = Cell()
                if self.cell_desired_state[cell_index] == "1":
                    current_cell.set_blocked(True)
                else:
                    current_cell.set_blocked(False)
                cell_index += 1
                self.board[columns].append(current_cell)

    def print_maze_representation(self):
        row_content = ""
        for row in self.board:
            for cell in row:
                row_content += cell.get_cell_representation()

            print(row_content)
            row_content = ""
        