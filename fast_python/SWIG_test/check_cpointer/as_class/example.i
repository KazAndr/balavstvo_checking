%module example
%include "cpointer.i"

%{
#include "example.h"
%}

%pointer_class(int, intPoint);

%include "example.h"
