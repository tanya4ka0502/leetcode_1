class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        numbers = set(nums)
        result = []
        for n in range(1, len(nums) + 1):
            if n not in numbers:
                result.append(n)
        return result
    