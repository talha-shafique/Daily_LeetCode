class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        if len(s)!=len(goal):
            return False
        for i in range(len(s)):
            s=s[1:]+s[0]
            if s==goal:
                return True
        return False
        
      
      
      
    
    #   The solution below is done by array-method thus less efficient.
      
        # s=list(s)
        # goal=list(goal)
        # for i in range(len(s)):
        #     s.append(s[0])
        #     s.pop(0)
        #     print(s)
        #     if s==goal:
        #         return True
        #     else:
        #         continue
        # return False

        
        