from junction import Junction
from position import Position

class Graph():
    def __init__(self, start, finish, maze):
        self.start = start
        self.finish = finish
        self.maze = maze
        self.graph = []

        self.create_graph()

    def create_graph(self):
        for row in range(self.maze.get_rows()):
            self.graph.append([])
            for column in range(self.maze.get_columns()):
                if self.maze.get_board()[row][column].is_blocked():
                    self.graph[row].append(None)
                else:
                    current_junction = Junction(Position(row, column))
                    self.graph[row].append(current_junction)
                    self.update_junctions(current_junction)


    def update_junctions(self, current_junction):
        position = current_junction.get_position()

        upper_junction = self.get_junction_relative_to_position(position, 1, 0)
        left_junction = self.get_junction_relative_to_position(position, 0, -1)

        if upper_junction is not None:
            current_junction.set_up(upper_junction)
            upper_junction.set_down(current_junction)

        if left_junction is not None:
            current_junction.set_left(left_junction)
            left_junction.set_right(current_junction)

    def get_junction_relative_to_position(self, position, row_offset, column_offset):
        try:
            return self.graph[position.get_row()+row_offset][position.get_column()+column_offset]
        except:
            return None

    def __str__(self):
        display = ""
        for row in self.graph:
            for node in row:
                if node is not None:
                    display += '+'
                else:
                    display += ' '
            display += '\n'
        return display



