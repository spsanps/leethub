

int maxScore(int* cP, int cPS, int k){
    
    

    int lsum, rsum;
    lsum = 0; rsum = 0;
    
    
    int c = 0;
    
    int* l_csum = (int*)malloc(sizeof(int)*(k+1));
    int* r_csum = (int*)malloc(sizeof(int)*(k+1));
    
    l_csum[0] = 0;
    r_csum[0] = 0;
    
    while (c < k) {
        lsum += cP[c];
        rsum += cP[cPS - 1 - c];
        l_csum[c + 1] = lsum;
        r_csum[c + 1] = rsum;
        c++;
    }
    
    int sum = 0;
    int asum;
    c = 0;
    while (c <= k) {
        asum = l_csum[c] + r_csum[k - c];
        sum = asum > sum ? asum : sum;
        c++;
    }


    return sum;
    

}