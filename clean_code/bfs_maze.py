

class BFS_search():
    def __init__(self, graph):
        self.graph = graph
        self.finish_junction = self.get_finish_junction()
        self.start_junction = self.get_start_junction()    
        self.temp = self.start_junction

    def best_route_in_positions(self):
        self.map_best_route()
        best_route = self.create_best_route()
        return self.convert_junctions_to_positions(best_route)
    
    def get_finish_junction(self):
        finish = self.graph.get_finish()
        return self.graph.get_graph()[finish.get_row()][finish.get_column()]

    def get_start_junction(self):
        start = self.graph.get_start()
        return self.graph.get_graph()[start.get_row()][start.get_column()]

    def map_best_route(self):
        nodes = []
        nodes.append(self.temp)
        self.temp.set_is_discovered(True)
        while not len(nodes) == 0:
            self.temp = nodes[0]
            del nodes[0]

            neighbours = self.get_neighbours(self.temp)
            for neighbour in neighbours:
                if neighbour.is_finish():
                    return

                if not neighbour.is_discovered():
                    nodes.append(neighbour)
                    neighbour.set_is_discovered(True)
            
    
    def get_neighbours(self, current_junction):
        neighbours = []

        if current_junction.has_up():
            neighbours.append(current_junction.get_up())
        
        if current_junction.has_down():
            neighbours.append(current_junction.get_down())

        if current_junction.has_left():
            neighbours.append(current_junction.get_left())

        if current_junction.has_right():
            neighbours.append(current_junction.get_right())

        return neighbours

    def create_best_route(self):
        current_junction = self.finish_junction
        best_route = []
        best_route.append(current_junction)

        while not current_junction.is_start():
            next_junction = self.get_smallest_refernce_number_neighbour(current_junction)
            best_route.append(next_junction)
            current_junction = next_junction

        return best_route

    def get_smallest_refernce_number_neighbour(self, current_junction):
        neighbours = self.get_neighbours(current_junction)
        smallest_reference_neighbour = neighbours[0]
        for neighbour in neighbours:
            if not neighbour.get_reference_number() == -1:
                if neighbour.get_reference_number() < smallest_reference_neighbour.get_reference_number():
                    smallest_reference_neighbour = neighbour
                if smallest_reference_neighbour.get_reference_number() == -1:
                    smallest_reference_neighbour = neighbour
        return smallest_reference_neighbour

    def convert_junctions_to_positions(self, junctions):
        positions = []
        for junction in junctions:
            positions.append(junction.get_position())
        return positions