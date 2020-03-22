from junction import Junction
from position import Position

class Graph():
    def __init__(self, start, finish, maze):
        self.start = start
        self.finish = finish
        self.maze = maze
        self.graph = []

        self.create_graph()
        
        self.set_start()
        self.set_finish()

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

        upper_junction = self.get_junction_relative_to_position(position, -1, 0)
        left_junction = self.get_junction_relative_to_position(position, 0, -1)

        if upper_junction is not None:
            current_junction.add_connection(upper_junction)
            upper_junction.add_connection(current_junction)

        if left_junction is not None:
            current_junction.add_connection(left_junction)
            left_junction.add_connection(current_junction)

    def get_junction_relative_to_position(self, position, row_offset, column_offset):
        try:
            return self.graph[position.get_row()+row_offset][position.get_column()+column_offset]
        except IndexError:
            return None

    def __str__(self):
        display = ""
        for row in self.graph:
            for node in row:
                if node is not None:
                    if node.is_start():
                        display += " s "
                    elif node.is_finish():
                        display += " f "
                    else:
                        display += " " + str(node.get_reference_number()) + " "
                else:
                    display += '   '
            display += '\n'
        return display

    def get_start(self):
        return self.start

    def get_finish(self):
        return self.finish

    def set_start(self):
        for row in self.graph:
            for node in row:
                if node is not None and node.get_position() == self.start:
                    node.set_is_start()
                    return

    def set_finish(self):
        for row in self.graph:
            for node in row:
                if node is not None and node.get_position() == self.finish:
                    node.set_is_finish()
                    return

    def get_finish_junction(self):
        return self.graph[self.finish.get_row()][self.finish.get_column()]

    def get_start_junction(self):
        return self.graph[self.start.get_row()][self.start.get_column()]

    def convert_junctions_to_positions(self, junctions):
        positions = []
        for junction in junctions:
            positions.append(junction.get_position())
        return positions



