class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = s.split()
        res = []
        for i in range(len(st) - 1, -1, -1):
            res.append(st[i])
            if i != 0:
                res.append(" ")

        return "".join(res)
