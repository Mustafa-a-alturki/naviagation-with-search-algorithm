from utility import cal_abs_elevation_diff, Node, cal_h
import copy


class Problem:
    def __init__(self, init_state, state_space, goal_state, actions, max_elev_diff):
        self.init_state = init_state
        self.state_space = state_space
        self.goal_state = goal_state
        self.actions = actions
        self.max_elev_diff = max_elev_diff

    def __str__(self):
        return f'initial state:{self.init_state}, goal state:{self.goal_state}'

    def goal_test(self, state):
        print('current state', state)
        print('goal state', self.goal_state)
        return state == self.goal_state

    def is_possible_action(self, source, destination):
        if destination is None:
            return False
        if cal_abs_elevation_diff(source, destination) > self.max_elev_diff:
            return False
        elif destination.x < 0 or destination.y < 0:
            return False
        elif destination.x >= len(self.state_space[0]) or destination.y >= len(self.state_space):
            return False
        else:
            return True

    def get_possible_actions(self, state):
        possible_actions = []
        for action in self.actions:
            destination = self.transition_fn(state, action)
            if destination is not None:
                possible_actions.append((action, destination))
        return possible_actions

    def transition_fn(self, state, action):
        destination = copy.deepcopy(state)
        if action == 'E':
            destination.y += 1
        elif action == 'W':
            destination.y -= 1
        elif action == 'N':
            destination.x += 1
        elif action == 'S':
            destination.x -= 1
        elif action == 'NE':
            destination.y += 1
            destination.x += 1
        elif action == 'SE':
            destination.y += 1
            destination.x -= 1
        elif action == 'SW':
            destination.y -= 1
            destination.x -= 1
        elif action == 'NW':
            destination.y -= 1
            destination.x += 1
        else:
            destination = None

        if self.is_possible_action(state, destination):
            destination.z = (self.state_space[destination.y][destination.x]).z
            return destination
        else:
            return None


# return nodes, not state
def expand(parent, destination, action, goal_state, algorithm):
    if algorithm == 'UCS' or algorithm == 'BFS':
        child = Node(state=destination,
                     parent=parent,
                     path_cost=parent.path_cost + step_cost(algorithm,
                                                            action,
                                                            cal_abs_elevation_diff(parent.state,
                                                                                   destination)))
    else:
        child = Node(state=destination,
                     parent=parent,
                     path_cost=parent.path_cost + step_cost(algorithm,
                                                            action,
                                                            cal_abs_elevation_diff(parent.state,
                                                                                   destination)),
                     estimated_cost=cal_h(destination, goal_state))
    return child


# step_cost for BFS is 1 for all movement but you have to check if the moving is legal regarding the elevation
# difference
def step_cost(algorithm, action, abs_elevation_diff=0):
    hor_ver = ['E', 'W', 'N', 'S']
    diag = ['NE', 'SE', 'SW', 'NW']
    if algorithm == 'BFS':
        return 1
    elif algorithm == 'UCS':
        if action in hor_ver:
            return 10
        elif action in diag:
            return 14
    elif algorithm == 'A_STAR':
        if action in hor_ver:
            return 10 + abs_elevation_diff
        elif action in diag:
            return 14 + abs_elevation_diff
