from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # Helper function to count how many elements are <= mid
        def countElements(mid):
            j = len(matrix[0]) - 1  # Start from the last column
            count = 0  # Count of elements <= mid
            
            # Traverse each row
            for i in range(len(matrix)):
                while j >= 0 and matrix[i][j] > mid:  # Move left if the element is greater than mid
                    j -= 1
                count += (j + 1)  # Number of elements <= mid in this row
            return count  # Return total count of elements <= mid

        # Initialize the binary search range
        left, right = matrix[0][0], matrix[-1][-1]  # The smallest and largest values in the matrix
         
        # Binary search on the value range
        while left < right:
            mid = left + (right - left) // 2  # Find the middle value
            
            if countElements(mid) < k:
                # If there are fewer than k elements <= mid, move search to the right half
                left = mid + 1
            else:
                # Otherwise, move search to the left half (including mid)
                right = mid
        
        # When left == right, we've found the kth smallest element
        return left  
