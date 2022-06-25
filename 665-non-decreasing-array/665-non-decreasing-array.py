class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        aChange = False
        for i in range(1, len(nums)):
            #print(aChange, nums, nums[i])
            if nums[i] < nums[i - 1]:

                if aChange:
                    return False
                else:
                    aChange = True
                    if i - 2 >=0:
                        if nums[i] >= nums[i - 2]:
                            nums[i - 1] = nums[i]
                        else:
                            nums[i] = nums[i - 1]
                    else:
                        nums[i - 1] = nums[i]
                    
            #print(aChange, nums)
                    
            if i - 2 >= 0:
                if nums[i] < nums[i - 2]: return False
        return True
        