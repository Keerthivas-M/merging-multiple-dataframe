#import pandas and numpy packages
import pandas as pd
import numpy as np
#enter input values to id filename
load = input("Enter the normal load")
temp = input("Enter the temperature")
#read multiple csv files space seperated and skip firstrow 
lf1 = pd.read_csv('p0d_'+load+'nN_'+temp+'K_sliding1.profile', sep = ' ',skiprows=1)
lf2 = pd.read_csv('p0d_'+load+'nN_'+temp+'K_sliding2.profile', sep = ' ',skiprows=1)
lf2 = lf2.iloc[1:,:]
lf3 = pd.read_csv('p0d_'+load+'nN_'+temp+'K_sliding3.profile', sep = ' ',skiprows=1)
lf3 = lf3.iloc[1:,:]
lf4 = pd.read_csv('p0d_'+load+'nN_'+temp+'K_sliding4.profile', sep = ' ',skiprows=1)
lf4 = lf4.iloc[1:,:]
lateral = [lf1, lf2, lf3, lf4]
nan_value=0
merged = pd.concat(lateral, join='outer', ignore_index=True).fillna(nan_value)
merged.to_csv('merged_lf.csv')
stdev_x = np.std(merged.v_virtualdispz[25:])
avg_x = np.mean(merged.v_virtualdispz[25:])
stdev_z = np.std(merged.v_pullvirtualy[25:])
avg_z = np.mean(merged.v_pullvirtualy[25:])
print(stdev_x, stdev_z, avg_x, avg_z)
