import pulp as p
import app


class LinerProgramming(object):

    variables = {'varX': [], 'varC': []}
    LpProblem = p.LpProblem('problema', p.LpMaximize)

    def __init__(self, arr):
        self.arr = arr

    def take_LP_data(self):
        return self.arr

    def create_vars(self):
        len_arr = len(self.arr) + 1

        for u in range(0, len_arr):
            self.variables['varC'].append(p.LpVariable(
                name='c{}'.format(u), cat='Integer', lowBound=0))

        for x in range(0, len_arr):
            if x != 0:
                self.variables['varX'].append(p.LpVariable(
                    name='x{}_{}'.format(x, 0), cat='Binary'))

            for i in range(0, x+1):
                if x != i:
                    self.variables['varX'].append(p.LpVariable(
                        name='x{}_{}'.format(x, i), cat='Binary'))

            for a in range(x+1, len_arr):
                self.variables['varX'].append(p.LpVariable(
                    name='x{}_{}'.format(x, a), cat='Binary'))
