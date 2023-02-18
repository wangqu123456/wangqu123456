class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        mark = formatMark(m, n)
        res = False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    # mark = formatMark(m, n)
                    pointer = 0
                    res = judgeWord(board, mark, word, i, j, pointer)
                if res:
                    return True
        return res

def formatMark(m, n ):
    mark = []
    for i in range(m):
        tmp = []
        for j in range(n):
            tmp.append(0)
        mark.append(tmp)
    return mark

def judgeWord(board, mark, word, i, j, pointer):
    if i >= len(board) or i < 0:
        return False
    if j >= len(board[0]) or j < 0:
        return False
    if pointer >= len(word):
        return False
    if mark[i][j] != 0:
        return False

    if board[i][j] == word[pointer]:
        print(i, j, pointer)
        mark[i][j] = 1
        if pointer == len(word) - 1:
            return True
        res = judgeWord(board, mark, word, i, j-1, pointer + 1) \
               or judgeWord(board, mark, word, i, j + 1, pointer + 1) \
               or judgeWord(board, mark, word, i - 1, j, pointer + 1) \
               or judgeWord(board, mark, word, i+1, j, pointer + 1)
        if not res:
            mark[i][j] = 0
        return res

    else:
        return False


sol = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"
# word = "ABCESEEEFS"
word = "SEE"

print(sol.exist(board, word))
