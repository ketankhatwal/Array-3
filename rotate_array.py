# Time Complexity: O(n)
# Space Complexity: O(1)
# Ran on Leetcode: Yes

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        if not k:
            return
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
        
    def reverse(self, nums, l, r):
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    
        
            
        