class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            result = node
            
            while result != parents[result]:
                parents[result] = parents[parents[result]]
                result = parents[result]
            return result
        
        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)

            if parent1 == parent2:
                return 0
            
            if rank[parent1] > rank[parent2]:
                parent1, parent2 = parent2, parent1
            parents[parent2] = parent1
            rank[parent1] += rank[parent2]
            return 1

        answer = n
        for node1,node2 in edges:
            answer -= union(node1, node2)
        return answer
        