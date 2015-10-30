#include <math.h>
#include "Python/Python.h"

int divide(int a,int b,int *remainder) {
    int quot = a/b;
    *remainder = a%b;
    return quot;
}

void avg(double *a,int n) {
    int i;
    double total = 0.0;
    for(i=0;i<n;i++) {
        //total += *(a+i);
        *(a+i) += 1;
    }
    //return total/n;
}