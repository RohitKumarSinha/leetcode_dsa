def setZeroes(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_col_zero = False 

        #check for zeros and mark the corresponding rows and columns 
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True 

            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        #Set Zeros based on the marks 
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0 

        #Handle the first row 
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0

        #Handle the first column 
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

        return matrix

ans = setZeroes(matrix = [[1,1,1],[1,0,1],[1,1,1]])
print(ans)