class Graph:
    def __init__(self,n):
        self.n=n
        self.adj=[[]*n for i in range(n)] #adj=adjecency list
    def createedge(self,x,y):
        self.adj[x-1].append(y-1)
        self.adj[y-1].append(x-1)
    def bfs(self,source):
        visited=[False]*self.n
        result=[]
        queue=[]
        queue.append(source)
        visited[source]=True
        while len(queue)>0:
            s=queue.pop(0)
            result.append(s)
            for node in self.adj[s]:
                if visited[node]==False:
                    queue.append(node)
                    visited[node]=True
        return result

g=Graph(4)
g.createedge(1,2)
g.createedge(1,3)
g.createedge(2,4)
print(g.bfs(0))