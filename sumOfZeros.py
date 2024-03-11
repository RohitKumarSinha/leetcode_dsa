def coverageOfMatrix(mat):
    # Write your code here.
    rows = len(mat)
    cols = len(mat[0])

    count = 0

    for i in range(0,rows):
        for j in range(0,cols):
            if (i - 1 >= 0 and mat[i - 1][j] == 1):
                count += 1

            if (j + 1 < cols and mat[i][j + 1] == 1):
                count += 1 

            if (i + 1 < rows and mat[i + 1][j] == 1):
                count += 1

            if (j - 1 >= 0 and mat[i][j - 1] == 1):
                count += 1

    return count

mat = [[1,0], [0, 1]]

ans = coverageOfMatrix(mat)
print(ans)

        
