

int maxScore(int* cP, int cPS, int k){
    
    
  
    int i;
    int lsum = 0;
    for (i = 0; i < k; i++) {
        lsum += cP[i];
    }
    int max = lsum;
    for (i = 0; i < k; i++) {
        lsum += cP[cPS - i - 1] - cP[k - i - 1];
        if (lsum > max) max = lsum;
    }
    
    return max;
    

}