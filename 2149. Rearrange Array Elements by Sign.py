def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        ans = size * [None]
        posIndex = 0 
        negIndex = 1

        for i in range(size):
            if(nums[i] < 0):
                ans[negIndex] = nums[i]
                negIndex += 2
            else:
                ans[posIndex] = nums[i]
                posIndex += 2
            
        return ans