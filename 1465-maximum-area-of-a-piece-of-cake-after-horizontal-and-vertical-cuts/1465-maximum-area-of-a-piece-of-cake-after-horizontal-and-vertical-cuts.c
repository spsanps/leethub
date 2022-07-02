int mulMod(int a, int b, int m) {
    int res = 0;
    a %= m;
    b %= m;
    while (b > 0) {
        if (b%2 == 1) res = (res + a)%m;
        a = (a*2)%m;
        b = b/2;
    }
    return res;
}


int comp(const void* a, const void* b) {
    return *((int*)a) - *((int*)b);
}


int maxArea(int h, int w, int* hC, int hCS, int* vC, int vCS){
    
    qsort(hC, hCS, sizeof(int), comp);
    qsort(vC, vCS, sizeof(int), comp);
    
    int maxV = w - vC[vCS - 1];
    int maxH = h - hC[hCS - 1];
    
    if (hC[0] > maxH) maxH = hC[0];
    if (vC[0] > maxV) maxV = vC[0];
    
    int i;
    for(i = 1; i < hCS; i++) {
        if (hC[i] - hC[i - 1] > maxH) maxH = hC[i] - hC[i - 1];
    }
    
    for(i = 1; i < vCS; i++) {
        if (vC[i] - vC[i - 1] > maxV) maxV = vC[i] - vC[i - 1];
    }
    
    
    return mulMod(maxH, maxV, 1000000000 + 7);

}