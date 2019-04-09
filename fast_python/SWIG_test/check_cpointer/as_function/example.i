%module example
%include "cpointer.i"

%{
#include "example.h"
%}

%pointer_functions(int, intPoint);

%include "example.h"
