from maze import Maze
from position import Position
from graph import Graph

def main():
    # 1 = wall. 0 = empty
    state = ("11111111"
    "10100011"
    "10001001"
    "11111111")

    board = Maze(8, state)
    board_as_graph = Graph(Position(1, 1), Position(2, 6), board)
    
    print(board)
    print(board_as_graph)


if __name__ == "__main__":
    main()