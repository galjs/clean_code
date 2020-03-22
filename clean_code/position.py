
class Position():
    """x and y index of a node in the maze matrix"""
    def __init__(self, row, column):
        self._row = row
        self._column = column

    def __str__(self):
        return "[{0}, {1}]".format(self._row, self._column)

    def __eq__(self, position):
        return self._row == position.get_row() and self._column == position.get_column()
    
    def get_row(self):
        return self._row

    def get_column(self):
        return self._column

    def set_row(self, row):
        self._row = row

    def set_column(self, column):
        self._column = column