#Homework 1

#Author: Daniel Dobson
#Student number: 5152739

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Dataframes of all variables from 'HEAT - A_final.xls' - 'HEAT - E_final.xls'
dfA = pd.read_excel('HEAT - A_final.xls', skiprows=[0,1,2,4])
dfB = pd.read_excel('HEAT - B_final.xls', skiprows=[0,1,2,4])
dfC = pd.read_excel('HEAT - C_final.xls', skiprows=[0,1,2,4])
dfD = pd.read_excel('HEAT - D_final.xls', skiprows=[0,1,2,4])
dfE = pd.read_excel('HEAT - E_final.xls', skiprows=[0,1,2,4])

#Means, of each variable in 'HEAT - A_final.xls' - 'HEAT - E_final.xls'
#df_mean_concat = pd.concat([dfA.apply(np.mean), dfB.apply(np.mean), dfC.apply(np.mean), dfD.apply(np.mean), dfE.apply(np.mean)], axis=1, ignore_index=True)
#df_mean_concat.to_csv('Means_ALL2.csv')
#df_mean_concat.to_excel('Means_excel.xlsx')
#print(df_mean_concat)

#Mean for all variables in 'HEAT - A_final.xls' - 'HEAT - E_final.xls'
dfA_mean = dfA.mean()
dfB_mean = dfB.mean()
dfC_mean = dfC.mean()
dfD_mean = dfD.mean()
dfE_mean = dfE.mean()
df_mean_concat = pd.concat(
    [dfA_mean, dfB_mean, dfC_mean, dfD_mean, dfE_mean], 
    axis=1, ignore_index=True)
#print(df_mean_concat)

#Std.dev for all variables in 'HEAT - A_final.xls' - 'HEAT - E_final.xls'
dfA_std = dfA.std()
dfB_std = dfB.std()
dfC_std = dfC.std()
dfD_std = dfD.std()
dfE_std = dfE.std()
df_std_concat = pd.concat(
    [dfA_std, dfB_std, dfC_std, dfD_std, dfE_std], 
    axis=1, ignore_index=True)
#df_std_concat.columns = ['Std.dev']
#print(df_std_concat)

#Variance for all variables in 'HEAT - A_final.xls' - 'HEAT - E_final.xls'
#dfA.drop('FORMATTED DATE-TIME', inplace=True, axis=1) #Did not need this in the end
dfA_var = dfA.var()
dfB_var = dfB.var()
dfC_var = dfC.var()
dfD_var = dfD.var()
dfE_var = dfE.var()
df_var_concat = pd.concat(
    [dfA_var, dfB_var, dfC_var, dfD_var, dfE_var], 
    axis=1, ignore_index=True)

#Means, std.dev and variance of all sensors joined in one dataframe
#df_mean_std_var = pd.concat([df_mean_concat, df_std_concat, df_var_concat],ignore_index=True)      #Redundant
df_mean_std_var_2 = pd.concat([df_mean_concat, df_std_concat, df_var_concat],axis=1, ignore_index=True)
header = pd.MultiIndex.from_product([['Mean','Std.dev.','Variance'], ['A','B','C','D','E']], names=['stat','sensor'])
df_mean_std_var_2.columns = header

#Print concat dfs of all basic stats
#print(df_mean_std_var)     #Redundant
print(df_mean_std_var_2)

#Export basic stats to excel
#df_mean_std_var.to_excel('Basic_stats_excel_V1.xlsx')
df_mean_std_var_2.to_excel('Basic_stats_excel_V2.xlsx')


'''
#Prints for initial look into data
#print(df.head)
#print(df.columns)
#print(df.mean)

#Get quick initial idea of basic stats
#dfA.describe()
''' 