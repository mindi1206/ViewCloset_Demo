import pandas as pd 

attr_cloth_Data = pd.read_csv('./list_attr_cloth_new.csv',header=None)
cloth_dataset = attr_cloth_Data.values

ac_x = cloth_dataset[:,0]
ac_y = cloth_dataset[:,1]

att_total = []
for i, d in enumerate(ac_y):
    if d==1:
        att_total.append(ac_x[i])
    elif d==2:
        att_total.append(ac_x[i])

print(len(att_total))
    
