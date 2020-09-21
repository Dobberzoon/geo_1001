#Homework 1

#Author: Daniel Dobson
#Student number: 5152739
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import plotly.express as px
import seaborn as sns
from scipy import stats
from scipy.stats import sem, t, ttest_ind
import numpy as np
import scipy.stats
from scipy import mean


#Function for A4
def confidence_interval_95(data):
    confidence=0.95
    n = len(data)
    m = mean(data)
    std_err = sem(data)
    h = std_err * t.ppf((1 + confidence) / 2, n - 1)
    #print('The 95 % confidence interval is: ')
    return m-h, m+h

#Dataframes of all variables from 'HEAT - A_final.xls' - 'HEAT - E_final.xls'
dfA = pd.read_excel('HEAT - A_final.xls', skiprows=[0,1,2,4])
dfB = pd.read_excel('HEAT - B_final.xls', skiprows=[0,1,2,4])
dfC = pd.read_excel('HEAT - C_final.xls', skiprows=[0,1,2,4])
dfD = pd.read_excel('HEAT - D_final.xls', skiprows=[0,1,2,4])
dfE = pd.read_excel('HEAT - E_final.xls', skiprows=[0,1,2,4])
dfs = pd.concat([dfA, dfB, dfC, dfD, dfE])

#Means, of each variable in 'HEAT - A_final.xls' - 'HEAT - E_final.xls'
df_mean_concat = pd.concat([dfA.apply(np.mean), 
                            dfB.apply(np.mean), 
                            dfC.apply(np.mean), 
                            dfD.apply(np.mean), 
                            dfE.apply(np.mean)], 
                            axis=1, ignore_index=True)
#df_mean_concat.to_excel('Means_excel.xlsx')
#print(df_mean_concat)

#Mean for all variables in 'HEAT - A_final.xls' - 'HEAT - E_final.xls'
dfA_mean = dfA.mean()
dfB_mean = dfB.mean()
dfC_mean = dfC.mean()
dfD_mean = dfD.mean()
dfE_mean = dfE.mean()
df_mean_concat = pd.concat([dfA_mean, dfB_mean, dfC_mean, dfD_mean, dfE_mean], axis=1, ignore_index=True)
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
#print(df_std_concat)

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

df_mean_std_var_2 = pd.concat([df_mean_concat, df_std_concat, df_var_concat],axis=1, ignore_index=True)


#Export basic stats to excel
#header = pd.MultiIndex.from_product([['Mean','Std.dev.','Variance'], ['A','B','C','D','E']], names=['stat','sensor'])
#df_mean_std_var_2.to_excel('Basic_stats_excel_V2.xlsx')

#Histogram of temperatures for sensors A -E, bin=5
dfs.hist(column='Temperature', bins=5)
plt.title('Temperatures of sensors')
plt.xlabel('Temp in C')
plt.ylabel('Frequency')
#plt.savefig('Temps_bin5.png')
plt.show()

#Histogram of temperatures for sensors A -E, bin=50
dfs.hist(column='Temperature', bins=50)
plt.title('Temperatures of sensors')
plt.xlabel('Temp in C')
plt.ylabel('Frequency')
#plt.savefig('Temps_bin50.png')
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
#plt.savefig('Frequency_Polygon_Temperatures_A-E.png')
plt.show()

##Boxplots for Wind Speed sensors A - E  
boxplot_windspeed = [dfA['Wind Speed'], dfB['Wind Speed'], dfC['Wind Speed'], dfD['Wind Speed'], dfE['Wind Speed']]
fig1, ax1 = plt.subplots()
ax1.set_title('Distribution of measured Wind Speed values')
plt.xlabel('Sensor')
plt.ylabel('Windpeed in m/s')
ax1.boxplot(boxplot_windspeed, labels=['A','B','C','D','E'])
#plt.savefig('Boxplot_Windspeed.png')

##Boxplots for Wind Direction, True values sensors A - E
boxplot_direction = [dfA['Direction ‚ True'], dfB['Direction ‚ True'], dfC['Direction ‚ True'], dfD['Direction ‚ True'], dfE['Direction ‚ True']]
fig1, ax1 = plt.subplots()
ax1.set_title('Distribution of measured Direction, True values')
plt.xlabel('Sensor')
plt.ylabel('Direction in degrees')
ax1.boxplot(boxplot_direction, labels=['A','B','C','D','E'])
#plt.savefig('Boxplot_DirectionTrue.png')

