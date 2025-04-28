class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        #Primary Diagonal
        row=0
        column=0
        summ=0
        while row<len(mat) and column <len(mat[0]):
            print(mat[row][column])
            summ=summ+mat[row][column]
            row=row+1
            column=column+1
        print(summ)
        print('----------')

        #Secondary Diagonal
        row=0
        column=len(mat[0])-1
        while row<len(mat) and column>=0:
            print(mat[row][column])
            summ=summ+mat[row][column]
            row=row+1
            column=column-1
        print(summ)

        #Removing the repeating  element if Matrix rows are odd
        if len(mat)%2!=0:
            row=len(mat)//2
            column=len(mat)//2
            summ=summ-mat[row][column]
        return summ
        

        