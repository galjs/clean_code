class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_next(self):
        return self.next

    def get_value(self):
        return self.value

    def set_next(self, node):
        self.next = node

    def set_value(self, value):
        self.value = value

    def has_next(self):
        if self.next is None:
            return False
        return True

class Queue():
    def __init__(self):
        self.first = None
        self.last = None

    def insert(value):
        node = Node(value)
        if self.first is None:
            self.first = node
            self.last = node
        else:
            last.set_next(node)
            last = last.get_next()

    def remove(self):
        value = self.first.get_value()
        first = self.first.get_next()
        if first is None:
            last = None
        return value

    def head(self):
        return self.first.get_value()

    def is_empty(self):
        return self.first is None



class BFS_search():
    def __init__(self, graph):
        self.graph = graph
        self.start_junction = self.get_start_junction()    

        self.find_best_route()


    def get_start_junction(self):
        start = self.graph.get_start()
        return self.graph.get_graph()[start.get_row()][start.get_column()]

    def find_best_route(self):
        nodes = Queue()
        nodes.insert(self.start_junction)
        self.start_junction.set_is_discovered(True)
        while not nodes.is_empty():
            self.start_junction = nodes.remove()

            neighbours = get_neighbours_list(self.start_junction)
            for neighbour in neighbours:
                if neighbour.is_finish:
                    nodes.insert(neighbour)
                    return nodes

                if not neighbour.is_discovered():
                    nodes.insert(neighbour)
                    neighbour.set_is_discovered(True)
            
    
    def get_neighbours_list(current_junction):
        neighbours = []

        if current_junction.has_up():
            neighbours.append(current_junction.get_up())
        
        if current_junction.has_down():
            neighbours.append(current_junction.get_down())

        if current_junction.has_down():
            neighbours.append(current_junction.get_down())

        if current_junction.has_down():
            neighbours.append(current_junction.get_down())

        return neighbours

            