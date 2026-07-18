class Solution:
    def solveSudoku(self, board):
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        box=[set() for _ in range(9)]
        emp=[]

        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    emp.append((i,j))
                else:
                    x=board[i][j]
                    rows[i].add(x)
                    cols[j].add(x)
                    box[(i//3)*3+j//3].add(x)

        def dfs(k):
            if k==len(emp):
                return True
            i,j=emp[k]
            b=(i//3)*3+j//3
            for x in "123456789":
                if x not in rows[i] and x not in cols[j] and x not in box[b]:
                    board[i][j]=x
                    rows[i].add(x)
                    cols[j].add(x)
                    box[b].add(x)

                    if dfs(k+1):
                        return True

                    board[i][j]="."
                    rows[i].remove(x)
                    cols[j].remove(x)
                    box[b].remove(x)
            return False

        dfs(0)