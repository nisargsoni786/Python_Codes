def minkey(g,key,mstset):
    min=99999
    v=len(g)
    for i in range(v):
        if key[i]<min and mstset[i]==False:
            min=key[i]
            min_ind=i
    return min_ind

def printMST(g,parent):
    v=len(g)
    for i in range(1,v):
        print(str(parent[i]) + "-" + str(i) + "\t"+ str(g[i][ parent[i] ]))

def prims(g):
    v=len(g)
    key=[99999]*v
    parent=[None]*v
    key[0]=0
    parent[0]=-1
    mstset=[False]*v

    for cout in range(v):
        u=minkey(g,key,mstset)
        mstset[u]=True
        for i in range(v):
            if g[u][i]>0 and mstset[i]==False and key[i]>g[u][i]:
                key[i]=g[u][i]
                parent[i]=u
    printMST(g,parent)

g=[ [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0] ]
prims(g)