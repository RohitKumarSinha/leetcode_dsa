class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)

        result = list(set_nums1.intersection(set_nums2))

        return result

        