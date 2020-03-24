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
        return positions

    def _map_best_route(self):
        """adds all nodes connected to the current node to a queue.
           repeats the process for every node in the queue 
           until it reaches the desired node (end of maze)"""
        sequence_number = 0
        nodes = [self._start_junction]

        self._start_junction.set_discovered(sequence_number)

        while not len(nodes) == 0:
            current_junction = nodes[0]
            del nodes[0]

            neighbours = current_junction.get_connections()
            for neighbour in neighbours:
                if neighbour.is_finish():
                    neighbour.set_discovered(sequence_number)
                    return

                if not neighbour.is_discovered():
                    nodes.append(neighbour)
                    sequence_number += 1
                    neighbour.set_discovered(sequence_number)
                    

        # if the algorithm checked all nodes without finding the finish node
        # it means there is no solution
        raise BoardIntegrityError("no solution!")

    def _create_best_route(self):
        best_route = []
        current_junction = self._finish_junction
        
        best_route.append(current_junction)

        while not current_junction.is_start():
            next_junction = self._get_smallest_sequence_number_neighbour(current_junction)
            best_route.append(next_junction)
            current_junction = next_junction

        return best_route

    def _get_smallest_sequence_number_neighbour(self, current_junction):
        visited_junctions = filter(lambda connection: connection.is_discovered(), current_junction.get_connections())
        return min(visited_junctions, key=lambda junction: junction.get_sequence_number())