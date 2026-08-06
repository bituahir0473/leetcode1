class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == ".":
                    continue

                row = (num, "row", i)
                col = (num, "col", j)
                box = (num, "box", i // 3, j // 3)

                if row in seen or col in seen or box in seen:
                    return False

                seen.add(row)
                seen.add(col)
                seen.add(box)

        return True