def Rotate_Array(nums, k):
    n = len(nums)

    rot_nums = [None] * n 

    for i in range(0, n):
        rot_nums[(i + k) % n] = nums[i]

    for j in range(0, n):
        nums[j] = rot_nums[j]

    return nums


nums = [1,2,3,4,5,6,7]
Rotate_Array(nums, 3)
print(nums)