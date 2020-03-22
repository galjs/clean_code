from position import Position

class Junction():
    """represents a path square in the maze.
       connected to all the path-squares that are adjacent to it"""
    def __init__(self, position):
        self._connections = []
        self._position = position
        self._discovered = False
        self._finish = False
        self._start = False
        self._reference_number = None

    def get_position(self):
        return Position(self._position.get_row(), self._position.get_column())

    def get_connections(self):
        return self._connections

    def get_reference_number(self):
        return self._reference_number

    def set_postion(self, position):
        self._position = Position(position.get_row(), position.get_column())

    def set_is_discovered(self, is_discovered):
        self._discovered = is_discovered

    def set_is_finish(self):
        self._finish = True

    def set_is_start(self):
        self._start = True

    def set_reference_number(self, reference_number):
        self._reference_number = reference_number

    def has_connections(self):
        return len(self._connections) > 0

    def add_connection(self, connection):
        self._connections.append(connection)

    def is_start(self):
        return self._start

    def is_finish(self):
        return self._finish

    def is_discovered(self):
        return self._discovered