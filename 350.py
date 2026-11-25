class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        d = {}
        for num in nums1:
            d[num] = d.get(num, 0) + 1
        result = []
        for num in nums2:
            if d.get(num, 0) > 0:
                result.append(num)
                d[num] -= 1
        return result
    