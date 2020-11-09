# class Solution:
#     def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
#         if K >= len(points):
#             return points
        
#         heap = [[10000, 10000, 10000 * 10000 * 2]] * K
                
#         for i in range(0, len(points)):
            
#             temp = points[i][0] ** 2 + points[i][1] ** 2

#             if temp > heap[0][2]:
#                 continue
#             else:
#                 heap[0] = points[i] + [temp]
            
#             cur_index = 0
#             while cur_index * 2 + 1 <= K - 1:
#                 left_child_index = cur_index * 2 + 1
#                 right_child_index = cur_index * 2 + 2
#                 flag = 0
#                 if heap[left_child_index][2] > heap[cur_index][2]:
#                     flag = 1
#                 if right_child_index <= K - 1 and heap[right_child_index][2] > heap[left_child_index][2]:
#                     if heap[right_child_index][2] > heap[cur_index][2]:
#                         flag = 2
                
#                 if flag == 1:
#                     heap[cur_index], heap[left_child_index] = heap[left_child_index], heap[cur_index]
#                     cur_index = left_child_index
#                 elif flag == 2:
#                     heap[cur_index], heap[right_child_index] = heap[right_child_index], heap[cur_index]
#                     cur_index = right_child_index
#                 else:
#                     break
        
#         return [[node[0], node[1]] for node in heap]

import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        q = [(-x ** 2 - y ** 2, i) for i, (x, y) in enumerate(points[:K])]
        heapq.heapify(q)
        
        n = len(points)
        for i in range(K, n):
            x, y = points[i]
            dist = -x ** 2 - y ** 2
            heapq.heappushpop(q, (dist, i))
        
        ans = [points[identity] for (_, identity) in q]
        return ans

