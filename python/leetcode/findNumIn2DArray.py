class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        mark = []
        for i in range(m):
            tmp_list = []
            for j in range(n):
                tmp_list.append(0)
            mark.append(tmp_list)
        print mark
        # return
        i = 0
        j = 0
        res = False
        res = huisu(matrix, i, j, target, mark)
        print res
        return res


def huisu(matrix, i, j, target, mark):
    if i < 0 or i >= len(matrix):
        return False
    if j < 0 or j >= len(matrix[0]):
        return False
    print("i: {0}, j:{1}".format(i, j))
    if mark[i][j] != 0:
        return False
    mark[i][j] = 1
    if matrix[i][j] == target:
        return True
    elif matrix[i][j] < target:
        return huisu(matrix, i + 1, j, target, mark) or huisu(matrix, i, j + 1, target, mark)
    elif matrix[i][j] > target:
        return huisu(matrix, i - 1, j, target, mark) or huisu(matrix, i, j - 1, target, mark)


if __name__ == "__main__":
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    sol = Solution()
    sol.findNumberIn2DArray(matrix, target)
