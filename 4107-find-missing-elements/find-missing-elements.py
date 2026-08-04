class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        missing = []
        for i in range(len(nums) - 1):
            for x in range(nums[i] + 1, nums[i + 1]):
                missing.append(x)
        return missing