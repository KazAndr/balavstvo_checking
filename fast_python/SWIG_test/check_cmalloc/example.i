%module example
%include "cmalloc.i"

%malloc(int);
%free(int);

%malloc(int *, intp);
%free(int *, intp);

%allocators(double);

%{
#include "example.h"
%}

%include "example.h"
