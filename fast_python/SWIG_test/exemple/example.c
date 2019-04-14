/* File: example.c */

#include "example.h"

void range(int *rangevec, int n)
{
    int i;

    for (i=0; i< n; i++)
        rangevec[i] = i;
}
