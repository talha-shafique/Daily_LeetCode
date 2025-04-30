class Solution:
    def checkRecord(self, s: str) -> bool:
        temp='LLL'
        if temp in s or s.count('A')>=2:
            return False
        return True


        