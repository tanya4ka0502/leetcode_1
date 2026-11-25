class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        prev_rows = self.generate(numRows - 1)
        new_row = [1] * numRows
        for i in range(1, numRows - 1):
            new_row[i] = prev_rows[-1][i - 1] + prev_rows[-1][i]
        prev_rows.append(new_row)
        return prev_rows
