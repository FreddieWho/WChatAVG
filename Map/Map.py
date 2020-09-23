

# zawaludo!
# a graph object constructed by networkx
class TheWorld:
    def __init__(self,BlockNum = 5, MaxDist = 5):
        iLocation = pd.read_csv('data/i_diming.csv', sep=',', header=None)
        
        adjMtx = np.random.randint(0, MaxDist, (BlockNum, BlockNum))
        np.fill_diagonal(adjMtx, 0)
        g = nx.convert_matrix.from_numpy_matrix(adjMtx)
        
        for i in g.nodes:
            g.add_node(i,Block = Block(id = iLocation[0][i]))
        
        self.dict = dict(zip(list(range(len(g))),iLocation[0]))
        self.graph = g


class Block:
    def __init__(self, id):
        self.Id = id



