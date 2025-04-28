class Solution:
    def makeFancyString(self, s: str) -> str:
        stack=["",""]
        for i in range(len(s)):
            if stack and s[i]==stack[-1] and s[i]==stack[-2]:
                continue
            else:
                stack.append(s[i])
        res=''.join(stack[2:])
        return res
        