from maze import Maze

def main():
    
    state = [True, False, True, 
             True, True, True, 
             True, True, True, 
             False, False, False,
             False, True, False]

    board = Maze(3, 5, state)
    
    board.print_maze_representation()

if __name__ == "__main__":
    main()