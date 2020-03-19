from junction import Junction
from position import Position

class Graph():
    def __init__(self, start, finish, board):
        self.start = start
        self.finish = finish
        self.board = board
        self.graph = []

    def create_graph(self):
        for row in range(len(self.board.get_rows())):
            self.graph.append([])
            for column in range(len(self.board.get_columns())):
                if self.board[row][columns].is_blocked():
                    self.graph[row][column].append(None)
                else:
                    current_junction = Junction(Position(row, column))
                    self.graph[row][column].append(current_junction)
                    self.update_junctions(current_junction)


    def update_junctions(self, current_junction):

        upper_junction = self.get_junction_relative_to_position(position, 1, 0)
        left_junction = self.get_junction_relative_to_position(position, 0, -1)

        current_junction.set_up(upper_junction)
        current_junction.set_left(left_junction)
        upper_junction.set_down(current_junction)
        left_junction.set_right(current_junction)

    def get_junction_relative_to_position(self, position, row_offset, column_offset):
        try:
            return self.board[position.get_row()+row_offset][position.get_column()+column_offset]
        except:
            return None

    def __str__(self):
        counter = 0
        for row in self.graph:
            for node in row:
                if node is not None:
                    counter += 1
        return "number of nodes: {0}".format(counter)



