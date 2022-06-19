

int maxSubArray(int* nums, int numsSize){
    int i, l, r, s, maxs;
    l = 0, r = 0;
    s = 0;
    maxs = nums[0];
    for(i = 0; i < numsSize; i++) {
        s += nums[i];
        if (s > maxs) maxs = s;
        if(s < 0) {        
            s = 0;
        }
    }
    return maxs;
   

}