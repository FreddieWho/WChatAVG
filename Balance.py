#卡方分布——画图
#导入需要的包
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.style as style
# from IPython.core.display import HTML

#PLOTTING CONFIG 绘图配置
%matplotlib inline
style.use('fivethirtyeight')
plt.rcParams['figure.figsize']=(4,2)
plt.figure(dpi=100)

#PDF  概率密度函数
plt.plot(np.linspace(0,10,100),np.full(100,10)-sorted(stats.chi2.rvs(2,size = 100)))
plt.plot(np.linspace(0,10,100),sorted(stats.chi2.rvs(2,size = 100)))
plt.plot(np.linspace(0,10,100),np.full(100,10)-sorted(stats.norm.rvs(2,size = 100)))


plt.fill_between(np.linspace(0,20,100),stats.chi2.pdf(np.linspace(0,20,100),df=4),alpha=0.15) #填充曲线

#CDF 累积概率密度函数
plt.plot(np.linspace(0,20,100),stats.chi2.cdf(np.linspace(0,20,100),df=4)) #绘制累积概率密度函数

#LEGEND 图例
plt.text(x=11,y=0.25,s="pdf(normed)",alpha=0.75,weight="bold",color="#008fd5")
plt.text(x=11,y=0.85,s="cdf",alpha=0.75,weight="bold",color="#fc4f30")

#Ticks 坐标轴
plt.xticks(np.arange(0,21,2))
plt.tick_params(axis="both",which="major",labelsize=18)
plt.axhline(y=0,color="black",linewidth=1.3,alpha=.7)
