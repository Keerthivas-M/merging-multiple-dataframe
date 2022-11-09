import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
load = input("Enter the normal load")
temp = input("Enter the temperature")
lf1 = pd.read_csv('p0d_'+load+'nN_'+temp+'K_sliding1.profile', sep = ' ',skiprows=2, names=['TimeStep' ,'v_disx' ,'v_disy' ,'v_disz' ,'v_virtualdispx' ,'v_virtualdispy' ,'v_virtualdispz', 'v_pullvirtualx' ,'v_pullvirtualy', 'v_pullvirtualz' ,'c_contactforce[1]' ,'c_contactforce[2]' ,'c_contactforce[3]' ,'c_grforce[1]' ,'c_grforce[2]' ,'c_grforce[3]' ,'c_adhesion' ,'c_potential','c_intertemp)'])
# lf1 = lf1.iloc[1:,:]
# lf1.drop(index=lf1.index[0], axis=0, inplace=True)
# print(lf1[:5])
lf2 = pd.read_csv('p0d_'+load+'nN_'+temp+'K_sliding2.profile', sep = ' ',skiprows=2, names=['TimeStep' ,'v_disx' ,'v_disy' ,'v_disz' ,'v_virtualdispx' ,'v_virtualdispy' ,'v_virtualdispz', 'v_pullvirtualx' ,'v_pullvirtualy', 'v_pullvirtualz' ,'c_contactforce[1]' ,'c_contactforce[2]' ,'c_contactforce[3]' ,'c_grforce[1]' ,'c_grforce[2]' ,'c_grforce[3]' ,'c_adhesion' ,'c_potential','c_intertemp)'])
lf3 = pd.read_csv('p0d_'+load+'nN_'+temp+'K_sliding3.profile', sep = ' ',skiprows=2, names=['TimeStep' ,'v_disx' ,'v_disy' ,'v_disz' ,'v_virtualdispx' ,'v_virtualdispy' ,'v_virtualdispz', 'v_pullvirtualx' ,'v_pullvirtualy', 'v_pullvirtualz' ,'c_contactforce[1]' ,'c_contactforce[2]' ,'c_contactforce[3]' ,'c_grforce[1]' ,'c_grforce[2]' ,'c_grforce[3]' ,'c_adhesion' ,'c_potential','c_intertemp)'])
lf4 = pd.read_csv('p0d_'+load+'nN_'+temp+'K_sliding4.profile', sep = ' ',skiprows=2, names=['TimeStep' ,'v_disx' ,'v_disy' ,'v_disz' ,'v_virtualdispx' ,'v_virtualdispy' ,'v_virtualdispz', 'v_pullvirtualx' ,'v_pullvirtualy', 'v_pullvirtualz' ,'c_contactforce[1]' ,'c_contactforce[2]' ,'c_contactforce[3]' ,'c_grforce[1]' ,'c_grforce[2]' ,'c_grforce[3]' ,'c_adhesion' ,'c_potential','c_intertemp)'])
lateral = [lf1, lf2, lf3, lf4]
nan_value=0
merged = pd.concat(lateral, join='outer', ignore_index=True).fillna(nan_value)
merged.to_csv('merged_lf.csv')
merged['sliding_dist'] = (merged['TimeStep'] - 100500) * 0.000004
print(merged.head())
stdev_x = np.std(merged.v_pullvirtualx[25:])
avg_x = np.mean(merged.v_pullvirtualx[25:])
stdev_z = np.std(merged.v_pullvirtualz[25:])
avg_z = np.mean(merged.v_pullvirtualz[25:])
#stderror.x = stdev_x/ sqrt()
print(stdev_x, stdev_z, avg_x, avg_z)
plt.plot(merged.sliding_dist[25:], merged.v_pullvirtualx[25:])
plt.show()
