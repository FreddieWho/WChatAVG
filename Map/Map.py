class Block:
    def __init__(self, id):
        self.Id = id
        self.Connected2 = {}

    def addNeighbor(self, nbr, distence):
        self.Connected2[nbr] = weight

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

    def addBlock(self,id):
        self.numBlock = self.numBlock + 1
        newBlock = Block(id)
        self.BlockList[id] = newBlock
        return newBlock
    
    def getBlock(slef,n)