def firstUniqChar(s):
        """
        :type s: str
        :rtype: int
        """

        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    return i

        return -1

ans = firstUniqChar(s = "leetcode")
print(ans)