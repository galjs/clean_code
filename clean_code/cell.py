class Cell():
    """Represents a square in the maze that can be a wall or a path."""
    def __init__(self):
        self._blocked = False
        self._mark = None
    
    def __str__(self):
        if self._blocked:
            return 'X'
        if self._mark is not None:
            return self._mark
        return ' '

    def set_mark(self, _mark):
        self._mark = _mark

    def set_blocked(self):
        self._blocked = True

    def is_blocked(self):
        return self._blocked




