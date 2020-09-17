class UnionFind:
    def __init__(self, n):
        self.ancestor = list(range(n))
        
    def union(self, index1: int, index2: int):
        self.ancestor[self.find(index1)] = self.find(index2)
    
    def find(self, index):
        if self.ancestor[index] != index:
            self.ancestor[index] = self.find(self.ancestor[index])
        return self.ancestor[index]
    
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        l = len(edges)
        uf = UnionFind(l + 1)
        parent = list(range(l + 1))
        conflict = -1
        cycle = -1
        
        for i, [node1, node2] in enumerate(edges):
            """
                当前如果发现冲突边, 则不加入并查集. 标记为冲突边
                如果不加入冲突边的情况下没有发现环, 这删除冲突边
                如有冲突边的情况下还有环存在, 则删除冲突点所在环的边.
                
            """ 
            
            if parent[node2] != node2:
                conflict = i
            else:
                parent[node2] = node1
                if uf.find(node1) == uf.find(node2):
                    cycle = i
                else:
                    uf.union(node1, node2)
        
        if conflict < 0:
            return edges[cycle]
        else:
            if cycle < 0:
                return edges[conflict]
            else:
                return [parent[edges[conflict][1]], edges[conflict][1]]
