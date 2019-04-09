%module example
%include "carrays.i"

%{
#include "example.h"
%}

%array_functions(double, doubleArray);


%include "example.h"
