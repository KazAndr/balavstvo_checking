/* File: example.i */
%module example

%{
    #define SWIG_FILE_WITH_INIT
    #include "example.h"
%}

%include "numpy.i"

%init %{
    import_array();
%}

%apply (int* ARGOUT_ARRAY1, int DIM1){(int* rangevec, int n)}

%include "example.h"
