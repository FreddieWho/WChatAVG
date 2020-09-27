import utils.keyboard
from character.Attribute import ExpLevel
import _thread
import numpy as np
import 


class Player:
    def __init__(self):
        # basic attributions
        self.Level = 1
        self.ExpPool = 99
        self.HP = 100
        self.MP = 100

        self.DamageIndex = 1+getattr(self, 'Level')*0.1

        # self.MagicDamage = 3
        # self.PhysicDamage = 3

        self.MagicDefence = 1
        self.PhysicDefence = 1

        self.Accuracy = 0.9
        self.Evade = 0.1

        self.Position = np.random.randint(0, len(WorldMap.graph), size=1)

        self.timeStamp = time.time()

    def create(self):
        if hasattr(self, 'Name'):
            print(u'你已经创建了角色')
        else:
            print(u'Welcome To The Oasis')
            print(u'你的名字是：')
            self.Name = input()
            print(u'你的职业是：')
            self.Character = input()
            print(u'你的外形是：：')
            self.Look = input()
            print(u'你的长相是：')
            self.Appearence = input()

            print(u'角色创建完成')
    
    def move(self,to):
        path = (self.Position,WorldMap.dict[to])

        if path in WorldMap.graph.edges:
            dist = WorldMap.graph.edges
        else:
            dist = WorldMap.graph.edges[path]['weight']
        
        if 

        delay = 
        tmpTimeStamp = time.time()

        if tmpTimeStamp - self.TimeStamp > delay:
            # move func
        else:


        _thread.start_new_thread( print_time, (context, 4) )


