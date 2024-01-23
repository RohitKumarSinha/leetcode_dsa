def findErrorNums(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = [0] * len(nums)

        for i in nums:
            count[i - 1] += 1
        
        return [count.index(2) + 1, count.index(0) + 1]

ans = findErrorNums(nums = [1,2,2,4])
print(ans)
