import numpy as np
from scipy import stats
import time


class Attribution():
    def __init__(self, Name, *Class, Level, Distribution, **kwargs):
        self.Name = Name
        self.Class = Class
        self.Level = Level
        self.Distribution = Distribution

        Attr_names = self.__dict__
        for ArgNames in kwargs.keys():
            Attr_names[ArgNames] = kwargs[ArgNames]

    def output(self):
        if self.Distribution == 'None':
            return self.Level
        elif self.Distribution == 'truncNorm':
            distFunc = stats.truncnorm(
                self.low, self.high, self.mean, self.sigma)
            return distFunc.rvs(1)


class ExpLevel():
    @staticmethod
    def test(Player):
        print(Player.ExpPool)

    @staticmethod
    def use(Player, speed=1, vebose=True):

        print(u'获得了' + str(speed) + u'点经验')

        for i in range(speed):
            ExpPool_array = np.append(np.zeros(Player.ExpPool), 1)
            UpLevel = int(np.random.choice(ExpPool_array, 1).sum())
            if UpLevel == 1:
                Player.Level = Player.Level + 1
                print(u'duang,' + Player.Name + u'升了' + str(UpLevel) + u'级')
                Player.ExpPool = 99
            else:
                Player.ExpPool = Player.ExpPool-1

class Distribution():
    @staticmethod
    def Unif(x):
        return(x*10)

    @staticmethod
    def Critical(x)
        rand = np.random.choice(np.linspace(0,1,1000), 1)
        y = np.exp(4-5.3*rand)        
        return(x * y)

    @staticmethod
    def Norm(x):
        
