%module example

%{
extern void echo(void);
extern int million();
extern double f(double x);
extern double integrate_f(double a, double b, int N);
extern int main();
%}

extern void echo(void);
extern int million();
extern double f(double x);
extern double integrate_f(double a, double b, int N);
extern int main();
