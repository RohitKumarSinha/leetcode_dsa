def secondLargest(nums, n):
    largest = nums[0]
    secondLargest = -99999

    for i in range(1, n):
        if nums[i] > largest:
            secondLargest = largest
            largest = nums[i]

        elif (nums[i] > secondLargest and nums[i] != largest):
            secondLargest = nums[i]

        if secondLargest == -9999:
            return -1

    return secondLargest


    


ans = secondLargest([1,3, 5, 6, 2,8, 8], 7)
print(ans)