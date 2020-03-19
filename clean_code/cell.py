class Cell():
    def __init__(self):
        self.blocked = True
        self.mark = None
    
    def __str__(self):
        if self.blocked:
            return 'X'
        if self.mark is not None:
            return self.mark
        return '+'

    def set_mark(self, mark):
        self.mark = mark

    def set_blocked(self, is_blocked):
        self.blocked = is_blocked

    def is_blocked(self):
        return self.blocked




