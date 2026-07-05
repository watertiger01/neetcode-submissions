class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        m=len(nums)
        w_i=0
        for i in range(m):
            if nums[i]!=val:
                nums[w_i]=nums[i]
                w_i+=1
            # print(nums, " ", i, " ", w_i)
        
        return w_i
        