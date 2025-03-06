class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for i in strs:
            l = "".join(sorted(i))
            dic.setdefault(l,[]).append(i)
        return dic.values()
