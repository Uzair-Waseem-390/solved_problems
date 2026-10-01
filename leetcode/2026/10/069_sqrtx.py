# Sqrt(x)
# Difficulty: Easy
# https://leetcode.com/problems/sqrtx/

# Binary search works well here because the square function is monotonic,
# allowing efficient search for the largest integer whose square is less than or equal to x.
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        low = 0
        high = x
        result = 0

        while low <= high:
            mid = low + (high - low) // 2
            
            mid_squared = mid * mid

            if mid_squared == x:
                return mid
            elif mid_squared < x:
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return result