class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, lNum in enumerate(nums):
            for j, rNum in enumerate(nums[i+1:]):
                if (lNum+rNum == target):
                    return (i, j+i+1)