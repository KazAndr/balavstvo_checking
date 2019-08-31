%module range_ez

%{
    #define SWIG_FILE_WITH_INIT
    #include "range_ez.h"
%}

%include "numpy.i"

%init %{
    import_array();
%}

%apply (int* ARGOUT_ARRAY1, int DIM1) {(int* rangevec, int n)}

%include "range_ez.h"
