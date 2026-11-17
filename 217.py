class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in nums:
            if nums.count(i) == 2:
                return True
        return False
