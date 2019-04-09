/* File: example.i */
%module example

%{
    #include "struct_h.h"
%}
%include "struct_h.h"

FILE *fopen(const char *filename, const char *mode);
int fputs(const char *, FILE *);
int fclose(FILE *);

int fact(int n);

%inline %{
extern int My_variable;
extern double density;
%}


