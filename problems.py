import os
import time
import random
import os
import numpy as np
class SingleFoodSearchProblem:
 
  
  def __init__(self, maze_file):

    self.maze_file = maze_file
    self.walls, self.food_locations, self.start_state = self.load_maze()

  def load_maze(self):
    with open(self.maze_file, 'r') as f:
        lines = f.readlines()
    walls = []
    food_locations = None
    start_state = None
    for row in range(len(lines)):
        line = lines[row].strip()
        maze_row = []
        for col in range(len(line)):
            if line[col] == '%':
                maze_row.append(True)
            elif line[col] == '.':
                food_locations = (row, col)
                maze_row.append(False)
            elif line[col] == 'P':
                start_state = (row, col)
                maze_row.append(False)
            else:
                maze_row.append(False)
        walls.append(maze_row)
    return walls, food_locations, start_state

  def is_goal_state(self, state):
    return state == self.food_locations
  def remove_food(self, food_locations, state):
    if isinstance(food_locations, list):
      if self.is_goal_state(state):
          self.food_locations.remove(state)
    elif isinstance(food_locations, tuple):
          self.food_locations = ()
    return self.food_locations
  def successor(self, state):
    successors = []
    for action in ['North', 'South', 'East', 'West']:
        row, col = state
        if action == 'North':
            row -= 1
        elif action == 'South':
            row += 1
        elif action == 'East':
            col += 1
        elif action == 'West':
            col -= 1
        if not self.walls[row][col]:
            successors.append(((row, col), action, 1))
    return successors

  def get_start_state(self):
    return self.start_state

  def get_cost_of_actions(self, actions):
    return len(actions)

  def update_food(self,food_locations):
      self.food_locations = food_locations
  
  def set_start_state(self,state):
      self.start_state = state

  def print_maze(self, state=None,food_locations = None):
    for r in range(len(self.walls)):
        line = ''
        for c in range(len(self.walls[0])):
            if self.walls[r][c]:
                line += '%'
            elif food_locations == None:
               food_locations = self.load_maze()[1]
               if (r, c) == food_locations or (r, c) in food_locations:
                  line += '.'
            elif state == None:
               state = self.load_maze()[2]
               if (r, c) == state:
                  line += 'P'
            elif food_locations == None and state == None:
                food_locations = self.load_maze()[1]
                state = self.load_maze()[2]
                if (r, c) == food_locations or (r, c) in food_locations:
                  line += '.'
                if (r, c) == state:
                  line += 'P'
            elif (r, c) == food_locations or (r, c) in food_locations:
                if (r, c) == state:
                    line += 'P'
                else:
                   line += '.'
            elif (r, c) == self.start_state:
                line += 'P'
            elif (r, c) == state:
                line += 'P'
            else:
                line += ' '
        print(line)

  def animate(self, actions):
    maze = self.load_maze()
    state = maze[2]
    food_locations = maze[1]
    
    for action in actions:
        if action == 'North':
            state = (state[0] - 1, state[1])
        elif action == 'South':
            state = (state[0] + 1, state[1])
        elif action == 'East':
            state = (state[0], state[1] + 1)
        elif action == 'West':
            state = (state[0], state[1] - 1)
        elif action == 'Stop':
           state = (state[0], state[1])

        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_maze(state,food_locations)
        if state == food_locations or state in food_locations:
            self.update_food(self.remove_food(food_locations, state))
        time.sleep(0.1)

    print("Pacman has found the food!")
    return 'Done'


