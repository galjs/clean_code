from maze import Maze
from position import Position
from graph import Graph
from bfs_search import BFS_search

def main():
    # 1 = wall, 0 = empty
    maze_structure = ("1111111111"
                      "1010001001"
                      "1000100101"
                      "1010001011"
                      "1000100001"
                      "1111111111")

    maze = Maze(10, maze_structure)
    print(maze)

    start = Position(1, 1)
    finish = Position(4, 8)
    board_as_graph = Graph(start, finish, maze)
    
    find = BFS_search(board_as_graph)
    positions = find.best_route_in_positions()
    maze.mark_cells_at_positions(positions)

    print(maze)
    print("number of steps needed: ", len(positions), "\n")
    
if __name__ == "__main__":
    main()