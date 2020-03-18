class Cell():
    def __init__(self):
        self.blocked = True
        self.edge = False
       

    def set_blocked(self, is_blocked):
        self.blocked = is_blocked

    def set_edge(self, is_edge):
        self.edge = is_edge
    
    def get_edge(self):
        return self.edge

    def get_blocked(self):
        return self.blocked

    def get_cell_representation(self):
        if self.blocked:
            return 'X'
        return ' '



