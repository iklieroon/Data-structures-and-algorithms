class Graph:
    def __init__(self,n):
        self.n=n
        self.adj=[[]  for i in range(n)]
    def createedge(self,x,y):
        self.adj[x-1].append(y-1)
        self.adj[y-1].append(x-1)
    def dfs1(self,source,visited,result): #dfs id a recursive function
        result.append(source)
        visited[source]=True
        for node in self.adj[source]:
            if visited[node]==False:
                self.dfs1(node,visited,result)
    def dfs(self,source):
        visited=[False]*self.n
        result=[]
        self.dfs1(source,visited,result)
        return result

n=int(input("How many nodes in the graph?"))
g=Graph(n)
m=int(input("How many edges in the graph?"))
for i in range(m):
    x,y=map(int,list(input().split()))
    g.createedge(x,y)
r=g.dfs(1)
print(r)