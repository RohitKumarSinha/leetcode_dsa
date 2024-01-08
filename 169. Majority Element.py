class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        
        # Verify the candidate
        count = nums.count(candidate)
        
        # Check if the candidate is the majority element
        if count > len(nums) // 2:
            return candidate
        else:
            return -1  # Indicating no majority element

