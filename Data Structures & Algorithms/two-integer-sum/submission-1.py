class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_dict={}
        for i in range(len(nums)):
            idx_dict[nums[i]]=i
        
        for i in range(len(nums)):
            if target-nums[i] in idx_dict and i!=idx_dict[target-nums[i]]:
                return [i,idx_dict[target-nums[i]]]
        return []