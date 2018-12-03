# pyBinarize
Binarizes gene expression data using a k-means based approach that is ported from the R package Binarize.

This is a python port of the k-means based binarization in the R package <a href='https://cran.r-project.org/web/packages/Binarize/index.html'>Binarize</a>. It also adds an additonal filter that we found useful for single cell RNA-seq (scRNA-seq) data. It dichotomizes scRNA-seq count data with a greater than zero filter.

There are two functions that can be imported by using:

```python
import pyBinarize
```

The functions in pyBinarize are:

* <b>binarize_matrix</b>(<i>df1</i>) - which binarizes a full Pandas DataFrame (df1) and returns the a new binarized Pandas DataFrame.

* <b>binarize_kMeans</b>(<i>series1</i>) - which binarizes a single Pandas Series serires1 and returns a new binarized Pandas Series.

For example usage of the k-means functions please take a look at test.py:

```python
import pandas as pd
import pyBinarize as pyBin

# Read in data
df1 = pd.read_csv('exampleExp.csv', header=0, index_col=0)

# k-means binarize a Series
series1 = pyBin.binarize_kMeans(df1.iloc[0])
print(series1)

# k-means binraize a DataFrame
bin_df1 = pyBin.binarize_kMeans_matrix(df1)
print(bin_df1.shape)
```

In process of making a greater than zero test case.
