%module readRAW_py

%{
#include <iostream>
#include <fstream>
#include <stdint.h>
#include <cmath>
#include <bitset>
#include "TH1F.h"
#include "TFile.h"
#include "TH2F.h"
#include "TTree.h"
#include "TRandom.h"
#include "TProfile.h"
#include "TProfile2D.h"


extern int chToNum(char ch);
extern double readNumber(char* buffer, int iStart, int N0, int N1);
extern float pulseToFloat(unsigned int pulse, float tau);
extern int readRAW(std::string runID, std::string rawdata_dir, std::string output_dir);
extern int main(int argc, char *argv[]);
%}
#include <iostream>
#include <fstream>
#include <stdint.h>
#include <cmath>
#include <bitset>
#include "TH1F.h"
#include "TFile.h"
#include "TH2F.h"
#include "TTree.h"
#include "TRandom.h"
#include "TProfile.h"
#include "TProfile2D.h"

extern int chToNum(char ch);
extern double readNumber(char* buffer, int iStart, int N0, int N1);
extern float pulseToFloat(unsigned int pulse, float tau);
extern int readRAW(std::string runID, std::string rawdata_dir, std::string output_dir);
extern int main(int argc, char *argv[]);
