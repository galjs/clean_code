from maze import Maze

def main():
    
    state = ("11111"
    "00101"
    "10001"
    "11101")

    board = Maze(5, state)
    
    board.print_maze_representation()

if __name__ == "__main__":
    main()