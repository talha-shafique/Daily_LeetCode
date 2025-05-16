class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ss=int(''.join(str(x) for x in digits))
        ss=ss+1
        ss=[int(digit) for digit in str(ss)]
        return ss