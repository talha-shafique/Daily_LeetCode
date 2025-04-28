class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        k=[x for x in range(1,len(matrix)+1)]
        temp=[]
        #checking rows
        for i in matrix:
            if sorted(i)!=k:
                return False
        print('Rows are good!')
        #checking columns
        r=0
        for c in range(len(matrix)):
            while r<len(matrix):
                temp.append(matrix[r][c])
                r=r+1
            print(temp)
            if sorted(temp)!=k:
                print('column disfunction: ')
                return False
            else:
                r=0
                temp.clear()

        return True

        
        