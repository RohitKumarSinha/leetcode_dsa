def isMatrixSymmetric(matrix):
    # Write your code here. 
    row = len(matrix) 
    col = len(matrix[0])
    transpose = [[0 for x in range(row)] for y in range(col)] 
    for i in range(row):
        for j in range(col):
            transpose[i][j] = matrix[j][i]

    print(transpose)
    for i in range(0, row):
        for j in range(0, col):
            if (matrix[i][j] != transpose[i][j]):
                print("NO")
                return

        
    print("Yes")

ans = [[1, 2, 3], [2, 4, 5], [3, 5, 8]]
isMatrixSymmetric(ans)