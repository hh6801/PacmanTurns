from problems import *
from fringes import *
from searchAgents import *



if __name__ == '__main__':
    # SingleFoodSearchProblem
    maze_file_path1 = 'pacman_single03.txt'
    problem1 = SingleFoodSearchProblem(maze_file=maze_file_path1)

    print('Maze:')
    problem1.print_maze()
    print(problem1.animate(bfs(problem1)))

    # MultiFoodSearchProblem
    maze_file_path2 = 'pacman_multi03.txt'
    problem2 = MultiFoodSearchProblem(maze_file=maze_file_path2)

    print('Maze:')
    problem2.print_maze()
    print(problem2.animate(bfs(problem2)))

    # A*
    problem3 = SingleFoodSearchProblem(maze_file=maze_file_path1)
    print(problem3.animate(astar(problem3, euclideanHeuristic)))

    # GBFS
    problem4 = SingleFoodSearchProblem(maze_file=maze_file_path1)
    print(problem4.animate(gbfs(problem4, euclideanHeuristic)))
    
    
    # EightQueenProblem
    file_path = 'eight_queens03.txt'
    problem = EightQueenProblem(file_path)
    print("Initial board:")
    problem.print_board()
    final_state = problem.hill_climbing_search()
    while problem.h(final_state) == 0:
        final_state = problem.hill_climbing_search()
    print("\nSolution:")
    problem.print_board_state(final_state)