##Boxplots for Temperature values sensors A - E
boxplot_temp = [dfA['Temperature'], dfB['Temperature'], dfC['Temperature'], dfD['Temperature'], dfE['Temperature']]
fig1, ax1 = plt.subplots()
ax1.set_title('Distribution of measured Temperature values')
plt.xlabel('Sensor')
plt.ylabel('Temperature in C')
ax1.boxplot(boxplot_temp, labels=['A','B','C','D','E'])
#plt.savefig('Boxplot_Temp.png')

##A2
#Plot PMF Temperatur valuess all sensors
fig1, ax1 = plt.subplots()
ax1.set_title('PMF Temperature values Sensors A - E')
plt.ylabel('Probability')
plt.xlabel('Temp in C')
plt.hist(dfs['Temperature'], bins=50, histtype= 'step', edgecolor='k', density=True)
#plt.savefig('PMF_Temps.png')
plt.show()

#Plot PDF Temperatures all sensors
y,edges_T,_=plt.hist(dfs['Temperature'], bins=50, histtype= 'step', edgecolor='w', density=True)
dfs['Temperature']
midpoints_T=0.5*(edges_T[1:]+edges_T[:-1])
plt.plot(midpoints_T, y, 'b', label='PDF_Temps')
plt.plot()
plt.ylabel('Probability')
plt.xlabel('Temp in C')
plt.title('PDF Temperatures Sensors A - E')
#plt.savefig('PDF_Temperatures_A-E.png')
plt.show()

#CDF Temperature values
plt.hist(dfs['Temperature'], bins=50, histtype= 'step', edgecolor='k', density=True, cumulative=True)
plt.plot()
plt.ylabel('Cumulative Density')
plt.xlabel('Temp in C')
plt.title('CDF Temperatures Sensors A - E')
#plt.savefig('CDF.png')
plt.show()

#PDF and KDE of measured Windspeed values from sensors A - E
y,edges_WSPDF,_=plt.hist(dfs['Wind Speed'], bins=30, histtype= 'step', edgecolor='w', density=True)
midpoints_WSPDF=0.5*(edges_WSPDF[1:]+edges_WSPDF[:-1])
plt.plot(midpoints_WSPDF, y, 'b', label='PDF Wind Speed')
sns.kdeplot(dfs['Wind Speed'], color='#ff7f0e')
plt.ylabel('Probability')
plt.xlabel('Windspeed in m/s')
plt.title('PDF & KDE Wind Speed Sensors A - E')
plt.legend()
#plt.savefig('PDF_KDE_WindSpeed_A-E.png')
plt.show()

##A3
#Correlation matrices Temperature Pearson and Spearman
dfs_Temp = pd.concat([dfA['Temperature'], dfB['Temperature'], dfC['Temperature'], dfD['Temperature'], dfE['Temperature']], axis=1, keys=['A', 'B', 'C', 'D', 'E'])
dfs_Temp_P = dfs_Temp.corr(method='pearson')
#dfs_Temp_P.to_excel('dfs_Temp_P.xlsx')
dfs_Temp_S = dfs_Temp.corr(method='spearman')
#dfs_Temp_S.to_excel('dfs_Temp_S.xlsx')

#Correlation matrices WBGT Pearson and Spearman
dfs_WBGT = pd.concat([dfA['WBGT'], dfB['WBGT'], dfC['WBGT'], dfD['WBGT'], dfE['WBGT']], axis=1, keys=['A', 'B', 'C', 'D', 'E'])
dfs_WBGT_P = dfs_WBGT.corr(method='pearson')
#dfs_WBGT_P.to_excel('dfs_WBGT_P.xlsx')
dfs_WBGT_S = dfs_WBGT.corr(method='spearman')
#dfs_WBGT_S.to_excel('dfs_WBGT_S.xlsx')

