class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        in_stack = {}
        c_counter = collections.Counter(s)
        
        for c in s:
            if not in_stack.get(c, False):
                while stack and c_counter[stack[-1]] > 0 and stack[-1] > c:         
                    temp = stack.pop()
                    in_stack[temp] = False
                stack.append(c)
                in_stack[c] = True
            c_counter[c] -= 1

        return ''.join(stack)

