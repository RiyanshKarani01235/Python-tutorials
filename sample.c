#include <math.h>

int divide(int a,int b,int *remainder) {
    int quot = a/b;
    *remainder = a%b;
    return quot;
}

double avg(double *a,int n) {
    int i;
    double total = 0.0;
    for(i=0;i<n;i++) {
        total += a[i];
    }
    return total/n;
}