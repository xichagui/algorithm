class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        tree = [[] for _ in range(N)]
        for node, child in edges:
            tree[node].append(child)
            tree[child].append(node)
        depth = [0 for _ in range(N)]
        count = [0 for _ in range(N)]
    
        def dfs_for_depth_and_count(node, parent):
            count[node] = 1
            for child in tree[node]:
                if child != parent:
                    depth[child] = depth[node] + 1
                    dfs_for_depth_and_count(child, node)
                    count[node] += count[child]

        dfs_for_depth_and_count(0, -1)

        answer = [0 for _ in range(N)]
        answer[0] = sum(depth)

        def dfs_for_answer(node, parent):
            for child in tree[node]:
                if child != parent:
                    answer[child] = answer[node] + N - 2 * count[child]
                    dfs_for_answer(child, node)

        dfs_for_answer(0, -1)
        return answer
