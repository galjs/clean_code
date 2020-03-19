class Cell():
    def __init__(self):
        self.blocked = True
        self.edge = False
    
    def __str__(self):
        if self.blocked:
            return 'X'
        return '+'

    def set_blocked(self, is_blocked):
        self.blocked = is_blocked

    def set_edge(self, is_edge):
        self.edge = is_edge
    
    def is_edge(self):
        return self.edge

    def is_blocked(self):
        return self.blocked




