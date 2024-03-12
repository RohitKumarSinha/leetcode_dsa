def minIncrementForUnique(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        total_operations = 0

        for i in  range(1, len(nums)):
            if (nums[i] <= nums[i - 1]):
                increment = nums[i - 1] - nums[i] + 1
                nums[i] += increment
                total_operations += increment

        return total_operations

ans = minIncrementForUnique(nums = [1,2,2])
print(ans)