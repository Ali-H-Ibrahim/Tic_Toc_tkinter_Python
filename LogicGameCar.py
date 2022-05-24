#########################################################################################
#                                   Logic                                               #
#########################################################################################

import sys
import math
import states as s

sys.setrecursionlimit(4000)


class Game:

    def __init__(self, bs):

        self.bs = bs
        self.l = []
        self.sul = 0
        self.cont = 0
        self.visited_states = []
        self.goul = None
        self.list = []

    def eqal(self, b1, b2):
        if b1 == b2:
            return True
        else:
            return False


    # ****************************DFS*******************************



    def c_h(self, state, t):
        c = 0

        temp = True
        n = 0
        for i in range(5):
            temp = True
            for j in range(5):
                if state.grid[i][j] == '-':
                    pass
                elif state.grid[i][j] == t:
                    n = n + 1
                    pass
                else:
                    temp = False
                    # c = c - 1
                    break
            if temp:
                c = c + 1
        return c


    def c_v(self, state, t):
        c = 0
        n = 0
        temp = True
        for i in range(5):
            temp = True

            for j in range(5):
                if state.grid[j][i] == '-':
                    pass
                elif state.grid[j][i] == t:
                    pass
                else:
                    temp = False
                    # c = c - 1
                    break
            if temp:
                c = c + 1
        return c

    def c_l(self, state, t):
        c = 0
        n = 5

        for i in range(5):
            for j in range(5):
                if i == j:
                    if state.grid[i][j] == '-':
                        pass
                    elif state.grid[i][j] == t:
                        pass
                    else:
                        n = n - 1
        if n == 5:
            c = c + 1
        return c

    def c_r(self, state, t):
        c = 0
        n = 5
        for i in range(5):
            for j in range(5):
                if i + j == 4:

                    if state.grid[i][j] == '-':
                        pass
                    elif state.grid[i][j] == t:
                        pass
                    else:
                        n = n - 1

        if n == 5:
            c = c + 1

        return c

    def e_t(self, state, t):
        c = self.c_l(state, t) + self.c_r(state, t) + self.c_v(state, t) + self.c_h(state, t)
        return c

    def eval_f(self, state):
        if state.is_woin('X'):
            return +math.inf
        if state.is_woin('O'):
            return -math.inf

        return self.e_t(state, 'X') - self.e_t(state, 'O')

    def min_max(self, state):

        if state.livel == 1:
            self.list.append(state)

        if state.gool():

            self.cont += 1
            state.cost = self.eval_f(state)

            print(self.cont)
            return 1
        next_state = state.next_states()

        for ch_state in next_state:

            if self.min_max(ch_state) == 1:
                if state.livel % 2 == 0:

                    if state.cost < ch_state.cost:
                        print("cost")
                        print(ch_state.cost)
                        ch_state.print_gride()
                        state.cost =  ch_state.cost
                        state.new =  ch_state.new

                else:

                    if state.cost > ch_state.cost:

                        state.cost = ch_state.cost

        state.cost=state.cost
        return 1


    def alfa_beta(self,state,alpha = -math.inf, beta = +math.inf):

        if state.livel == 1:
            self.list.append(state)

        if state.gool():
            self.cont += 1
            state.cost = self.eval_f(state)

            print(self.cont)
            return 1

        next_state = state.next_states()

        for ch_state in next_state:

            if self.alfa_beta(ch_state) == 1:
                best=-math.inf

                if state.cost < ch_state.cost:
                        print("cost")
                        print(ch_state.cost)
                        state.cost =  ch_state.cost

                if state.livel % 2 == 0:
                    if state.cost < ch_state.cost:
                        print("cost")
                        print(ch_state.cost)
                        state.cost = ch_state.cost
                    best = max(best,ch_state.cost)
                    alpha = max(alpha,best)
                    if beta <= alpha:
                        break
                else:
                    if state.cost > ch_state.cost:
                        print("cost")
                        print(ch_state.cost)
                        state.cost = ch_state.cost
                    best = -math.inf

                    best = min(best,ch_state.cost)
                    beta = min(beta, best)
                    if alpha >= beta:

                        break


        state.cost=state.cost
        return 1






    def game(self):

        pass

    def p(self):

        c = self.list[0]
        if c.livel % 2 != 0:
            # ch_state.print_gride()
            n = c.pr('X')

        else:
            n = - c.pr('O')
        print("*" * 30)
        for i in self.list:
            i.print_gride()

            if i.is_woin('X'):
                return i
            next_states= i.next_states()
            for inext_states in next_states:
                if inext_states.is_woin('O'):
                    return inext_states

            if i.livel % 2 != 0:
                m = i.pr('X')

            else:
                m = - i.pr('O')
            if i.cost +m  > c.cost  +n:
                print(i.cost)
                c = i

        self.list = []
        print(c.cost)
        c.print_gride()

        return c
