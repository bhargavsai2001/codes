def printPath(parent, vertex):
    if vertex < 0:
        return
    
    printPath(parent, parent[vertex])
    print(vertex, end=' ')
    
def bellmanFord(edges, source, N):
    distance= [float('inf')]*N
    parent=[-1]*N
    distance[source]=0
    
    for k in range(N-1):
        for (u,v,w) in edges:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                parent[v] = u
    for(u,v, w) in edges:
        if distance[u] + w < distance[v]:
            print("Negative Weight Cycle Found!!")
            return
                
    for i in range(N):
        print("Distance of vertex", i, "from the source is",distance[i],end='.')
        print("It's path is [", end='')
        printPath(parent, i)
        print("]")

if name == 'main':
    edges=[
        (0,1,-1),(0,2,4),(1,2,3),(1,3,2),
        (1,4,2),(3,2,5),(3,1,1),(4,3,-3)
    ]
    
    N=5
    source=0
    bellmanFord(edges, source, N)
