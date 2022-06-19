

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize){
    *returnSize = numsSize;
    int* ret = (int*)malloc(sizeof(int)*numsSize);
    
    int i, mult;
    
    mult = 1;
    for(i = 0; i < numsSize; i++) {
        ret[i] = mult;
        mult *= nums[i];
    }
    
    mult  = 1;
    for(i = numsSize - 1; i >= 0; i--) {
        ret[i] = ret[i]*mult;
        mult *= nums[i];
    }
    return ret;
    
    

}