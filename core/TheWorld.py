# zawaludo!

import networkx as nx
import numpy as np
import pandas as pd

# a graph object constructed by networkx
class TheWorld:
    def __init__(self, BlockNum=5, MaxDist=5):
        iLocation = pd.read_csv('data/i_diming.csv', sep=',', header=None)

        adjMtx = np.random.randint(0, MaxDist, (BlockNum, BlockNum))

        np.fill_diagonal(adjMtx, 1)
        # make the mtx symmertry
        adjMtx = np.triu(adjMtx)
        adjMtx += adjMtx.T - np.diag(adjMtx.diagonal())
        g = nx.convert_matrix.from_numpy_matrix(adjMtx)

        for i in g.nodes:
            g.add_node(i, Block=Block(id=iLocation[0][i]))

        self.dict = dict(zip(iLocation[0], list(range(len(g)))))
        self.graph = g


class CharactorPool:
    def __init__(self, id):
        self.charaNum=input()

        while 1:
            if not isinstance(self.charaNum,int) :
                print(u'---请正确输入玩家人数---')
                self.charaNum = input()
            elif self.charaNum < 3 or self.charaNum > 10:
                print(u'---请正确输入玩家人数---')
                self.charaNum = input()
                break

        if self.charaNum < 4:
            chara_list = ['spy'] * 1 + ['citizen'] * (n-1)
        elif 4 < self.charaNum < 7:
            chara_list = ['spy'] * 2 + ['police'] * 1 + ['citizen'] * (n-2)
        elif 6 < self.charaNum < 9:
            chara_list = ['spy'] * 3 + ['police'] * 1 + ['citizen'] * (n-2)
        elif 8 < self.charaNum:
            chara_list = ['spy'] * 4 + ['police'] * 1 + ['citizen'] * (n-2)

        self.chara_pool = dict(zip(np.linspace(1, n, num=n, dtype=str), chara_list))

    def die():
        