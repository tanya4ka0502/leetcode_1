class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        d = {}
        for num in nums1:
            d[num] = d.get(num, 0) + 1
        result = []
        for num in nums2:
            if num in d:
                result.append(num)
                del d[num]
        return result
