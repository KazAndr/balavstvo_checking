
double dot(int n, double *a, int m, double *b) {
    double sum = 0.0;
    int i;
    for (i = 0; i < n; i++){
        sum += a[i]*b[i];
    }
    return sum;
}

void arange(int size, double *arr){
    int i;
    for (i = 0; i < size; i++)
        arr[i]=i;
}
