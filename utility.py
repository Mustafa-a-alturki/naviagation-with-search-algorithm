import math


class State:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True


class Node:
    def __init__(self, state, parent, path_cost, estimated_cost=0):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost
        self.estimated_cost = estimated_cost

    def __str__(self):
        return f'Node with state:{self.state}, parent:{self.parent}, path cost:{self.path_cost}'

    def __lt__(self, other):
        return self.path_cost + self.estimated_cost < other.path_cost + other.estimated_cost


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0) if len(self.queue) > 0 else None

    def is_empty(self):
        return len(self.queue) < 1

    def __str__(self):
        s = '['
        for i in self.queue:
            s += i + ''
        s += ']'
        return s


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if len(self.stack) > 0 else None

    def is_empty(self):
        return len(self.stack) < 1


def create_state_objects(grid, height, width):
    states_grid = [[None for _ in range(width)] for _ in range(height)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            states_grid[i][j] = State(j, i, grid[i][j])
    return states_grid


# a function to trace the parents of final_node to root, adding each node on the way to the solution and returns it
def get_solution(final_node):
    solution = '' + str(final_node.state.x) + ',' + str(final_node.state.y)
    node = final_node.parent
    while node is not None:
        solution = str(node.state.x) + ',' + str(node.state.y) + ' ' + solution
        node = node.parent
    return solution


def cal_abs_elevation_diff(source, destination):
    return abs(destination.z - source.z)


def cal_stright_line_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# returns the sum of path_cost and estimated cost from node to goal.
def cal_h(state, goal_state):
    if state == goal_state:
        estimated_cost = 0
    else:
        estimated_cost = math.floor(cal_stright_line_distance(state.x, state.y, goal_state.x,
                                                              goal_state.y)) + cal_abs_elevation_diff(state, goal_state)
    return estimated_cost


def read_input_file():
    with open('input.txt') as file:
        input_dict = dict()
        lines = file.readlines()
        input_dict['algorithm'] = lines[0].strip()
        input_dict['width'], input_dict['height'] = int(lines[1].split()[0]), int(lines[1].split()[1])
        input_dict['landing_site'] = (int(lines[2].split()[0]), int(lines[2].split()[1]))
        input_dict['max_elevation_diff'] = int(lines[3])
        input_dict['num_of_targets'] = int(lines[4])
        targets = []
        for target in range(input_dict['num_of_targets']):
            x = int(lines[5 + target].split()[0])
            y = int(lines[5 + target].split()[1])
            targets.append((x, y))
        input_dict['targets'] = targets
        elevations = lines[5 + input_dict['num_of_targets']:]
        elevations_matrix = []
        for row in elevations:
            elevations_matrix.append([int(i) for i in row.split()])
        print(elevations_matrix)
        input_dict['state_grid'] = create_state_objects(elevations_matrix, input_dict['height'], input_dict['width'])
        return input_dict
