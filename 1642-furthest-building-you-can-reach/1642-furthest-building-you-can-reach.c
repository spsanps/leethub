

void swap (int *x, int *y) {
    int temp;
    temp = *y;
    *y = *x;
    *x = temp;
}


int left(int i) {
    return (2*i) + 1;
}

int right(int i) {
    return 2*i + 2;
}

int parent(int i) {
    return (i - 1)/2;
}

void heapify (int* heap, int size, int i) {
    int l = left(i);
    int r = right(i);
    

    if (l < size && heap[l] < heap[i]) {
        if (r < size && heap[r] < heap[l]) {
            swap(heap + r, heap + i);
            heapify(heap, size, r);
        } else if (l < size) {
            swap(heap + l, heap + i);
            heapify(heap, size, l);
        }
    } else {
        if (r < size && heap[r] < heap[i]) {
            swap(heap + r, heap + i);
            heapify(heap, size, r);
        }
    }
}

int furthestBuilding(int* hs, int h_len, int b, int l) {
    
    
    int h = 0;
    int i;
    
    int *ls = (int *)malloc(sizeof(int)*(l + 1));
    for(i = 0; i < l; i++) {
        ls[i] = 0;
    }
    ls[i] = INT_MAX;
     
        
    for(i = 0; i < h_len - 1; i++ ) {
        h = hs[i + 1] - hs[i];
        //printf("%d %d %d \n", b, ls[0], h);
        if (h > ls[0]) {
            b -= ls[0];
            ls[0] = h;
            heapify(ls, l, 0);
        } else if (h > 0) {
            b -= h;
        }

        if (b < 0) {
            return i;
        }
        
        
    }
    
    return i;

}