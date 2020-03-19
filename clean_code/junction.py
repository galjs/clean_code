from position import Position


class Junction():

    def __init__(self, row, column):
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.position = Position(row, column)

    def get_position(self):
        return Position(self.position)

    def get_up(self):
        return self.up

    def get_down(self):
        return self.down

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


    def set_up(self, up):
        self.up = up

    def set_down(self, down):
        self.down = down

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def set_postion(self, position):
        self.position = Position(position)

    def has_up(self):
        return self.up is not None

    def has_down(self):
        return self.down is not None

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

