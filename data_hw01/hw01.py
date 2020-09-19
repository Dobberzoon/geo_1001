#Homework 1

#Author: Daniel Dobson
#Student number: 5152739
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Dataframes of all variables from 'HEAT - A_final.xls' - 'HEAT - E_final.xls'
dfA = pd.read_excel('HEAT - A_final.xls', skiprows=[0,1,2,4])
dfB = pd.read_excel('HEAT - B_final.xls', skiprows=[0,1,2,4])
dfC = pd.read_excel('HEAT - C_final.xls', skiprows=[0,1,2,4])
dfD = pd.read_excel('HEAT - D_final.xls', skiprows=[0,1,2,4])
dfE = pd.read_excel('HEAT - E_final.xls', skiprows=[0,1,2,4])
dfs = pd.concat([dfA, dfB, dfC, dfD, dfE])


#Histogram of temperatures for sensors A -E, bin=5
dfs.hist(column='Temperature', bins=5)
plt.title('Temperatures of sensors')
plt.xlabel('Temp in C')
plt.ylabel('Frequency')
plt.savefig('Temps_bin5.png')
plt.show()

#Histogram of temperatures for sensors A -E, bin=5
dfs.hist(column='Temperature', bins=50)
plt.title('Temperatures of sensors')
plt.xlabel('Temp in C')
plt.ylabel('Frequency')
plt.savefig('Temps_bin50.png')
plt.show()

#Frequency Polygon of Temperature of sensors A -E
y,edges_A,_=plt.hist(dfA['Temperature'], bins=50, histtype= 'step', edgecolor='w')
y,edges_B,_=plt.hist(dfB['Temperature'], bins=50, histtype= 'step', edgecolor='w')
y,edges_C,_=plt.hist(dfC['Temperature'], bins=50, histtype= 'step', edgecolor='w')
y,edges_D,_=plt.hist(dfD['Temperature'], bins=50, histtype= 'step', edgecolor='w')
y,edges_E,_=plt.hist(dfE['Temperature'], bins=50, histtype= 'step', edgecolor='w')
midpoints_A=0.5*(edges_A[1:]+edges_A[:-1])
midpoints_B=0.5*(edges_B[1:]+edges_B[:-1])
midpoints_C=0.5*(edges_C[1:]+edges_C[:-1])
midpoints_D=0.5*(edges_D[1:]+edges_D[:-1])
midpoints_E=0.5*(edges_E[1:]+edges_E[:-1])
plt.plot(midpoints_A, y, 'r-*', label='A')
plt.plot(midpoints_B, y, 'b-*', label='B')
plt.plot(midpoints_C, y, 'g-*', label='C')
plt.plot(midpoints_D, y, 'c-*', label='D')
plt.plot(midpoints_E, y, 'm-*', label='E')
plt.title('Temperatures of sensors A - E')
plt.xlabel('Temp in C')
plt.ylabel('Frequency')
plt.legend()
plt.savefig('Frequency_Polygon_Temperatures_A-E.png')
plt.show()

#print(dfs.describe())

#concat_dfs('Temperature')
#print(dfA.head)
#print(dfs.head)
#print(dfs.colums)

#print(dfs['Temperature'].head)




#dfA_Temp = dfA[['Temperature']]
#plt.show()

#print(dfA_Temp.head)
#print(dfA_Temp.columns)

