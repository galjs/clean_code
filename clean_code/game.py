from maze import Maze
from position import Position
from graph import Graph
from bfs_maze import BFS_search

def main():
    # 1 = wall. 0 = empty
    state = ("111111111"
    "101000101"
    "100010011"
    "101000101"
    "100010001"
    "111111111")

    maze = Maze(9, state)
    board_as_graph = Graph(Position(1, 1), Position(4, 7), maze)
    print(maze)
    find = BFS_search(board_as_graph)
    positions = find.best_route_in_positions()
    for position in positions:
        maze.get_board()[position.get_row()][position.get_column()].set_mark("+")

    print(maze)
    print("number of steps needed: ", len(positions))
    



if __name__ == "__main__":
    main()