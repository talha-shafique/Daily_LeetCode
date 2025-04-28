class Solution:
    def reverseVowels(self, s: str) -> str:
        stack=[]
        ans=''
        for i in s:
            if i in 'AEIOUaeiou':
                stack.append(i)
        for i in s:
            if i in 'AEIOUaeiou':
                ans=ans+stack.pop()
            else:
                ans=ans+i
        return ans

        
        