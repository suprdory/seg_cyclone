def calc_seg_params(r0,rs,dt):
    import numpy as np 
    # y = a + b * exp(r * t)
    a=0
#    dt=0.1
#    r0=0.2#0.1848/dt
#    rs=0.2#0.2/dt
    
    nt=20
    ns=1000
    b=np.random.randn(ns)*0.1+.4;
  
       
    y=np.zeros([nt,ns])
    for s in range(0,ns):
        #r=r0+rn[s]*rs
        y[0,s]=a+b[s]
        for t in range(1,nt):
            r=r0+np.random.randn(1)*rs/dt
            y[t,s]=y[t-1,s]+(y[t-1,s]-a)*r*dt
    
    t=np.arange(0,nt)*dt
    ly=np.log(y)

    pfit=np.polyfit(t,ly,1)
    py=np.empty([nt,ns])
    for i in range(ns):
        py[:,i]=np.polyval(pfit[:,i].T,t)
        
    res=ly-py 
    sigres=np.std(res,0)
    
    msigres=np.mean(sigres)
    mgr=np.mean(pfit[0,:])  

    return (mgr,msigres)     
        
#==============================================================================
#     p.figure(2)
#     p.clf()
#     p.subplot(311)
#     p.plot(ly[:,:])
#     p.title('time series')
#     p.subplot(312)
#     p.plot(py)
# 
#     p.subplot(313)
#     p.plot(res)
#==============================================================================
   
    # %matplotlib qt