'''
#Means, of each variable in 'HEAT - A_final.xls' - 'HEAT - E_final.xls'
df_mean_concat = pd.concat([dfA.apply(np.mean), dfB.apply(np.mean), dfC.apply(np.mean), dfD.apply(np.mean), dfE.apply(np.mean)], axis=1, ignore_index=True)
df_mean_concat.to_csv('Means_ALL2.csv')
df_mean_concat.to_excel('Means_excel.xlsx')
print(df_mean_concat)

#Mean for all variables in 'HEAT - A_final.xls' - 'HEAT - E_final.xls'
dfA_mean = dfA.mean()
dfB_mean = dfB.mean()
dfC_mean = dfC.mean()
dfD_mean = dfD.mean()
dfE_mean = dfE.mean()
df_mean_concat = pd.concat(
    [dfA_mean, dfB_mean, dfC_mean, dfD_mean, dfE_mean], 
    axis=1, ignore_index=True)
print(df_mean_concat)

#Std.dev for all variables in 'HEAT - A_final.xls' - 'HEAT - E_final.xls'
dfA_std = dfA.std()
dfB_std = dfB.std()
dfC_std = dfC.std()
dfD_std = dfD.std()
dfE_std = dfE.std()
df_std_concat = pd.concat(
    [dfA_std, dfB_std, dfC_std, dfD_std, dfE_std], 
    axis=1, ignore_index=True)
df_std_concat.columns = ['Std.dev']
print(df_std_concat)

#Variance for all variables in 'HEAT - A_final.xls' - 'HEAT - E_final.xls'
dfA.drop('FORMATTED DATE-TIME', inplace=True, axis=1) #Did not need this in the end
dfA_var = dfA.var()
dfB_var = dfB.var()
dfC_var = dfC.var()
dfD_var = dfD.var()
dfE_var = dfE.var()
df_var_concat = pd.concat(
    [dfA_var, dfB_var, dfC_var, dfD_var, dfE_var], 
    axis=1, ignore_index=True)

#Means, std.dev and variance of all sensors joined in one dataframe
df_mean_std_var = pd.concat([df_mean_concat, df_std_concat, df_var_concat],ignore_index=True)      #Redundant
df_mean_std_var_2 = pd.concat([df_mean_concat, df_std_concat, df_var_concat],axis=1, ignore_index=True)
header = pd.MultiIndex.from_product([['Mean','Std.dev.','Variance'], ['A','B','C','D','E']], names=['stat','sensor'])
df_mean_std_var_2.columns = header

#Histogram of temperatures for sensors A -E, bin=5
dfs.hist(column='Temperature', bins=5)
plt.title('Temperatures of sensors')
plt.xlabel('Temp in C')
plt.ylabel('Frequency')
plt.savefig('Temps_bin5.png')
plt.show()

#Histogram of temperatures for sensors A -E, bin=5
dfs.hist(column='Temperature', bins=50)
plt.title('Temperatures of sensors')
plt.xlabel('Temp in C')
plt.ylabel('Frequency')
plt.savefig('Temps_bin50.png')
plt.show()

#Print concat dfs of all basic stats
#print(df_mean_std_var)     #Redundant
#print(df_mean_std_var_2)

#Export basic stats to excel
#df_mean_std_var.to_excel('Basic_stats_excel_V1.xlsx')
#df_mean_std_var_2.to_excel('Basic_stats_excel_V2.xlsx')
'''

#Prints for initial look into data
#print(df.head)
#print(df.columns)
#print(df.mean)

#Get quick initial idea of basic stats
#dfA.describe()

'''
def Pmf(pmf, **options):
    """Plots a Pmf or Hist as a line.

    Args:
      pmf: Hist or Pmf object
      options: keyword args passed to plt.plot
    """
    xs, ys = pmf.Render()
    low, high = min(xs), max(xs)

    width = options.pop('width', None)
    if width is None:
        try:
            width = np.diff(xs).min()
        except TypeError:
            warnings.warn("Pmf: Can't compute bar width automatically."
                          "Check for non-numeric types in Pmf."
                          "Or try providing width option.")
    points = []

    lastx = np.nan
    lasty = 0
    for x, y in zip(xs, ys):
        if (x - lastx) > 1e-5:
            points.append((lastx, 0))
            points.append((x, 0))

        points.append((x, lasty))
        points.append((x, y))
        points.append((x+width, y))

        lastx = x + width
        lasty = y
    points.append((lastx, 0))
    pxs, pys = zip(*points)

    align = options.pop('align', 'center')
    if align == 'center':
        pxs = np.array(pxs) - width/2.0
    if align == 'right':
        pxs = np.array(pxs) - width

    options = _Underride(options, label=pmf.label)
    Plot(pxs, pys, **options)

dfA_hist = dfA.hist(column='Temperature', histtype= 'step',  bins=50)

Pmf(dfA_hist)
plt.show()
''' 
# %%
