from position import Position

class Junction():

    def __init__(self, position):
        self.connections = []
        self.position = position
        self.discovered = False
        self.finish = False
        self.start = False
        self.reference_number = -1

    def get_position(self):
        return Position(self.position.get_row(), self.position.get_column())

    def get_connections(self):
        return self.connections

    def get_reference_number(self):
        return self.reference_number

    def set_postion(self, position):
        self.position = Position(position.get_row(), position.get_column())

    def set_is_discovered(self, is_discovered):
        self.discovered = is_discovered

    def set_is_finish(self):
        self.finish = True

    def set_is_start(self):
        self.start = True

    def set_reference_number(self, reference_number):
        self.reference_number = reference_number

    def has_connections(self):
        return len(self.connections) > 0

    def add_connection(self, connection):
        self.connections.append(connection)

    def is_start(self):
        return self.start

    def is_finish(self):
        return self.finish

    def is_discovered(self):
        return self.discovered