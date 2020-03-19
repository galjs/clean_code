
class Position():
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __str__(self):
        return "[{0}, {1}]".format(self.row, self.column)

    def __eq__(self, position):
        if self.row == position.row and self.column == position.column:
            return True
        return False

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def set_row(self, row):
        self.row = row

    def set_column(self, column):
        self.column = column