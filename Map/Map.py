class Block:
    def __init__(self, id):
        self.Id = id
        self.Connected2 = {}

    def addNeighbor(self, nbr, distance):
        self.Connected2[nbr] = distance

    def getConnections(self):
        return self.Connected2.keys()

    def getId(self):
        return self.Id

    def getDistence(self, nbr_id):
        return self.Connected2[nbr_id]


class GlobalMap:
    def __init__(self):
        self.BlockList = {}
        self.numBlock = 0

    def addBlock(self,Block):
        self.numBlock = self.numBlock + 1

        if type(Block).__name__ == 'Block':
            newBlock = Block
            id = Block.Id
        else:
            newBlock = Block(id)
            
        self.BlockList[id] = newBlock
        return newBlock
    
    def getBlock(self,n):
        if n in self.BlockList:
            return self.BlockList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.BlockList
    
    def addEdge(self,fromId,toId,distance = 0):
        if fromId not in self.BlockList:
            nv = self.addBlock(fromId)
        if toId not in self.BlockList:
            nv = self.addBlock(toId)

        self.BlockList[fromId].addNeighbor(self.BlockList[toId],distance)
    
    def getEdge(self):
        return self.BlockList.keys()

    def __iter__(self):
        return iter(self.BlockList.values())

g = GlobalMap()
for i in range(6):
    g.addBlock(i)

g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
for v in g:
   for w in v.getConnections(): 
      print("( %s , %s , %s )" % (v.getId(), w.getId(),w.Connected2))
