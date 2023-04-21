class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
 
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            # Memoization, tracking answers to subproblems.
            triangle = [[0]] * numRows
            triangle[0] = [1]
            triangle[1] = [1, 1]

        for i in range(2, numRows):
            row = [1] * (i + 1)
            x = 1
            while x < len(row) - 1:
                row[x] = triangle[i - 1][x] + triangle[i - 1][x - 1]
                x += 1
            triangle[i] = row
            
        return triangle
