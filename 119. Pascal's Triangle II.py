class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1] * (rowIndex + 1)  # Initialize the row with 1s
        
        for i in range(1, rowIndex + 1):
            # Update the row values based on the binomial coefficient formula
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]
        
        return row