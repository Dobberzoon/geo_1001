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

#dfA.describe()

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
df_mean_concat = pd.concat([dfA_mean, dfB_mean, dfC_mean, dfD_mean, dfE_mean], axis=1, ignore_index=True)
#df_mean_concat.columns = ['Mean']
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
print(df_std_concat)

#Variance for all variables in 'HEAT - A_final.xls' - 'HEAT - E_final.xls'
#dfA.drop('FORMATTED DATE-TIME', inplace=True, axis=1) #Did not need this in the end
dfA_var = dfA.var()
dfB_var = dfB.var()
dfC_var = dfC.var()
dfD_var = dfD.var()
dfE_var = dfE.var()
df_var_concat = pd.concat([dfA_var, dfB_var, dfC_var, dfD_var, dfE_var], axis=1, ignore_index=True)
#df_var_concat.columns = ['Variance']

#print(df_var_concat)

#Means, std.dev and variance of all sensors joined
df_mean_std_var = pd.concat([df_mean_concat, df_std_concat, df_var_concat],ignore_index=True)
df_mean_std_var_2 = pd.concat([df_mean_concat, df_std_concat, df_var_concat],axis=1, ignore_index=True)
header = pd.MultiIndex.from_product([['Mean','Std.dev.','Variance'], ['A','B','C','D','E']], names=['stat','sensor'])
#df_mean_std_var_2 = pd.DataFrame(df_mean_std_var_2, columns=header)
df_mean_std_var_2.columns = header
#header = ['Mean', 'Mean', 'Mean', 'Mean', 'Mean', 'Std.dev', 'Std.dev', 'Std.dev', 'Std.dev', 'Std.dev', 'Variance', 'Variance', 'Variance', 'Variance', 'Variance']
#df_mean_std_var_2.columns = pd.MultiIndex.from_tuples(list(zip(header, ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E'])))

#df_mean_std_var_2.columns = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E']
print(df_mean_std_var)
print(df_mean_std_var_2)
df_mean_std_var.to_excel('Basic_stats_excel_V1.xlsx')
df_mean_std_var_2.to_excel('Basic_stats_excel_V2.xlsx')



#print(dfA.head())
#dfA_types = dfA.dtypes
#print('Data type of each column of Dataframe :')

#Data types are uniform across sources
#print(dfA.dtypes)
#print(dfB.dtypes)
#print(dfC.dtypes)
#print(dfD.dtypes)
#print(dfE.dtypes)

#No duplicates or null values
#dfA.drop_duplicates(inplace=True)
#print(dfA.shape)
#print(dfA.isnull().sum())

#dfA.drop('FORMATTED DATE-TIME', inplace=True, axis=1)
#df_mean_ALL = pd.merge((df_A.apply(np.mean), df_B.apply(np.mean), df_C.apply(np.mean), df_D.apply(np.mean), df_E.apply(np.mean)))
#df_mean_ALL.to_csv('Means_ALL2.csv')
#df_A.apply(np.mean).to_csv('Means_A_.csv')

