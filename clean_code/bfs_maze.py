

class BFS_search():
    def __init__(self, graph):
        self.graph = graph
        self.start_junction = self.get_start_junction()    

        printlen(self.find_best_route())


    def get_start_junction(self):
        start = self.graph.get_start()
        return self.graph.get_graph()[start.get_row()][start.get_column()]

    def find_best_route(self):
        nodes = []
        nodes.append(self.start_junction)
        self.start_junction.set_is_discovered(True)
        while not len(nodes) == 0:
            self.start_junction = nodes[0]
            del nodes[0]

            neighbours = self.get_neighbours(self.start_junction)
            for neighbour in neighbours:
                if neighbour.is_finish:
                    nodes.append(neighbour)
                    return nodes

                if not neighbour.is_discovered():
                    nodes.append(neighbour)
                    neighbour.set_is_discovered(True)
            
    
    def get_neighbours(self, current_junction):
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

            