class MultiFoodSearchProblem:
  '''
  Input: 
    maze_file: string -> file path to a maze (txt)
  '''

  def __init__(self, maze_file):
    '''
    walls: list -> represent wall of the maze
    food_locations: tuple -> location of the food
    start_state: tuple -> location to the starting place of Pacman
    '''
    self.maze_file = maze_file
    self.walls, self.food_locations, self.start_state = self.load_maze()

  def load_maze(self):
    with open(self.maze_file, 'r') as f:
        lines = f.readlines()
    walls = []
    food_locations = []
    start_state = None
    for row in range(len(lines)):
        line = lines[row].strip()
        maze_row = []
        for col in range(len(line)):
            if line[col] == '%':
                maze_row.append(True)
            elif line[col] == '.':
                food_locations.append((row, col))
                maze_row.append(False)
            elif line[col] == 'P':
                start_state = (row, col)
                maze_row.append(False)
            else:
                maze_row.append(False)
        walls.append(maze_row)
    return walls, food_locations, start_state

  def is_goal_state(self, state):
    return state in self.food_locations

  def successor(self, state):
    successors = []
    for action in ['North', 'South', 'East', 'West']:
        row, col = state
        if action == 'North':
            row -= 1
        elif action == 'South':
            row += 1
        elif action == 'East':
            col += 1
        elif action == 'West':
            col -= 1
        if not self.walls[row][col]:
            successors.append(((row, col), action, 1))
    return successors

  def set_start_state(self, state):
      self.start_state = state

  def get_start_state(self):
    return self.start_state

  def get_cost_of_actions(self, actions):
    return len(actions)

  def update_food(self, food_locations):
      self.food_locations = food_locations

  def remove_food(self, food_locations, state):
    if isinstance(food_locations, list):
      if self.is_goal_state(state):
          self.food_locations.remove(state)
    elif isinstance(food_locations, tuple):
        self.food_locations = ()
    return self.food_locations

  def print_maze(self, state=None, food_locations=None):
    for r in range(len(self.walls)):
        line = ''
        for c in range(len(self.walls[0])):
            if self.walls[r][c]:
                line += '%'
            elif food_locations == None :
               food_locations = self.load_maze()[1]
               if (r, c) == food_locations or (r, c) in food_locations:
                  line += '.'
            elif state == None:
               state = self.load_maze()[2]
               if (r, c) == state:
                  line += 'P'
            elif food_locations == None and state == None:
                food_locations = self.load_maze()[1]
                state = self.load_maze()[2]
                if (r, c) == food_locations or (r, c) in food_locations:
                  line += '.'
                if (r, c) == state:
                  line += 'P'
            elif (r, c) == food_locations or (r, c) in food_locations:
                if (r, c) == state and len(food_locations) !=0:
                    line += 'P'
                else:
                   line += '.'
            elif (r, c) == state:
                line += 'P'
            else:
                line += ' '
        print(line)

  def animate(self, actions):
    maze = self.load_maze()
    state = maze[2]
    food_locations = maze[1]

    for action in actions:
        if action == 'North':
            state = (state[0] - 1, state[1])
        elif action == 'South':
            state = (state[0] + 1, state[1])
        elif action == 'East':
            state = (state[0], state[1] + 1)
        elif action == 'West':
            state = (state[0], state[1] - 1)
        elif action == 'Stop':
           state = (state[0], state[1])
        print(food_locations)
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_maze(state, food_locations)
        if state == food_locations or state in food_locations:
            
            food_locations = [x for x in food_locations if x != state]
        time.sleep(0.1)

    print("Pacman has found the food!")
    return 'Done'


class EightQueenProblem:
    def __init__(self, file_path):
        self.file_path = file_path
        self.board = self.read_board()

    def read_board(self):
        board = []
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                row = []
                for char in line.strip():
                    if char != ' ':
                        row.append(char)
                board.append(row)
        return board

    def print_board(self):
        for row in range(8):
            for col in range(8):
                    if self.board[row][col] == 'Q':
                        print("Q", end=" ")
                    else:
                        print("0", end=" ")
            print()

    def print_board_state(self, state):
        board_state = [['0' for _ in range(8)] for _ in range(8)]
        for i, col in enumerate(state):
            board_state[col][i] = 'Q'
        for row in board_state:
            print(' '.join(row))

    def h(self, state):
        attacks = 0
        for i in range(8):
            for j in range(i + 1, 8):
                if state[i] == state[j] or state[i] + i == state[j] + j or state[i] - i == state[j] - j:
                    attacks += 1
        return attacks

    def hill_climbing_search(self):
        current_state = [random.randint(0, 7) for _ in range(8)]
        current_h = self.h(current_state)
        while True:
            neighbors = []
            for i in range(8):
                for j in range(8):
                    if i != j:
                        neighbor = list(current_state)
                        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                        neighbors.append(neighbor)
            if not neighbors:
                return current_state
            neighbor_h = [self.h(neighbor) for neighbor in neighbors]
            best_neighbor_h = min(neighbor_h)
            if best_neighbor_h >= current_h:
                return current_state
            best_neighbors = [neighbor for neighbor, h in zip(
                neighbors, neighbor_h) if h == best_neighbor_h]
            current_state = random.choice(best_neighbors)
            current_h = best_neighbor_h

            # Check if the current state satisfies the requirement of no attacking queens
            if self.h(current_state) == 0:
                return current_state
