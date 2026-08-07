class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxs = [[False] * 9 for _ in range(9)]

        for rind in range(9):
            for cind in range(9):
                cellval = board[rind][cind]

                if cellval == ".":
                    continue
                
                digitind = int(cellval) - 1

                bind = (rind // 3) * 3 + (cind // 3)

                if rows[rind][digitind] or cols[cind][digitind] or boxs[bind][digitind]:
                    return False

                rows[rind][digitind] = True
                cols[cind][digitind] = True
                boxs[bind][digitind] = True
        return True
