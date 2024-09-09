# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        def get_values_from_linked_list(head):
            values = []
            while head:
                values.append(head.val)
                head = head.next
            return values

        def fill_spiral(matrix, values):
            m, n = len(matrix), len(matrix[0])
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
            direction_index = 0
            row, col = 0, 0
            for value in values:
                matrix[row][col] = value
                next_row, next_col = row + directions[direction_index][0], col + directions[direction_index][1]
                if (0 <= next_row < m and 0 <= next_col < n and matrix[next_row][next_col] == -1):
                    row, col = next_row, next_col
                else:
                    direction_index = (direction_index + 1) % 4
                    row += directions[direction_index][0]
                    col += directions[direction_index][1]

        matrix = [[-1] * n for _ in range(m)]
        values = get_values_from_linked_list(head)
        fill_spiral(matrix, values)
        return matrix