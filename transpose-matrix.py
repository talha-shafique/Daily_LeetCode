class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows=len(matrix)
        columns=len(matrix[0])

        res=[]
        zeros=[0]*rows
        for i in range(columns):
            res.append(zeros.copy())
        print(res)

        for i in range(rows):
            for j in range(columns):
                res[j][i]=matrix[i][j]
        return res

        