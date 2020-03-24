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
        self._update_junctions()
        
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

    def _update_junctions(self):
        junctions = filter(None, [node for row in self._graph for node in row])
        for junction in junctions:
            position = junction.get_position()

            # by only connecting two at a time, no duplicate calls to
            # get_junction_relative_to_position are made
            upper_junction = self._get_junction_relative_to_position(position, -1, 0)
            left_junction = self._get_junction_relative_to_position(position, 0, -1)

            if upper_junction is not None:
                junction.add_connection(upper_junction)
                upper_junction.add_connection(junction)

            if left_junction is not None:
                junction.add_connection(left_junction)
                left_junction.add_connection(junction)

    def _get_junction_relative_to_position(self, position, row_offset=0, column_offset=0):
        try:
            return self._graph[position.get_row()+row_offset][position.get_column()+column_offset]
        except IndexError:
            return None


    def __str__(self):
        display = ""
        for row in self._graph:
            for node in row:
                if node is not None:
                    display += str(node)
                else:
                    display += '   '
            display += '\n'
        return display

    def _set_start(self):
        designated_start = self.get_start_junction()
        designated_start.set_is_start()

    def _set_finish(self):
        designated_finish = self.get_finish_junction()
        designated_finish.set_is_finish()

    def get_finish_junction(self):
        return self._get_junction_relative_to_position(self._finish)

    def get_start_junction(self):
        return self._get_junction_relative_to_position(self._start)

    def convert_junctions_to_positions(self, junctions):
        return [junction.get_position() for junction in junctions]