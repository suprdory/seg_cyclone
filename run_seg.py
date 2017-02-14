import numpy as np
import matplotlib.pyplot as p
import calc_seg_params

def main():
    #%%
    dt=6
    nr0=10
    nrs=10
    
    r0=np.linspace(0.00, .1,nr0)
    segp=np.empty([nr0,2])
    for i in range(nr0):
        segp[i]=calc_seg_params.calc_seg_params(r0[i],.02,dt)
        
    p.figure(1);p.clf();
    ax=p.subplot(211)
    p.plot(r0,segp[:,0])
    p.xlabel('r0')
    p.ylabel('r0_sim')
    add_identity_line(ax)
    
    rs=np.linspace(0.001,.1,nrs)
    segp=np.empty([nrs,2])
    for i in range(nrs):
        segp[i]=calc_seg_params.calc_seg_params(.0308,rs[i],dt)
        
    
    ax=p.subplot(212)
    p.plot(rs,segp[:,1]) 
    add_identity_line(ax)
    p.xlabel('rs')
    p.ylabel('rs_sim')

#%%
def add_identity_line(ax):
    lims = [
        np.min([ax.get_xlim(), ax.get_ylim()]),  # min of both axes
        np.max([ax.get_xlim(), ax.get_ylim()]),  # max of both axes
    ]
    # now plot both limits against eachother
    ax.plot(lims, lims, 'k-', alpha=0.75, zorder=0)
    ax.set_aspect('equal')
    ax.set_xlim(lims)
    ax.set_ylim(lims)
    
main()