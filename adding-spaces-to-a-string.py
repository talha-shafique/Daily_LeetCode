class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # s=[x for x in s]
        res=''
        c=0
        if spaces and spaces[0]!=0:
            res=res+s[0:spaces[0]]+" "
        if spaces[0]==0:
            res=res+ ' '

        while c<len(spaces)-1:
            res=res + s[spaces[c]:spaces[c+1]]+ ' '
            c=c+1
        res=res+s[spaces[-1]:]
        return res

            
            
        
        