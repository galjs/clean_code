from junction import Junction
from position import Position

class Graph():
    """Stores the junction structure in graph form 
       that a search algorithm can process."""
    def __init__(self, start, finish, maze):
        self._start = start
        self._finish = finish
        self._maze = maze
        self._graph = []

        self._create_graph()
        
        self._set_start()
        self._set_finish()

    def _create_graph(self):
        for row in range(self._maze.get_rows()):
            self._graph.append([])
            for column in range(self._maze.get_columns()):
                if self._maze.get_board()[row][column].is_blocked():
                    self._graph[row].append(None)
                else:
                    current_junction = Junction(Position(row, column))
                    self._graph[row].append(current_junction)
                    self._update_junctions(current_junction)



    def _update_junctions(self, current_junction):
        position = current_junction.get_position()

        upper_junction = self._get_junction_relative_to_position(position, -1, 0)
        left_junction = self._get_junction_relative_to_position(position, 0, -1)

        if upper_junction is not None:
            current_junction.add_connection(upper_junction)
            upper_junction.add_connection(current_junction)

        if left_junction is not None:
            current_junction.add_connection(left_junction)
            left_junction.add_connection(current_junction)

    def _get_junction_relative_to_position(self, position, row_offset, column_offset):
        try:
            return self._graph[position.get_row()+row_offset][position.get_column()+column_offset]
        except IndexError:
            return None


    def __str__(self):
        display = ""
        for row in self._graph:
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

    def _set_start(self):
        for row in self._graph:
            for node in row:
                if node is not None and node.get_position() == self._start:
                    node.set_is_start()
                    return

    def _set_finish(self):
        for row in self._graph:
            for node in row:
                if node is not None and node.get_position() == self._finish:
                    node.set_is_finish()
                    return

    def get_finish_junction(self):
        return self._graph[self._finish.get_row()][self._finish.get_column()]

    def get_start_junction(self):
        return self._graph[self._start.get_row()][self._start.get_column()]

    def convert_junctions_to_positions(self, junctions):
        positions = []
        for junction in junctions:
            positions.append(junction.get_position())
        return positions



