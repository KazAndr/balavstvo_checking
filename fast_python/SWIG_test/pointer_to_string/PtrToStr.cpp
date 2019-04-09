#include "PtrToStr.h"


std::string LDPToStr(long double * one)
{
    std::stringstream ss;
    ss<<one;
    return ss.str();
}

std::string LDToStr(long double one)
{
    std::stringstream ss;
    ss<<one;
    return ss.str();
}

char LDPToChar(long double * one)
{
    char str[1024];
    std::stringstream ss;
    ss<<one;
    ss>>str;
 
    return str;
}
