from maze import Maze

def main():
    # 1 = wall. 0 = empty
    state = ("11111111"
    "10100011"
    "10001001"
    "11111111")

    board = Maze(8, state)
    
    print(board)

if __name__ == "__main__":
    main()