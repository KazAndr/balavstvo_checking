%module example
%include "carrays.i"

%{
#include "example.h"
%}

%array_class(int, intArray);
%array_class(double, doubleArray)

%include "example.h"
