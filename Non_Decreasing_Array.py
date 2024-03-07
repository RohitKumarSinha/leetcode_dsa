def checkPossibility(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        changed = False 

        for i in range(0, len(nums)):
                if (nums[i] <= nums[i+1]):
                        continue
                if changed:
                        return False
                
                if i == 0 or nums[i + 1] >= nums[i - 1]:
                        nums[i] = nums[i + 1]

                else:
                        nums[i + 1] = nums[i]

ans = checkPossibility([2, 3, 2, 1, 6])
print(ans)