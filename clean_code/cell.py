class Cell():
    def __init__(self):
        self.blocked = False
        self.mark = None
    
    def __str__(self):
        if self.blocked:
            return 'X'
        if self.mark is not None:
            return self.mark
        return ' '

    def set_mark(self, mark):
        self.mark = mark

    def set_blocked(self):
        self.blocked = True

    def is_blocked(self):
        return self.blocked




