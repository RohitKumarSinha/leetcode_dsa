class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if (len(nums) == 0):
            return nums

        slow = 0

        for fast in range(len(nums)):
            if (nums[fast] != val):
                nums[slow] = nums[fast]
                slow += 1

        return slow