from connection import Connection

class Junction():
    def __init__(self, up, down, left, right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def __init__(self):
        self.up = None
        self.down = None
        self.left = None
        self.right = None

    def get_up_value(self):
        return self.up.get_length()

    def get_down_value(self):
        return self.down.get_length()

    def get_left_value(self):
        return self.left.get_length()

    def get_right_value(self):
        return self.right.get_length()

    def get_up_node(self):
        return self.up.get_next()

    def get_down_node(self):
        return self.down.get_next()

    def get_left_node(self):
        return self.left.get_next()

    def get_right_node(self):
        return self.right.get_next()

    def set_up(self, up):
        self.up = up

    def set_down(self, down):
        self.down = down

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def has_up(self):
        return self.up.get_next() is not None

    def has_down(self):
        return self.down.get_next() is not None

    def has_left(self):
        return self.left.get_next() is not None

    def has_right(self):
        return self.right.get_next() is not None

