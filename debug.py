def findMaxConsecutiveOnes(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                largest = max(largest, count)
                count = 0

        return largest

ans = findMaxConsecutiveOnes(nums = [1,1,0,1,1,1])
print(ans)
