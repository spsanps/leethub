

int lengthOfLongestSubstring(char * s){
    int eng_map[128] = { [0 ... 127] = -1 };
    int l = 0;
    int max = 0;
    int i = 0;
    int j;
    char c = s[0];
    int ltemp;
    while (c) {
        //printf("%c %d\n", c, eng_map[c]);
        if (eng_map[c] != -1) {
            ltemp = eng_map[c] + 1;
            for(j = l; j < ltemp; j++) {
                eng_map[s[j]] = -1;
            }
            l = ltemp;
        }
        eng_map[c] = i;
        //printf("%d \n", l);
        if ( i - l + 1 > max) max =  i - l + 1;
        c = s[++i];    
    }
    return max;
}