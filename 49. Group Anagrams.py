def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = []
        keyToAnagrams = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            keyToAnagrams[key].append(s)

        for anagrams in keyToAnagrams.values():
            ans.append(anagrams)

        return ans

