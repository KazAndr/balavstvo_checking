#include <iostream>
#include <string>
#include <vector>
#include "example.h"


void printFunction(std::vector<std::string> strs) {
	unsigned int i;
	for (i = 0; i < strs.size(); i++) {
	std::cout << strs[i] << std::endl;
	};

};