'''
print('Means of each variable in "HEAT - A_final.xls"')
print('Direction, True: ', + df['Direction ‚ True'].mean())
print('Windspeed: ', + df['Wind Speed'].mean())
print('Crosswind Speed: ', + df['Crosswind Speed'].mean())
print('Headwind Speed: ', + df['Headwind Speed'].mean())
print('Temperature: ', + df['Temperature'].mean())
print('Globe Temperature: ', + df['Globe Temperature'].mean())
print('Wind Chill: ', + df['Wind Chill'].mean())
print('Relative Humidity: ', + df['Relative Humidity'].mean())
print('Heat Stress Index: ', + df['Heat Stress Index'].mean())
print('Dew Point: ', + df['Dew Point'].mean())
print('Psychro Wet Bulb Temperature: ', + df['Psychro Wet Bulb Temperature'].mean())
print('Station Pressure: ', + df['Station Pressure'].mean())
print('Barometric Pressure: ', + df['Barometric Pressure'].mean())
print('Altitude: ', + df['Altitude'].mean())
print('Density Altitude: ', + df['Density Altitude'].mean())
print('NA Wet Bulb Temperature: ', + df['NA Wet Bulb Temperature'].mean())
print('WBGT: ', + df['WBGT'].mean())
print('TWL: ', + df['TWL'].mean())
print('Direction ‚ Mag: ', + df['Direction ‚ Mag'].mean(), '\n')

print('Direction, True: ', + df['Direction ‚ True'].var())

df.describe().to_csv("describe_A.csv")


#Means of each variable in 'HEAT - B_final.xls'
df = pd.read_excel('HEAT - B_final.xls', skiprows=[0,1,2,4])

print('Means of each variable in "HEAT - B_final.xls"')
print('Direction, True: ', + df['Direction ‚ True'].mean())
print('Windspeed: ', + df['Wind Speed'].mean())
print('Crosswind Speed: ', + df['Crosswind Speed'].mean())
print('Headwind Speed: ', + df['Headwind Speed'].mean())
print('Temperature: ', + df['Temperature'].mean())
print('Globe Temperature: ', + df['Globe Temperature'].mean())
print('Wind Chill: ', + df['Wind Chill'].mean())
print('Relative Humidity: ', + df['Relative Humidity'].mean())
print('Heat Stress Index: ', + df['Heat Stress Index'].mean())
print('Dew Point: ', + df['Dew Point'].mean())
print('Psychro Wet Bulb Temperature: ', + df['Psychro Wet Bulb Temperature'].mean())
print('Station Pressure: ', + df['Station Pressure'].mean())
print('Barometric Pressure: ', + df['Barometric Pressure'].mean())
print('Altitude: ', + df['Altitude'].mean())
print('Density Altitude: ', + df['Density Altitude'].mean())
print('NA Wet Bulb Temperature: ', + df['NA Wet Bulb Temperature'].mean())
print('WBGT: ', + df['WBGT'].mean())
print('TWL: ', + df['TWL'].mean())
print('Direction ‚ Mag: ', + df['Direction ‚ Mag'].mean(), '\n')

#Means of each variable in 'HEAT - C_final.xls'
df = pd.read_excel('HEAT - C_final.xls', skiprows=[0,1,2,4])

print('Means of each variable in "HEAT - C_final.xls"')
print('Direction, True: ', + df['Direction ‚ True'].mean())
print('Windspeed: ', + df['Wind Speed'].mean())
print('Crosswind Speed: ', + df['Crosswind Speed'].mean())
print('Headwind Speed: ', + df['Headwind Speed'].mean())
print('Temperature: ', + df['Temperature'].mean())
print('Globe Temperature: ', + df['Globe Temperature'].mean())
print('Wind Chill: ', + df['Wind Chill'].mean())
print('Relative Humidity: ', + df['Relative Humidity'].mean())
print('Heat Stress Index: ', + df['Heat Stress Index'].mean())
print('Dew Point: ', + df['Dew Point'].mean())
print('Psychro Wet Bulb Temperature: ', + df['Psychro Wet Bulb Temperature'].mean())
print('Station Pressure: ', + df['Station Pressure'].mean())
print('Barometric Pressure: ', + df['Barometric Pressure'].mean())
print('Altitude: ', + df['Altitude'].mean())
print('Density Altitude: ', + df['Density Altitude'].mean())
print('NA Wet Bulb Temperature: ', + df['NA Wet Bulb Temperature'].mean())
print('WBGT: ', + df['WBGT'].mean())
print('TWL: ', + df['TWL'].mean())
print('Direction ‚ Mag: ', + df['Direction ‚ Mag'].mean(), '\n')

#Means of each variable in 'HEAT - D_final.xls'
df = pd.read_excel('HEAT - D_final.xls', skiprows=[0,1,2,4])

print('Means of each variable in "HEAT - D_final.xls"')
print('Direction, True: ', + df['Direction ‚ True'].mean())
print('Windspeed: ', + df['Wind Speed'].mean())
print('Crosswind Speed: ', + df['Crosswind Speed'].mean())
print('Headwind Speed: ', + df['Headwind Speed'].mean())
print('Temperature: ', + df['Temperature'].mean())
print('Globe Temperature: ', + df['Globe Temperature'].mean())
print('Wind Chill: ', + df['Wind Chill'].mean())
print('Relative Humidity: ', + df['Relative Humidity'].mean())
print('Heat Stress Index: ', + df['Heat Stress Index'].mean())
print('Dew Point: ', + df['Dew Point'].mean())
print('Psychro Wet Bulb Temperature: ', + df['Psychro Wet Bulb Temperature'].mean())
print('Station Pressure: ', + df['Station Pressure'].mean())
print('Barometric Pressure: ', + df['Barometric Pressure'].mean())
print('Altitude: ', + df['Altitude'].mean())
print('Density Altitude: ', + df['Density Altitude'].mean())
print('NA Wet Bulb Temperature: ', + df['NA Wet Bulb Temperature'].mean())
print('WBGT: ', + df['WBGT'].mean())
print('TWL: ', + df['TWL'].mean())
print('Direction ‚ Mag: ', + df['Direction ‚ Mag'].mean(), '\n')

#Means of each variable in 'HEAT - E_final.xls'
df = pd.read_excel('HEAT - E_final.xls', skiprows=[0,1,2,4])

print('Means of each variable in "HEAT - E_final.xls"')
print('Direction, True: ', + df['Direction ‚ True'].mean())
print('Windspeed: ', + df['Wind Speed'].mean())
print('Crosswind Speed: ', + df['Crosswind Speed'].mean())
print('Headwind Speed: ', + df['Headwind Speed'].mean())
print('Temperature: ', + df['Temperature'].mean())
print('Globe Temperature: ', + df['Globe Temperature'].mean())
print('Wind Chill: ', + df['Wind Chill'].mean())
print('Relative Humidity: ', + df['Relative Humidity'].mean())
print('Heat Stress Index: ', + df['Heat Stress Index'].mean())
print('Dew Point: ', + df['Dew Point'].mean())
print('Psychro Wet Bulb Temperature: ', + df['Psychro Wet Bulb Temperature'].mean())
print('Station Pressure: ', + df['Station Pressure'].mean())
print('Barometric Pressure: ', + df['Barometric Pressure'].mean())
print('Altitude: ', + df['Altitude'].mean())
print('Density Altitude: ', + df['Density Altitude'].mean())
print('NA Wet Bulb Temperature: ', + df['NA Wet Bulb Temperature'].mean())
print('WBGT: ', + df['WBGT'].mean())
print('TWL: ', + df['TWL'].mean())
print('Direction ‚ Mag: ', + df['Direction ‚ Mag'].mean(), '\n')


# Prints for initial look into data
#print(df.head)
#print(df.columns)
#print(df.mean)
''' 