class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        if not nums:
            return 0
        
        temp_sum = 0
        sum_list = [0]
        for num in nums:
            temp_sum += num
            sum_list.append(temp_sum)
        
        def merge_sort(left, right):
            if left == right:
                return 0

            mid = (left + right) // 2
            n1 = merge_sort(left, mid)
            n2 = merge_sort(mid + 1, right)
            cnt = n1 + n2
            
            i, l, r = left, mid + 1, mid + 1
            while i <= mid:
                while l <= right and sum_list[l] - sum_list[i] < lower:
                    l += 1
                while r <= right and sum_list[r] - sum_list[i] <= upper:
                    r += 1
                cnt += (r - l)
                i += 1
            
            sorted_list = [None] * (right - left + 1)
            p1, p2 = left, mid + 1
            p = 0
            while p1 <= mid or p2 <= right:
                if p1 > mid:
                    sorted_list[p] = sum_list[p2]
                    p2 += 1
                elif p2 > right:
                    sorted_list[p] = sum_list[p1]
                    p1 += 1
                else:
                    if sum_list[p1] <= sum_list[p2]:
                        sorted_list[p] = sum_list[p1]
                        p1 += 1
                    else:
                        sorted_list[p] = sum_list[p2]
                        p2 += 1
                p += 1
            
            for i in range(len(sorted_list)):
                sum_list[left + i] = sorted_list[i]
            
            return cnt
        
        return merge_sort(0, len(sum_list) - 1)

