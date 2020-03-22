from maze import BoardIntegrityError



class BFS_search():
    def __init__(self, graph):
        self.graph = graph
        self.finish_junction = self.graph.get_finish_junction()
        self.start_junction = self.graph.get_start_junction()

    def best_route_in_positions(self):
        self.map_best_route()
        best_route = self.create_best_route()
        positions = self.graph.convert_junctions_to_positions(best_route)
        if len(positions) == 0:
            raise BoardIntegrityError("no solution!")
        return positions

    def map_best_route(self):
        nodes = []
        reference_number = 0
        current_junction = self.start_junction
        nodes.append(current_junction)
        current_junction.set_is_discovered(True)
        current_junction.set_reference_number(reference_number)
        reference_number += 1
        while not len(nodes) == 0:
            current_junction = nodes[0]
            del nodes[0]

            neighbours = current_junction.get_connections()
            for neighbour in neighbours:
                if neighbour.is_finish():
                    neighbour.set_is_discovered(True)
                    neighbour.set_reference_number(reference_number)
                    reference_number += 1
                    return

                if not neighbour.is_discovered():
                    nodes.append(neighbour)
                    neighbour.set_is_discovered(True)
                    neighbour.set_reference_number(reference_number)
                    reference_number += 1

    def create_best_route(self):
        best_route = []
        if self.finish_junction.is_discovered():
            current_junction = self.finish_junction
        
            best_route.append(current_junction)

            while not current_junction.is_start():
                next_junction = self.get_smallest_refernce_number_neighbour(current_junction)
                best_route.append(next_junction)
                current_junction = next_junction

        return best_route

    def get_smallest_refernce_number_neighbour(self, current_junction):
        neighbours = current_junction.get_connections()
        smallest_reference_neighbour = neighbours[0]

        for neighbour in neighbours:
            if neighbour.is_discovered():
                if neighbour.get_reference_number() < smallest_reference_neighbour.get_reference_number():
                    smallest_reference_neighbour = neighbour
                if not smallest_reference_neighbour.is_discovered():
                    smallest_reference_neighbour = neighbour

        return smallest_reference_neighbour