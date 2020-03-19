from maze import Maze
from position import Position
from graph import Graph
from bfs_maze import BFS_search

def main():
    # 1 = wall. 0 = empty
    state = ("1111111111"
    "1010001001"
    "1000100101"
    "1010001011"
    "1000100101"
    "1111111111")

    maze = Maze(10, state)
    board_as_graph = Graph(Position(1, 1), Position(4, 8), maze)
    print(maze)
    find = BFS_search(board_as_graph)
    positions = find.best_route_in_positions()
    for position in positions:
        maze.get_board()[position.get_row()][position.get_column()].set_mark("+")

    print(maze)
    print("number of steps needed: ", len(positions), "\n")
    



if __name__ == "__main__":
    main()