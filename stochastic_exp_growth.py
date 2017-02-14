import numpy as np
import matplotlib.pyplot as p
from scipy import stats
# y = a + b * exp(r * t)

a=0
dt=0.1
r0=0.2#0.1848/dt
rs=0.2#0.2/dt


nt=17
ns=10
b=np.random.randn(ns)*0.1+.4;

#b=np.ones(ns)
#rn=np.random.randn(ns)

y=np.zeros([nt,ns])
sh=np.zeros([2,nt])
shl=np.zeros([2,nt])
for s in range(0,ns):
    #r=r0+rn[s]*rs
    y[0,s]=a+b[s]
    for t in range(1,nt):
        r=r0+np.random.randn(1)*rs
        y[t,s]=y[t-1,s]+(y[t-1,s]-a)*r*dt

for t in range(0,nt):
    sh[:,t]=stats.shapiro(y[t,:])
    shl[:,t]=stats.shapiro(np.log(y[t,:]))
    
#==============================================================================
# p.figure(1)
# p.clf()
# p.subplot(311)
# p.plot(y[:,:])
# p.title('time series')
# 
# ax=p.subplot(334)
# p.hist(y[0,:],normed=True,bins=20)
# p.title('initial pdf')
# p.text(0.01, .95, 'W=' + ('%.4f' % sh[0,0]), transform=ax.transAxes)
# p.text(0.01, .90, 'P=' + ('%.4f' % sh[1,0]), transform=ax.transAxes)
# 
# ax=p.subplot(335)
# p.hist(y[-1,:],normed=True,bins=20)
# p.title('final pdf')
# p.text(0.010, .95, 'W=' + ('%.4f' % sh[0,-1]), transform=ax.transAxes)
# p.text(0.01, .90, 'P=' + ('%.4f' % sh[1,-1]), transform=ax.transAxes)
# 
# ax=p.subplot(336)
# logy=np.log(y[-1,:])
# p.hist(logy[~np.isnan(logy)],normed=True,bins=20)
# p.title('log(final) pdf')
# p.text(0.01, .95, 'W=' + ('%.4f' % shl[0,-1]), transform=ax.transAxes)
# p.text(0.01, .90, 'P=' + ('%.4f' % shl[1,-1]), transform=ax.transAxes)
# 
# ax=p.subplot(313)
# p.plot(sh[1,:])
# p.plot(shl[1,:])
# p.title('Shapiro-Wilks P-value')
# p.legend(['y','log(y)'])
# 
# p.show()
#==============================================================================


ly=np.log(y)
p.figure(2)
p.clf()
p.subplot(311)
p.plot(ly[:,:])
p.title('time series')

t=np.arange(0,nt)*dt
pfit=np.polyfit(t,ly,1)
py=np.empty([nt,ns])
for i in range(ns):
    py[:,i]=np.polyval(pfit[:,i].T,t)
    
p.subplot(312)
p.plot(py)
res=ly-py
p.subplot(313)
p.plot(res)
sigres=np.std(res,0)

msigres=np.mean(sigres)
mgr=np.mean(pfit[0,:])
# %matplotlib qt
