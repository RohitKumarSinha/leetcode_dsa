class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        # Stores the count of numbers that
        # are needed to be removed
        count = 0
    
        # Store the index of the element
        # that needs to be removed
        index = -1
    
        # Traverse the range [1, N - 1]
        for i in range(1, n):
    
            # If arr[i-1] is greater than
            # or equal to arr[i]
            if (nums[i - 1] >= nums[i]):
                # Increment the count by 1
                count += 1
    
                # Update index
                index = i
    
        # If count is greater than one
        if (count > 1):
            return False
    
        # If no element is removed
        if (count == 0):
            return True
    
        # If only the last or the
        # first element is removed
        if (index == n - 1 or index == 1):
            return True
    
        # If a[index] is removed
        if (nums[index - 1] < nums[index + 1]):
            return True
    
        # If a[index - 1] is removed
        if (nums[index - 2] < nums[index]):
            return True
    
        return False
        