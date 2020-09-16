#Homework 1

#Author: Daniel Dobson
#Student number: 5152739

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Means, of each variable in 'HEAT - A_final.xls'
df = pd.read_excel('HEAT - A_final.xls', skiprows=[0,1,2,4])
df.apply(np.mean).to_csv('Means_A_.csv')

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