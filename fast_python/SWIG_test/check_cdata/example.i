%module example
%include "carrays.i"
%include "cdata.i"

%{
#include "example.h"
%}

%array_class(int, intArray);

%include "example.h"
