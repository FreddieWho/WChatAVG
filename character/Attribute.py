import numpy as np
from scipy import stats
import time


class Attribution():
    def __init__(self, Name, Class, Level, Distribution, **kwargs):
        self.Name = Name
        self.Class = Class
        self.Level = Level
        self.Distribution = Distribution

        Attr_names = self.__dict__
        for ArgNames in kwargs.keys():
            Attr_names[ArgNames] = kwargs[ArgNames]

    def output():
        if self.Distribution == 'None':
            return Level
        elif self.Distribution == 'truncNorm':
            distFunc = stats.truncnorm(low, high, mean, sigma)
            return distFunc.rvs(1)


class ExpLevel():
    def __init__(self, ExpPool_Size=99, Speed=1, Level=0):
        self.ExpPool = np.append(np.zeros(ExpPool_Size), 1)
        self.Speed = Speed
        self.Level = Level
        # 解决类的name的继承问题
        self.Name = Name

    # 注意检查speed大于ExpPool_Size时的期望
    def use(speed=self.speed, vebose=T):
        np.random.seed(round(time.time()))
        if np.random.choice(self.ExpPool, self.speed).sum == 1:
            self.Level = self.Level + 1
            print(u'duang,' + self.Name + u'升级了')
        else:
            if vebose:
                print(u'获得了' + speed + u'点经验')
            self.ExpPool = self.ExpPool[self.speed:]

    def get(getExp):
        for i in range(getExp):
            self.use(speed=getExp)
