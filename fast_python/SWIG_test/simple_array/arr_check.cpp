// Example program
#include <iostream>
#include <string>
#include "arr_check.h"
 
int* Func(int *Array)
{
    for(int i = 0; i < 3; i++) {
       Array[i]++;
    }
    return Array;
}
 
int* Func_2(int* Array, int size)
{
    int *new_array = new int[size];
    for(int i = 0; i < size; i++) {
       new_array[i] = Array[i] + 1;
    }
    return new_array;
}
 
 
int check_arr()
{
  int a[4] = { 5, 12, 13, 9};
  //Func(a);
  int*  ar = Func_2(a, 4);
  std::cout << a[1] << std::endl;
  std::cout << ar[1] << std::endl;
}
