class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        f0 = 1
        f1 = 1
        i = 2
        while i <= n:
            t = f0
            f0 = f1
            f1 = f0 + t
            i = i +1
        return f1


sol = Solution()
print(sol.numWays(0))
print(sol.numWays(1))
print(sol.numWays(2))
print(sol.numWays(3))
print(sol.numWays(37))
