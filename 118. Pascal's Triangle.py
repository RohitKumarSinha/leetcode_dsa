class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        pascal_triangle = [[1]] #Initialize with the first row 
        for i in range(1, numRows):
            prev_row = pascal_triangle[-1] # get the previous row 
            new_row = [1] #each row starts with 1
            # Calculate the values based on the row above 
            for j in range(1, i):
                new_row.append(prev_row[j - 1] + prev_row[j])
                
            new_row.append(1)  # Each row ends with 1
            pascal_triangle.append(new_row)  # Add the newly calculated row
        
        return pascal_triangle
    
