class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if not nums or not nums[0]:
            return []

        # Initialize the set with elements from the first array
        common_elements = set(nums[0])

        # Iterate through the remaining arrays and update the set of common elements
        for arr in nums[1:]:
            common_elements.intersection_update(arr)

        # Return the sorted list of common elements
        return sorted(list(common_elements))

        