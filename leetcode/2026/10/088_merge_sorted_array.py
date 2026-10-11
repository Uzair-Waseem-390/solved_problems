# Merge Sorted Array
# Difficulty: Easy
# https://leetcode.com/problems/merge-sorted-array/

# Merge from the end using three pointers to avoid overwriting elements in nums1.
# Compare largest elements and place them at the end of nums1.
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        pointer1 = m - 1
        pointer2 = n - 1
        write_pointer = m + n - 1

        while pointer1 >= 0 and pointer2 >= 0:
            if nums1[pointer1] > nums2[pointer2]:
                nums1[write_pointer] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[write_pointer] = nums2[pointer2]
                pointer2 -= 1
            write_pointer -= 1

        while pointer2 >= 0:
            nums1[write_pointer] = nums2[pointer2]
            pointer2 -= 1
            write_pointer -= 1