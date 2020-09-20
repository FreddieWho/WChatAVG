#卡方分布——画图
#导入需要的包
import numpy as np
import scipy.stats as stats
import sympy as sym
import matplotlib.pyplot as plt
import matplotlib.style as style
from scipy.integrate import tplquad,dblquad,quad
# from IPython.core.display import HTML

#PDF  概率密度函数
plt.plot(np.linspace(0,10,100),np.full(100,10)-sorted(stats.chi2.rvs(2,size = 100)))
plt.plot(np.linspace(0,10,100),sorted(stats.truncexpon.pdf(0.22,np.linspace(0,10,100))))
plt.plot(np.linspace(0,10,100),sorted(stats.truncexpon.rvs(1000,size = 100)))
plt.plot(np.linspace(0,10,100),sorted(stats.expon.pdf(1,np.linspace(0,10,100))))
plt.plot(np.linspace(0,10,100),sorted(stats.expon.rvs(1000,size = 100)))


X = stats.truncnorm(-5, 5, loc=10, scale=1)
plt.plot(np.linspace(0,10,1000),sorted(X.rvs(size = 1000)))
    
x = sym.symbols('x')
f = sym.Piecewise((exp(x) + 3.2 + 0.3*exp(1),x > 0.5), (exp(1-x) + 3.3 + 0.4*exp(1),True))
sym.integrate(f,(x,0,1))

def Critical():
    x = np.random.choice(np.linspace(0,1,1000), 1)
    y = np.exp(4-5.37*x)        
    return(y)

plt.plot(np.linspace(0,10,100),sorted([Critical() for t in np.linspace(0,1,100)]))

quad(Critical,0,1)

