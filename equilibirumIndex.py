def EquibiliriumIndex(nums, n):

    summ = 0
    summ_array = [None] * n
    for i in range(0, n):
        summ += nums[i]
        summ_array[i] = summ

    for i in range(1, n-1):
        lsum = summ_array[i] - nums[i]
        rsum = summ - summ_array[i]

        if (lsum == rsum):
            return i


ans = EquibiliriumIndex([1,2, 3 , 3, 4, 3, -1], 7)
print(ans)