

int minPartitions(char * n){
    int m = 0;
    while(*n) {
        //#printf("%d ", n - '0');
        if ((*n - '0') > m) m = (*n - '0');
        n++;
    }
    return m;

}