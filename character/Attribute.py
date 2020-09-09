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
            distFunc = stats.truncnorm(self.low, self.high, self.mean, self.sigma)
            return distFunc.rvs(1)


class ExpLevel():
    @staticmethod
    def test(Player):
        print(Player.ExpPool)

    @staticmethod
    # 注意检查speed大于ExpPool_Size时的期望
    def use(Player, speed = 1, vebose=True):

        print(u'获得了' + str(speed) + u'点经验')
        
        np.random.seed(round(time.time()))

        ExpPool_array = np.append(np.zeros(Player.ExpPool),1)
        UpLevel = int(np.random.choice(ExpPool_array, speed).sum())
        if UpLevel >= 1:
            Player.Level = Player.Level + UpLevel
            print(u'duang,' + Player.Name + u'升了' + str(UpLevel) + u'级')
            Player.ExpPool = 99
        else:
            if speed > Player.ExpPool + 1:
                Player.Level = Player.Level + 1
                Player.ExpPool = 99
            else:
                Player.ExpPool = Player.ExpPool-speed
