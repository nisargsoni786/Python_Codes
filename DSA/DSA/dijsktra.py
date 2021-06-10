def mindist(g,sptset,dist):
    min=99999
    for i in range(len(g)):
        if sptset[i]==False and dist[i]<min:
            min=dist[i]
            ans=i
    return ans

def dijkshtra(g,src):
    v=len(g)
    dist=[99999]*v
    dist[src]=0
    sptset=[False]*v
    for count in range(v):
        u=mindist(g,sptset,dist)
        sptset[u]=True
        for i in range(v):
            if g[u][i]>0 and sptset[i]==False and dist[i]>(dist[u]+g[u][i]):
                dist[i]=dist[u]+g[u][i]
    return dist

g=[     [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
print(dijkshtra(g,0))