

int comp(const void* a , const void* b) {
    return *((int*)a) - *((int*)b);
}

int minMoves2(int* n, int S){
    
    if (S == 1) return 0; 
    
    qsort(n, S, sizeof(int), comp);
    int i;
    /*for(i = 0; i < S; i++) {
        printf("%d ", n[i]);
    }
    printf("\n");*/
    
    int mid = n[S/2];
    int min = 0;
    for(i = 0; i < S/2; i++) {
        min += mid - n[i];
    }
    for(i = S/2 + 1; i < S; i++) {
        min += n[i] - mid;
    }
    //min -= mid*(S - S/2 -1);
    
    return min;
        
}