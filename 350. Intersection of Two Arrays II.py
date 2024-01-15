class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for num1 in nums1:
            for num2 in nums2:
                if (num1 == num2):
                    nums2.remove(num2)
                    result.append(num1)
                    break

        return result