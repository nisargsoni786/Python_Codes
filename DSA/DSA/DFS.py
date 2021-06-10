matrix=[[0,1,0,1],[0,0,1,1],[1,0,0,1],[0,0,0,0]]
visited=[0,0,0,0]

visited[0]=1
queue=[0]
node=queue.pop()
print(node,end=" ")

while True:
    for i in range(len(visited)):
        if matrix[node][i]==1 and visited[i]==0:
            visited[i]=1
            queue.append(i)

    if len(queue)==0:
        break
    else:
        node=queue.pop()
        print(node,end=" ")