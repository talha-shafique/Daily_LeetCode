class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Using Hash Map
        # freq={}
        # l=0
        # max_len=0
        # for r in range(len(s)):
        #     if s[r] in freq:
        #         freq[s[r]]+=1
        #     else:
        #         freq[s[r]]=1
        #     while freq[s[r]]>1:
        #         freq[s[l]]-=1
        #         l=l+1
        #     max_len=max(max_len,r-l+1)
        # return max_len

        #Using Set
        count=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in count:
                count.remove(s[l])
                l=l+1
            else:
                count.add(s[r])
                res=max(res,r-l+1)
        return res
            
                




        




        