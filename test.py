from collections import deque
from math import ceil
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        squares = []

        for i in range(n-1,-1,-1):
            left_right = (n-i)%2
            col_order = range(n) if left_right else range(n-1,-1,-1)
            for j in col_order:
                squares.append(board[i][j])

        destinations = deque([(1,0)])
        seen = {1}

        while destinations:
            curr, steps = destinations.popleft()
            if curr == n*n:
                return steps
            for next_num in range(curr+1, min(curr+6, n**2) + 1):
                next_steps = steps + 1
                next_square = squares[next_num-1]
                if next_square != -1:
                    next_num = next_square
                if next_num in seen:
                    continue
                seen.add(next_num)
                destinations.append((next_num, next_steps))
        return -1


        



