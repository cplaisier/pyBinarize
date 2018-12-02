##########################################################
## pyBinarize:  test.py                                 ##
##  ______     ______     __  __                        ##
## /\  __ \   /\  ___\   /\ \/\ \                       ##
## \ \  __ \  \ \___  \  \ \ \_\ \                      ##
##  \ \_\ \_\  \/\_____\  \ \_____\                     ##
##   \/_/\/_/   \/_____/   \/_____/                     ##
## @Developed by: Plaisier Lab                          ##
##   (https://plaisierlab.engineering.asu.edu/)         ##
##   Arizona State University                           ##
##   242 ISTB1, 550 E Orange St                         ##
##   Tempe, AZ  85281                                   ##
## @Author:  Chris Plaisier                             ##
## @License:  GNU GPLv3                                 ##
## @Port of:  Binarize by Hans A Kestler et al.         ##
## @Reference:  www.ncbi.nlm.nih.gov/pubmed/26468003    ##
##                                                      ##
## If this program is used in your analysis please      ##
## mention who built it. Thanks. :-)                    ##
##########################################################

import pandas as pd
import pyBinarize as pyBin

# Read in data
df1 = pd.read_csv('exampleExp.csv',header=0, index_col=0)

# Binarize a Series
series1 = pyBin.binarize_kMeans(df1.loc[2636])
print(series1)

# Binraize a DataFrame
bin_df1 = pyBin.binarize_kMeans_matrix(df1)
print(bin_df1.shape)

