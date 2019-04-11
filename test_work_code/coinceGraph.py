import os 
import sys 
import glob

#from path_config import *

import numpy as np
import matplotlib.pyplot as plt

_ = "/storage/9C33-6BBD/"
DATA_DIR = _ + "0.work/PulseViewer/pulsarsData/"
PATTERN_DIR = _ + "git_projects/pattern_profiles/"
PACK_DIR = _ + "git_projects/PRAO_module/"
ALL_DATA = None


sys.path.append(PACK_DIR)

from PRAO import *

file_list = sorted(glob.glob(DATA_DIR + '*'))

res_list = []
for file in file_list:
    header, main_profile, data_pulses, back = read_profiles(file)

    pattern = np.loadtxt(
                PATTERN_DIR
                + os.sep
                + header['name']
                + '_'
                + header['tay']
                + '.csv',  skiprows=4)
        
    l_frame, r_frame = edgesOprofile(main_profile, pattern)

    sum_res = 0
    for pat, prof in zip(pattern, main_profile[l_frame:r_frame]/max(main_profile)):
        sum_res += abs(pat - prof)
    res_list.append(sum_res)
print(res_list)
#plt.close()
#plt.plot(main_profile)
#plt.axvline(l_frame)
#plt.axvline(r_frame)
#plt.show()