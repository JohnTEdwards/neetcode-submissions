class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = list(range(n))
        rank = [1] * n

        def find(node):
            result = node
            while result != par[result]:
                par[result] = par[par[result]]
                result = par[result]
            return result

        def union(n1, n2):
            parent_node1, parent_node2 = find(n1), find(n2)

            if parent_node1 == parent_node2:
                return 0
            if rank[parent_node1] > rank[parent_node2]:
                par[parent_node2] = parent_node1
                rank[parent_node1] += rank[parent_node2]
            else:
                par[parent_node1] = parent_node2
                rank[parent_node2] += rank[parent_node1]
            return 1

        result = n
        for n1, n2 in edges:
            result -= union(n1,n2)
        return result        