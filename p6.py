# N皇后问题
# 有一个N*N的矩阵方格和N个棋子，现在需要将N个棋子按要求放置到矩阵方格中。要求如下:
# 1.任意两个棋子不能在同一行
# 2.任意两个棋子不能在同一列
# 3.任意两个棋子不能在同一对角线上(下图红色线段都为对角线)

def solve_n_queens(n):
    solutions = []
    board = [-1] * N

    def is_safe(row,col):
        for prev_row in range(row):
           prev_col = board[prev_row]

           if prev_col == col:
               return False
           if abs(prev_row - row) == abs(prev_col - col):
               #如果 |x1 - x2| == |y1 - y2|，那么这两个点在同一对角线上
               return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(board.copy())
            return
        for col in range(n):
            if is_safe(row,col):
                board[row] = col
                backtrack(row+1)
    backtrack(0)
    return solutions
    


# 示例使用
if __name__ == "__main__":
    N = int(input())
    solutions = solve_n_queens(N)
    print(f"共有 {len(solutions)} 种解法：\n")

