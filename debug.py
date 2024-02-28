def rotate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        temp = [None] * len(nums)

        for i in range(0,len(nums)):
            temp[(i + k) % len(nums)] = nums[i]

        nums = temp.copy

        
nums = [1,2,3,4,5,6,7]
rotate(nums, 3)
print(nums)
