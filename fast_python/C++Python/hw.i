%module hw
%{
#include "hw.h"
%}

%include "typemaps.i"

%apply double *OUTPUT {double* s}
%apply double *OUTPUT {double& s}

void hw1(double r1, double r2, double *s);
void hw2(double r1, double r2);
