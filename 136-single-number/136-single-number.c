

int singleNumber(int* nums, int numsSize){
    int i;
    int solution = 0;
    for(i = 0; i  < numsSize; i++) {
        solution = solution ^ nums[i];
    }
    
    return solution;

}