#Correlation matrices Crosswind Speed Pearson and Spearmann
dfs_CWS = pd.concat([dfA['Crosswind Speed'], dfB['Crosswind Speed'], dfC['Crosswind Speed'], dfD['Crosswind Speed'], dfE['Crosswind Speed']], axis=1, keys=['A', 'B', 'C', 'D', 'E'])
dfs_CWS_P = dfs_CWS.corr(method='pearson')
#dfs_CWS_P.to_excel('dfs_CWS_P.xlsx')
dfs_CWS_S = dfs_CWS.corr(method='spearman')
#dfs_CWS_S.to_excel('dfs_CWS_S.xlsx')

#Pearson's Coefficient Scatterplot for all three variables: Temperature, WBGT & Crosswind Speed
#Creating pairs AB, BD, AD, AE ,BC , BD, BE, CD, CE, DE
x = dfs_Temp_P.values.tolist()[0][1:]
x.extend(dfs_Temp_P.values.tolist()[1][2:])
x.extend(dfs_Temp_P.values.tolist()[2][3:])
x.extend(dfs_Temp_P.values.tolist()[3][4:])
y = dfs_WBGT_P.values.tolist()[0][1:]
y.extend(dfs_WBGT_P.values.tolist()[1][2:])
y.extend(dfs_WBGT_P.values.tolist()[2][3:])
y.extend(dfs_WBGT_P.values.tolist()[3][4:])
z = dfs_CWS_P.values.tolist()[0][1:]
z.extend(dfs_CWS_P.values.tolist()[1][2:])
z.extend(dfs_CWS_P.values.tolist()[2][3:])
z.extend(dfs_CWS_P.values.tolist()[3][4:])

#Collecting all Pearson sensor pairs into one dataframe
dfs_all_P = pd.DataFrame(data=zip(x,y,z),                   #Plotting into one scatterplot
                        index=['AB', 'BD', 'AD', 'AE' ,'BC' ,'BD' ,'BE', 'CD', 'CE', 'DE'], 
                        columns=['Temperature', 'WBGT','CrossWind Speed'])

#Plotting into one scatterplot.
# Jupyter Notebook launch is advised for this plot
# Type #%% to activate code as Jupyter Notebook cell (above imports) 
# see below for alternative.
#fig = px.scatter(dfs_all_P, title="Pearson's rank Coefficient")
#fig.show()                      #You can save the file as png from this pop-up

#If plotly's px.scatter did not load for you
# or you don't want to use #%% / Jupyter Notebook extension
# uncheck following to go for the alternative:
#plt.figure()
#sns.scatterplot(data=dfs_all_P)

#Spearmann's Coefficient Scatterplot for all three variables: Temperature, WBGT & Crosswind Speed
#Creating pairs AB, BD, AD, AE ,BC , BD, BE, CD, CE, DE
x = dfs_Temp_S.values.tolist()[0][1:]
x.extend(dfs_Temp_S.values.tolist()[1][2:])
x.extend(dfs_Temp_S.values.tolist()[2][3:])
x.extend(dfs_Temp_S.values.tolist()[3][4:])
y = dfs_WBGT_S.values.tolist()[0][1:]
y.extend(dfs_WBGT_S.values.tolist()[1][2:])
y.extend(dfs_WBGT_S.values.tolist()[2][3:])
y.extend(dfs_WBGT_S.values.tolist()[3][4:])
z = dfs_CWS_S.values.tolist()[0][1:]
z.extend(dfs_CWS_S.values.tolist()[1][2:])
z.extend(dfs_CWS_S.values.tolist()[2][3:])
z.extend(dfs_CWS_S.values.tolist()[3][4:])

#Collecting all Spearmann sensor pairs into one dataframe

dfs_all_S = pd.DataFrame(data=zip(x,y,z),                  #Plotting into one scatterplot
                        index=['AB', 'BD', 'AD', 'AE' ,'BC' ,'BD' ,'BE', 'CD', 'CE', 'DE'], 
                        columns=['Temperature', 'WBGT','CrossWind Speed'])

#Plotting into one scatterplot.
# Jupyter Notebook launch is advised for this plot
# Type #%% to activate code as Jupyter Notebook cell (above imports) 
# see below for alternative.
#fig = px.scatter(dfs_all_P, title="Spearmann's rank Coefficient")
#fig.show()                       #You can save the file as png from this pop-up

#If plotly's px.scatter did not load for you
# or you don't want to use #%% / Jupyter Notebook extension
# uncheck following to go for the alternative:
#plt.figure()
#sns.scatterplot(data=dfs_all_S)

