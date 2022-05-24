#########################################################################################


#                                   States                                              #

#########################################################################################


import copy
from termcolor import colored


class States:
    n = 5
    m = 5
    t=True
    dimension=5

    def __init__(self, grid, parent, livel, cost, new):
        self.grid = grid
        self.cost = cost
        self.livel = livel
        self.parent = parent
        self.new = new


    def is_woin(self,player):
        win = None

        # checking rows
        for i in range(self.dimension):
            win = True
            for j in range(self.dimension):
                if self.grid[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(self.dimension):
            win = True
            for j in range(self.dimension):
                if self.grid[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking main diagonals
        win = True
        for i in range(self.dimension):
            if self.grid[i][i] != player:
                win = False
                break
        if win:
            return win

        # checking second diagonals
        win = True
        for i in range(self.dimension):
            if self.grid[i][self.dimension - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False
    def gool(self):
            return self.livel ==4

    def get_number_empty_cells(self):
        num = 0
        for i in range(5):
            for j in range(5):
                if self.grid[i][j] == '-':
                    num += 1
        print(num)
        return num

    def __eq__(self, other):

        return self.grid == other.grid

    def next_states(self):
        l = []

        for i in range(5):
            for j in range(5):

                if self.grid[i][j] == '-':

                    if self.livel % 2 == 0:
                        newS = copy.deepcopy(self)
                        newS.livel = self.livel + 1
                        newS.parent = self
                        newS.grid[i][j] = 'X'
                        newS.new = [i, j]
                    else:
                        newS = copy.deepcopy(self)
                        newS.parent = self
                        newS.livel = self.livel + 1
                        newS.grid[i][j] = 'O'
                        newS.new = [i, j]

                    l.append(newS)

        return l

    def print_gride(self):
        print(colored('=' * 32), end="")
        for n, i in enumerate(self.grid):
            print('')

            for j in i:
                print("{:^6}".format(j), end='')

            print('|', end='')

        print()
        print(colored('=' * 32))

    def c_Row(self, t,i):
        c = 0
        temp = True
        n = 0
        for j in range(5):
                if self.grid[i][j] == '-':
                    pass
                elif self.grid[i][j] == t:
                    n = n + 1
                else:
                    temp = False
                    # c = c - 1
                    n=0
                    break
        return n

    def c_column(self, t,j):
        c = 0
        n = 0
        temp = True
        for i in range(5):

                if self.grid[i][j] == '-':
                    pass
                elif self.grid[i][j] == t:
                    n = n + 1
                    pass
                else:
                    temp = False
                    n=0
                    # c = c - 1
                    break

        return n


    def c_l(self, t):
        c = 0
        n = 5

        for i in range(5):
            for j in range(5):
                if i == j:
                    if self.grid[i][j] == '-':
                        pass
                    elif self.grid[i][j] == t:
                        c=c+1
                        pass
                    else:
                        c=0
                        break
        return c

    def c_r(self, t):
        c = 0
        n = 5
        for i in range(5):
            for j in range(5):
                if i + j == 4:

                    if self.grid[i][j] == '-':
                        pass
                    elif self.grid[i][j] == t:
                        c = c + 1
                        pass
                    else:
                        n = n - 1
                        break

        return c


    def pr(self,t):

            if self.new!=None:
                if self.new[0]==self.new[1]:
                    return self.c_l(t)
                if self.new[0]+self.new[1]==4:
                    return self.c_r(t)
            return  self.c_Row(t,self.new[0])+self.c_column(t,self.new[1])
        # else:
        #     if self.new != None:
        #         if self.new[0] == self.new[1]:
        #             return -self.c_l(t)
        #         if self.new[0] + self.new[1] == 4:
        #             return -self.c_r(t)
        #     return -self.c_Row(t, self.new[0]) + self.c_column(t, self.new[1])


            # return -self.c_r(t) + self.c_l(t) + self.c_Row(t) + self.c_column(t)