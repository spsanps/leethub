

int maxScore(int* cP, int cPS, int k){
    
    
  
    int c;
    
    int* l_csum = (int*)malloc(sizeof(int)*(k+1));
    
    l_csum[0] = 0;
    
    for(c = 0; c < k; c++) l_csum[c + 1] = cP[c] + l_csum[c];
    
    int r_csum = 0;
    int sum = l_csum[k];
    int asum;
    
    for(c = 0; c < k; c++) {
        r_csum += cP[cPS - c - 1];
        asum = l_csum[k - c - 1] + r_csum;
        if (asum > sum) sum = asum;        
    }

    return sum;
    

}