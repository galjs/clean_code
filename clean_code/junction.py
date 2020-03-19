

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

    def has_up(self):
        return self.up is not None

    def has_down(self):
        return self.down is not None

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

