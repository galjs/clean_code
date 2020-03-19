
class Connection():
    def __init__(self, length, junction):
        self. length = length
        self.next = junction

    def get_length(self):
        return self.length

    def get_next(self):
        return self.next

    def set_length(self, length):
        self.length = length

    def set_next(self, junction):
        self.next = junction

