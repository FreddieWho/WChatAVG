import networkx as nx
import numpy as np
import pandas as pd


# zawaludo!
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


class Block:
    def __init__(self, id):
        self.Id = id



