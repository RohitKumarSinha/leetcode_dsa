class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if (len(arr) < 3):
            return False

        i = 0
        for i in range(1, len(arr)):
            if (arr[i] <= arr[i - 1]):
                break
    
        if (i == len(arr) or i == 1):
            return False
    
        while i < len(arr):
            if (arr[i] >= arr[i - 1]):
                break
            i += 1
        return i == len(arr)
            