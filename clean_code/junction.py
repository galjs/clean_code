from position import Position


class Junction():

    def __init__(self, position):
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.position = position
        self.discovered = False
        self.finish = False
        self.start = False

    def get_position(self):
        return Position(self.position.get_row(), self.position.get_column())

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
        self.position = Position(position.get_row(), position.get_column())

    def has_up(self):
        return self.up is not None

    def has_down(self):
        return self.down is not None

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

    def set_to_discovered(self):
        self.visited = True

    def set_is_finish(self, is_finish):
        self.finish = is_finish

    def set_is_start(self, is_start):
        self.start = is_start

    def is_start(self):
        return self.start

    def is_finish(self):
        return self.finish

    def is_discovered(self):
        return self.discovered
