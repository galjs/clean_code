from maze import Maze

def main():
    # 1 = wall. 0 = empty
    state = ("11111"
    "10101"
    "10001"
    "11111")

    board = Maze(5, state)
    
    board.print_maze_representation()

if __name__ == "__main__":
    main()