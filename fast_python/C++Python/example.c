#include <iostream>
#include <cmath>

using namespace std;

void echo(void) {
    cout << "Hello World" << endl;
}

int million()
{
int i;
for (i=0; i<=1000000; i++)
{
    if (i==1000000)
    {
        cout << "Nice!" << endl;
    }
    else
    {
        continue;
    }
}
return 0;
}

double f(double x)
{
    return pow(x, 2)-x;
}

double integrate_f(double a, double b, int N)
{
    int i;
    double s, dx;
    s = 0;
    dx = (b - a)/N;
    for (i=0; i<=N; i++)
    {
        s+=f(a + i*dx);
    }
    return s*dx;
}

int main()
{
    cout << "Это работает!" << endl;

    cout << integrate_f(0, 10, 1000000) << endl;
    return 0;
}
