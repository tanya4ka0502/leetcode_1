class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = dict()
        for i in range(len(nums)):
            a = target - nums[i]
            if a in num_dict:
                return [num_dict[a], i]
            num_dict[nums[i]] = i
        return []
