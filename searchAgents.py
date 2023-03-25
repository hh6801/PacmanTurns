from fringes import Stack,PriorityQueue, Queue
import utils
def bfs(problem):
    """
    Bắt đầu tìm kiếm đường đi từ vị trí ban đầu của Pacman đến tất cả các thức ăn trong mê cung.
    """
    
    
    food_locations = problem.food_locations  # sao chép danh sách các điểm mồi
    if len(food_locations) == 0:
        return []+['Stop']
    start_state = problem.get_start_state()
     
    explored = set()
    frontier = Queue()
    frontier.push((start_state, []))
    num_foods_eaten = 0  # số điểm mồi đã ăn được
    while not frontier.is_empty():
        state, actions = frontier.pop()
        if state in explored:
            continue
        explored.add(state)
        if problem.is_goal_state(state):
            problem.update_food(problem.remove_food(food_locations,state))
            if len(food_locations) ==0:
                return actions+['Stop']
            problem.set_start_state(state)
            sub_actions = bfs(problem)
            return actions + sub_actions
        
        for next_state, action, _ in problem.successor(state):
            if next_state not in explored:
                new_actions = actions + [action]
                frontier.push((next_state, new_actions))
    return actions


def dfs(problem):
    """
    Tìm kiếm theo chiều sâu từ vị trí ban đầu của Pacman đến tất cả các điểm mồi trong mê cung.
    """
    food_locations = problem.food_locations
    if len(food_locations) == 0:
        return []+['Stop']
    start_state = problem.get_start_state()
    
    explored = set()
    frontier = Stack()
    frontier.push((start_state, []))
    while not frontier.is_empty():
        state, actions = frontier.pop()
        if state in explored:
            continue
        explored.add(state)
        if problem.is_goal_state(state):
            problem.update_food(problem.remove_food(food_locations,state))
            if len(food_locations) == 0:
                return actions+['Stop']
            problem.set_start_state(state)
            return actions + dfs(problem)
        for next_state, action, cost in problem.successor(state):
            if next_state not in explored:
                frontier.push((next_state, actions + [action]))
    return actions



def ucs(problem):
    """
    Tìm đường đi ngắn nhất từ vị trí ban đầu của Pacman đến tất cả các điểm mồi trong mê cung.
    """ 
    food_locations = problem.food_locations # Lấy danh sách các điểm mồi trong mê cung
    if len(food_locations) == 0:
        return []+['Stop']
    start_state = problem.get_start_state()
    
    explored = set()
    frontier = PriorityQueue()
    frontier.push((start_state, [], 0), 0)

    while not frontier.is_empty():
        state, actions, cost = frontier.pop()
        if state in explored:
            continue
        explored.add(state)
        if problem.is_goal_state(state):  # Nếu Pacman ăn được một điểm mồi
            problem.update_food(problem.remove_food(food_locations,state))  # Xóa điểm mồi khỏi danh sách
            if len(food_locations) == 0:  # Nếu không còn điểm mồi nào
                return actions+['Stop']  # Trả về các hành động đã thực hiện
            problem.set_start_state(state)
            return actions + ucs(problem)
        for next_state, action, step_cost in problem.successor(state):
            if next_state not in explored:
                total_cost = cost + step_cost
                frontier.push((next_state, actions + [action], total_cost), total_cost)
    return actions

def manhattanHeuristic(state,problem):
    current_pos = state
    food_pos = problem.food_locations
    if isinstance(food_pos,list):
        return abs(current_pos[0] - food_pos[0][0]) + abs(current_pos[1] - food_pos[0][1])
    else:
        return abs(current_pos[0] - food_pos[0]) + abs(current_pos[1] - food_pos[1])

# hàm heuristic 2


def euclideanHeuristic(state,problem):
    current_pos = state
    food_pos = problem.food_locations
    if isinstance(food_pos, list):
        return ((current_pos[0] - food_pos[0][0])**2 + (current_pos[1] - food_pos[0][1])**2)**0.5
    else:
        return ((current_pos[0] - food_pos[0])**2 + (current_pos[1] - food_pos[1])**2)**0.5


def heuristic(state,problem):
    '''
    A* heuristic function that estimates the distance from the current state to the closest food pellet
    '''
    food_locations = problem.food_locations
    if len(food_locations) == 0:
        return 0

    # Find the closest food pellet
    min_distance = float('inf')
    for food in food_locations:
        distance = manhattanDistance(state, food)
        if distance < min_distance:
            min_distance = distance

    return min_distance

def astar(problem, heuristic, start_state=None):
    """
    A* search algorithm for SingleFoodSearchProblem.
    """
    if start_state is None:
        start_state = problem.get_start_state()

    closed = set()
    fringe = PriorityQueue()
    fringe.push((start_state, [], 0), 0)
    while not fringe.is_empty():
        current_state, current_path, current_cost = fringe.pop()
        if current_state in closed:
            continue
        if problem.is_goal_state(current_state):
            return current_path
        closed.add(current_state)
        for successor_state, action, cost in problem.successor(current_state):
            if successor_state not in closed:
                new_path = current_path + [action]
                new_cost = current_cost + cost
                priority = new_cost + heuristic(successor_state, problem)
                fringe.push((successor_state, new_path, new_cost), priority)
    return []


def manhattanDistance( xy1, xy2 ):
    "Returns the Manhattan distance between points xy1 and xy2"
    return abs( xy1[0] - xy2[0] ) + abs( xy1[1] - xy2[1] )


def gbfs(problem, heuristic, start_state=None):
    """
    Greedy Best First Search algorithm for SingleFoodSearchProblem.
    """
    if start_state is None:
        start_state = problem.get_start_state()

    closed = set()
    fringe = PriorityQueue()
    fringe.push((start_state, [], 0), 0)
    while not fringe.is_empty():
        current_state, current_path, current_cost = fringe.pop()
        if current_state in closed:
            continue
        if problem.is_goal_state(current_state):
            return current_path
        closed.add(current_state)
        for successor_state, action, cost in problem.successor(current_state):
            if successor_state not in closed:
                new_path = current_path + [action]
                new_cost = current_cost + cost
                priority = heuristic(successor_state, problem)
                fringe.push((successor_state, new_path, new_cost), priority)
    return []
