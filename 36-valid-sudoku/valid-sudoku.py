class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            rows=[set()for i in range(9)]
            cols=[set()for j in range(9)]
            boxes=[set()for k in  range(9)] 
            for r in range(9):
                for c in range(9):
                    num=board[r][c]
                    if num==".":
                        continue
                    if num in rows[r]:
                        return False
                    rows[r].add(num)
                    if num in cols[c]:
                        return False
                    cols[c].add(num)
                    box=(r//3)*3+(c//3)
                    if num in boxes[box]:
                        return False
                    boxes[box].add(num)
            return True