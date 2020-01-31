from utility import read_input_file
from problem import Problem
from algorithms import ucs, bfs, a_star

if __name__ == '__main__':
    input_dict = read_input_file()
    for key, value in input_dict.items():
        print(key, value, sep=':')
    for target in input_dict['targets']:
        problem = Problem(init_state=input_dict['state_grid'][input_dict['landing_site'][1]][input_dict['landing_site'][0]],
                          state_space=input_dict['state_grid'],
                          goal_state=input_dict['state_grid'][target[1]][target[0]],
                          actions=['E', 'W', 'N', 'S', 'NE', 'SE', 'SW', 'NW'],
                          max_elev_diff=input_dict['max_elevation_diff'])
        # print(problem)
        if input_dict['algorithm'].lower() == 'bfs':
            print(bfs(problem))
        elif input_dict['algorithm'].lower() == 'ucs':
            print(ucs(problem))
        else:
            print(a_star(problem))
