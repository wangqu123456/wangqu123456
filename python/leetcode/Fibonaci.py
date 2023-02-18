class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        former = 0
        latter = 1
        i = 2
        while i <= n:
            t = former
            former = latter
            latter = former + t
            i = i + 1

        return divmod(latter, 1000000007)[-1]

sol = Solution()
print(sol.fib(3))