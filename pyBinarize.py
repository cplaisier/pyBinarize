##########################################################
## pyBinarize:  pyBinarize.py                           ##
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

#import numpy as np
import pandas as pd
from sklearn.cluster import KMeans 

def binarize_gtZero(series1):
    """
    Purpose:  Binarizes a vector of real-valued data using a cutoff of greater than zero. Designed to work with RNA-seq count data. 
    Parameters:
        v1 = Pandas series (pandas.core.series.Series) of values to binarize
    Returns:
        returnSeries = binarized Pandas series (pandas.core.series.Series)
    """
    # Check if input series1 is Pandas series
    if not isinstance(series1, (pd.core.series.Series) ):
        print('Not Pandas series.')
        return -1
    # Check if zero is smallest value (count data)
    if not list(min(series1))==0:
        print('Not count data.')
        return -1
    # If greater than zero then 1
    returnSeries = series1.copy()
    returnSeries[returnSeries>0] = 1
    return returnSeries

def binarize_matrix_gtZero(df1):
    """
    Purpose:  Binarizes a full Pandas dataframe row by row using the binarize_gtZero function. 
    Parameters:
        df1 = Pandas dataframe (pandas.core.frame.DataFrame) filed with values to binarize
    Returns:
        bin_df1 = binarized dataframe computed from the input Pandas dataframe
    """
    # Create a location to store binarized data
    bin_df1 = df1.copy()
    for row1 in df1.index:
        bin_df1.loc[row1] = binarize_gtZero(df1.loc[row1])
    return bin_df1

def binarize_kMeans(series1):
    """
    Purpose:  Binarizes a vector of real-valued data using the k-means clustering algorithm. The data is first split into 2 clusters.The values belonging to the cluster with the smaller centroid are set to 0, and the values belonging to the greater centroid are set to 1. 
    Parameters:
        v1 = Pandas series (pandas.core.series.Series) of values to binarize
    Returns:
        labels1 = numpy array of binarized data
    """
    # Check if input series1 is Pandas series
    if not isinstance(series1, (pd.core.series.Series) ):
        print('Not Pandas series.')
        return -1
    # Remove NAs from series
    noNAseries = series1.dropna()
    # K-means clustering with 2 clsuters
    kmeans1 = KMeans(n_clusters=2).fit(noNAseries.values.reshape(-1,1))
    # Get lables from clustering
    labels1 = kmeans1.labels_
    # Ensure that label of 0 is cluster with lowest mean value, and 1 is the highest mean value
    centers1 = [i[0] for i in kmeans1.cluster_centers_]
    if centers1[0]>centers1[1]:
        labels1 = abs(labels1-1)
    returnSeries = series1.copy()
    for id1 in range(len(noNAseries.index)):
        returnSeries[noNAseries.index[id1]] = labels1[id1]
    return returnSeries

def binarize_kMeans_matrix(df1):
    """
    Purpose:  Binarizes a full Pandas dataframe row by row using the binarize_kMeans function. 
    Parameters:
        df1 = Pandas dataframe (pandas.core.frame.DataFrame) filed with values to binarize
    Returns:
        bin_df1 = binarized dataframe computed from the input Pandas dataframe
    """
    # Create a location to store binarized data
    bin_df1 = df1.copy()
    for row1 in df1.index:
        bin_df1.loc[row1] = binarize_kMeans(df1.loc[row1])
    return bin_df1

