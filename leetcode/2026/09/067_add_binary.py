# Add Binary
# Difficulty: Easy
# https://leetcode.com/problems/add-binary/

# Simulating binary addition by iterating from right to left, managing a carry bit, and building the result string.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result_digits = []
        carry = 0
        
        ptr_a = len(a) - 1
        ptr_b = len(b) - 1
        
        while ptr_a >= 0 or ptr_b >= 0 or carry:
            current_sum = carry
            
            if ptr_a >= 0:
                current_sum += int(a[ptr_a])
                ptr_a -= 1
            
            if ptr_b >= 0:
                current_sum += int(b[ptr_b])
                ptr_b -= 1
            
            result_digits.append(str(current_sum % 2))
            carry = current_sum // 2
            
        return "".join(result_digits[::-1])