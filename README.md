# pyBinarize
Binarizes gene expression data using a k-means based approach that is ported from the R package Binarize.

This is a python port of the k-means based binarization in the R package <a href='https://cran.r-project.org/web/packages/Binarize/index.html'>Binarize</a>.

There are two functions that can be imported by using:

```python
import pyBinarize
```

The functions in pyBinarize are:

* <b>binarize_matrix</b>(<i>df1</i>) - which binarizes a full Pandas DataFrame (df1) and returns the a new binarized Pandas DataFrame.

* <b>binarize_kMeans</b>(<i>series1</i>) - which binarizes a single Pandas Series serires1 and returns a new Numpy ndarray.

For usage please take a look at test.py:

```python
import pandas as pd
import pyBinarize as pyBin

# Read in data
df1 = pd.read_csv('exampleExp.csv', header=0, index_col=0)

# Binarize a Series
series1 = pyBin.binarize_kMeans(df1.iloc[0])
print(series1)

# Binraize a DataFrame
bin_df1 = pyBin.binarize_matrix(df1)
print(bin_df1.shape)
```
