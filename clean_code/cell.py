class Cell():
    def __init__(self):
        self.blocked = True
    
    def __str__(self):
        if self.blocked:
            return 'X'
        return '+'

    def set_blocked(self, is_blocked):
        self.blocked = is_blocked

    def is_blocked(self):
        return self.blocked




