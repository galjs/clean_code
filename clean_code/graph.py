from junction import Junction
from position import Position

class Graph():
    """stores the junction structure in graph form 
       that a search algorithm can process"""
    def __init__(self, start, finish, maze):
        self._start_position = start
        self._finish_position = finish
        self._start_junction_index = None
        self._finish_junction_index = None
        self._maze = maze
        self._graph = []

        self._create_graph()
        
        self._set_start()
        self._set_finish()

    def _create_graph(self):
        for row in range(self._maze.get_rows()):
            for column in range(self._maze.get_columns()):
                if not self._maze.get_board()[row][column].is_blocked():
                    current_junction = Junction(Position(row, column))
                    self._graph.append(current_junction)
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
        #try:
        #    return self._graph[position.get_row()+row_offset][position.get_column()+column_offset]
        #except IndexError:
        #    return None
        row = position.get_row()+row_offset
        column = position.get_column()+column_offset
        desired_position = Position(row, column)
        for junction in self._graph:
            if junction.get_position() == desired_position:
                return junction
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
        for index in range(len(self._graph)):
            if self._graph[index].get_position() == self._start:
                self._graph[index].set_is_start()
                self._start_junction_index = index
                return

    def _set_finish(self):
        for index in range(len(self._graph)):
            if self._graph[index].get_position() == self._finish:
                self._graph[index].set_is_finish()
                self._finish_junction_index = index
                return

    def get_finish_junction(self):
        return self._graph[self._finish_junction_index]

    def get_start_junction(self):
        return self._graph[self._start_junction_index]

    def convert_junctions_to_positions(self, junctions):
        positions = []
        for junction in junctions:
            positions.append(junction.get_position())
        return positions



