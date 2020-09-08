# Clara Garcia-Sanchez
# 12/08/2020
################################# DO NOT CHANGE #####################################
# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../common_functions/')
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
heights, weights = sample.htm3, sample.wtkg2
print(heights)
