class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*5
        dp[0] = 0
        dp[1] = 0
        dp[2] = 1
        dp[3] = 2
        dp[4] = 4
        if n > 4:
            t1, t2 = divmod(n, 3)
            tmp_res = multiply(3, t1-1)
            if t2 == 0:
                res = tmp_res*3
            elif t2 == 1:
                res = tmp_res*4
            elif t2 == 2:
                res = 2*3*tmp_res

            return divmod(res, 1000000007)[-1]
        else:
            return dp[n]


def multiply(m, n):
    if n <= 0:
        return 1
    return m*multiply(m, n-1)

sol = Solution()
print(sol.cuttingRope(10))
print(sol.cuttingRope(180))
print(sol.cuttingRope(5))