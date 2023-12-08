def solulu(matrix):

    rows, cols = len(matrix), len(matrix[0])

    topRow, bottomRow, leftCol, rightCol = 0, rows - 1, 0, cols -1
    
    res = []

    while topRow <= bottomRow and leftCol <= rightCol:

        for i in range(leftCol,rightCol+1):
            res.append(matrix[topRow][i])
        
        topRow += 1

        for i in range(topRow,bottomRow+1):
            res.append(matrix[i][rightCol])

        rightCol -= 1

        if topRow <= bottomRow:
            for i in range(rightCol,leftCol - 1, -1):
                res.append(matrix[bottomRow][i])

            bottomRow -= 1

        if leftCol <= rightCol:
            print(leftCol,rightCol,bottomRow, topRow)
            for i in range(bottomRow,topRow - 1, -1):
                res.append(matrix[i][leftCol])

            leftCol += 1

    return res

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(solulu(matrix))

            