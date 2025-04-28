class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occur={}
        res=[]
        for i in range(len(s)):
            occur[s[i]]=i
        i=0
        while i <len(s):
            j=i
            t=occur[s[i]]
            while j<t:
                t=max(t,occur[s[j]])
                j=j+1
            res.append(j-i+1)
            i=j+1
        return res
        