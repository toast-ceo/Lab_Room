import os
import shutil

s = 'C:/Users/issac/Desktop/crosswalk/'
P = 'learning_datasets_outside_predict'
PM = 'learning_datasets_outside_predict_mask'
PMD_file_name = 'C:/Users/issac/Desktop/crosswalk/0'

P_file_names = os.listdir(s+P)

PM_file_names = os.listdir(s+PM)

# print(P_file_names)
# print(PM_file_names)


for i in range(len(PM_file_names)):

    temp = PM_file_names[i].replace("PM","P")
    if P_file_names.__contains__(temp):
        shutil.copyfile(s+PM+'/' + PM_file_names[i], PMD_file_name+'/' + PM_file_names[i] )
