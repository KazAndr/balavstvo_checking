#include <stdio.h>
#include <cmath>

#include "hw.h"

void hw1(double r1, double r2, double *s)
{
    *s = cos(r1 + r2);
}

void hw2(double r1, double r2)
{
    double s;
    s = cos(r1 + r2);
    printf("cos(%f+%f)=%f\n", r1, r2, s);
}
