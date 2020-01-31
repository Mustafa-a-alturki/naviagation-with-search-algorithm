from utility import Queue, Stack, Node, get_solution
from problem import expand
import heapq


def bfs(problem):
    current_node = Node(problem.init_state, None, 0)
    if problem.goal_test(current_node.state):
        solution = get_solution(current_node)
        return solution
    frontier = Queue()
    frontier.enqueue(current_node)
    explored_set = []
    while True:
        if frontier.is_empty():
            return 'FAIL'
        current_node = frontier.dequeue()
        # print(current_node.state)
        explored_set.append(current_node.state)
        for action, destination in problem.get_possible_actions(current_node.state):
            child = expand(parent=current_node, destination=destination, action=action, goal_state=problem.goal_state,
                           algorithm='BFS')
            if child.state not in [node.state for node in frontier.queue] and child.state not in [state for state in
                                                                                                  explored_set]:
                # print(child.state)
                if problem.goal_test(child.state):
                    solution = get_solution(child)
                    return solution
                frontier.enqueue(child)


def ucs(problem):
    frontier = []
    heapq.heappush(frontier, Node(problem.init_state, None, 0))
    explored_set = []
    while True:
        if len(frontier) <= 0:
            return 'FAIL'
        current_node = heapq.heappop(frontier)
        if problem.goal_test(current_node.state):
            solution = get_solution(current_node)
            return solution
        explored_set.append(current_node.state)
        for action, destination in problem.get_possible_actions(current_node.state):
            child = expand(parent=current_node, destination=destination, action=action, goal_state=problem.goal_state,
                           algorithm='UCS')
            if child.state not in [node.state for node in frontier] and child.state not in [state for state in
                                                                                            explored_set]:
                heapq.heappush(frontier, child)
            for node in frontier:
                if child.state == node.state:
                    if child.path_cost < node.path_cost:
                        frontier.remove(node)
                        heapq.heappush(frontier, child)  # not sure


def a_star(problem):
    frontier = []
    heapq.heappush(frontier, Node(problem.init_state, None, 0))
    explored_set = []
    while True:
        if len(frontier) <= 0:
            return 'FAIL'
        current_node = heapq.heappop(frontier)
        if problem.goal_test(current_node.state):
            solution = get_solution(current_node)
            return solution
        explored_set.append(current_node.state)
        for action, destination in problem.get_possible_actions(current_node.state):
            child = expand(parent=current_node, destination=destination, action=action, goal_state=problem.goal_state,
                           algorithm='A_STAR')
            if child.state not in [node.state for node in frontier] and child.state not in [state for state in
                                                                                            explored_set]:
                heapq.heappush(frontier, child)
            for node in frontier:
                if child.state == node.state:
                    if child.path_cost < node.path_cost:
                        frontier.remove(node)
                        heapq.heappush(frontier, child)  # not sure
