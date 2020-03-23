from exceptions import BoardIntegrityError



class BFS_search():
    """Implements BFS algorithm to find the shortest path in the maze.
        for more inforamtion visit:
        https://en.wikipedia.org/wiki/Breadth-first_search."""

    def __init__(self, graph):
        self._graph = graph
        self._finish_junction = self._graph.get_finish_junction()
        self._start_junction = self._graph.get_start_junction()

    def best_route_in_positions(self):
        self._map_best_route()
        best_route = self._create_best_route()
        positions = self._graph.convert_junctions_to_positions(best_route)
        if len(positions) == 0:
            raise BoardIntegrityError("no solution!")
        return positions

    def _map_best_route(self):
        """adds all nodes connected to the current node to a queue.
           repeats the process for every node in the queue 
           until it reaches the desired node (end of maze)"""
        reference_number = 0
        nodes = [self._start_junction]

        self._start_junction.set_discovered(reference_number)
        reference_number += 1

        while not len(nodes) == 0:
            current_junction = nodes[0]
            del nodes[0]

            neighbours = current_junction.get_connections()
            for neighbour in neighbours:
                if neighbour.is_finish():
                    neighbour.set_discovered(reference_number)
                    reference_number += 1
                    return

                if not neighbour.is_discovered():
                    nodes.append(neighbour)
                    neighbour.set_discovered(reference_number)
                    reference_number += 1

    def _create_best_route(self):
        best_route = []
        if self._finish_junction.is_discovered():
            current_junction = self._finish_junction
        
            best_route.append(current_junction)

            while not current_junction.is_start():
                next_junction = self._get_smallest_sequence_number_neighbour(current_junction)
                best_route.append(next_junction)
                current_junction = next_junction

        return best_route

    def _get_smallest_sequence_number_neighbour(self, current_junction):
        return sorted(filter(lambda connection: not connection.get_sequence_number() == -1, current_junction.get_connections()), key=lambda neighbour: neighbour.get_sequence_number())[0]