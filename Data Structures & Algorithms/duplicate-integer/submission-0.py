class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        lastNum = None
        for num in nums:
            if num == lastNum:
                return True
            lastNum = num
        return False