#CDF Temperature values with corresponding confidence interval
plt.figure()
plt.hist(dfs['Temperature'], bins=50, histtype= 'step', edgecolor='k', density=True, cumulative=True)
plt.plot()
plt.ylabel('Cumulative Density')
plt.xlabel('Temp in C')
plt.title('CDF Temperatures Sensors A - E')
#plt.savefig('CDF_Temp2.png')
plt.show()
#Print 95% confidence intervals for all sensors 
#Temperature 
#confidence_interval_95(dfs['Temperature']).to_excel('95_Temp.xlsx')
print(confidence_interval_95(dfs['Temperature']))


#CDF Wind Speed values
plt.figure()
plt.hist(dfs['Wind Speed'], bins=50, histtype= 'step', edgecolor='k', density=True, cumulative=True)
plt.plot()
plt.ylabel('Cumulative Density')
plt.xlabel('Windspeed in m/s')
plt.title('CDF Windspeed Sensors A - E')
#plt.savefig('CDF_Windspeed.png')
plt.show()
#Print 95% confidence intervals for all sensors 
#Wind Speed values

#Computing all the confidence 95% intervals for all sensors 
#Values Temperature and Wind Speed
df_CI = dfs.filter(['Temperature', 'Wind Speed']) 
#df_CI.apply(lambda x: confidence_interval_95(df_CI), axis=1).to_csv('95_CI_Temp_WS.csv')
#df_CI.apply(lambda x: confidence_interval_95(df_CI), axis=1).to_excel('95_CI_Temp_WS.excel')




##A4 hypothesis tests input between two sensors
#i.e. A = test1 B = test2


def h_test(test1,test2):
    t, p = ttest_ind(test1,test2)
    return(p)


df_h_test = pd.DataFrame(index=['Temperature', 'Wind Speed'])


df_h_test['E-D'] = h_test(dfE['Temperature'],dfD['Wind Speed'])
df_h_test['D-C'] = h_test(dfD['Temperature'],dfC['Wind Speed'])
df_h_test['C-B'] = h_test(dfC['Temperature'],dfB['Wind Speed'])
df_h_test['B-A'] = h_test(dfB['Temperature'],dfA['Wind Speed'])
df_h_test = df_h_test.T
df_h_test.to_csv('h_test_all.csv')
df_h_test



#%%
'''
df_h_test['D-C'] = h_test(  DFH[['Temp','WS']][DFH.sensor=='D']  ,  DFH[['Temp','WS']][DFH.sensor=='C']  )
df_h_test['C-B'] = h_test(  DFH[['Temp','WS']][DFH.sensor=='C']  ,  DFH[['Temp','WS']][DFH.sensor=='B']  )
df_h_test['B-A'] = h_test(  DFH[['Temp','WS']][DFH.sensor=='B']  ,  DFH[['Temp','WS']][DFH.sensor=='A']  )
df_h_test = df_h_test.T
df_h_test.to_csv('h_test_all.csv')
df_h_test


def h_test(test1,test2):
    t, p = ttest_ind(test1,test2)
    return(p)

print(h_test(dfE['Temperature'], dfD['Temperature']))



df_h_test = pd.DataFrame(index=['Temperature', 'Wind Speed'])

df_h_test['E-D'] = h_test(dfE['Temperature'],dfD['Temperature'])

#%%

hypo_df['E-D'] = hypothesis_tp(  a4[['Temp','WS']][a4.sensor=='E']  ,  a4[['Temp','WS']][a4.sensor=='D']  )
hypo_df['D-C'] = hypothesis_tp(  a4[['Temp','WS']][a4.sensor=='D']  ,  a4[['Temp','WS']][a4.sensor=='C']  )
hypo_df['C-B'] = hypothesis_tp(  a4[['Temp','WS']][a4.sensor=='C']  ,  a4[['Temp','WS']][a4.sensor=='B']  )
hypo_df['B-A'] = hypothesis_tp(  a4[['Temp','WS']][a4.sensor=='B']  ,  a4[['Temp','WS']][a4.sensor=='A']  )
hypo_df = hypo_df.T
hypo_df.to_csv('./exports/hypo_p_val.csv')
hypo_df


'''


# %%
