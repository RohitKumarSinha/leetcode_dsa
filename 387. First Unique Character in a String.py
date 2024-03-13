class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_count = Counter(s)

        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index 

        return -1