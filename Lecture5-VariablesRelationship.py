# Clara Garcia-Sanchez
# 12/08/2020
################################# DO NOT CHANGE #####################################
import numpy as np																	#
import matplotlib.pyplot as plt														#
import pandas as pd																	#
from analytic import ReadBabyBoom 
import thinkstats2
import thinkplot
import brfss
#####################################################################################
df = brfss.ReadBrfss(nrows=None)
sample = thinkstats2.SampleRows(df,5000)
heights, wreights = sample.htm3, sample.wtkg2
print(heights)
