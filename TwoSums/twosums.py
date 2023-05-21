class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = [-1, -1]
        temp = [0] * len(nums)
        for i in range(len(nums)):
            temp[i] = target - nums[i]
        for i in range(len(nums)):
            if temp[i] in nums and nums.index(temp[i]) != i:
                result = [i, nums.index(temp[i])]
                break
        return result


solv = Solution()
nums_list = [3, 3]
target = 6
print(solv.twoSum(nums_list, target))
