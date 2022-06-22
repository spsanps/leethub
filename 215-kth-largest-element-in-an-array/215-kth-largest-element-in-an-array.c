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


int findKthLargest(int* n, int nS, int k){
    
        int i;
    int *ls = (int *)malloc(sizeof(int)*k);
    for(i = 0; i < k; i++) {
        ls[i] = INT_MIN;
    }
    

    for (i = 0; i < nS; i++) {
        if (n[i] > ls[0]) {
            ls[0] = n[i];
            heapify(ls, k, 0);
        }
    }
    
    return ls[0];
    
}