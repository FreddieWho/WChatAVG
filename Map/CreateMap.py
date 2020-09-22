import networkx as nx
import numpy as np
import pandas as pd

diming = pd.read_csv('data/THUOCL_diming.txt', sep='\t', header=None)




def RandomWorld(BlockNum=5, MaxDist=5):
    adjMtx = np.random.randint(0, MaxDist, (BlockNum, BlockNum))
    np.fill_diagonal(adjMtx, 0)
    graph = nx.convert_matrix.from_numpy_matrix(adjMtx)
    return graph

class Block:
    def __init__(self, id):
        self.Id = id


