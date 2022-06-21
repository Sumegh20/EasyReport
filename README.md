
# Easy Report
Generates EDA reports from a pandas DataFrame.

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org)

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)  

## Features of the package
The pandas df.describe() function is great but a little 
basic, for serious exploratory data analysis for any 
classification or regression problem EasyReport helps the 
user for quick data analysis.

For each column the following statistics (if relevant for 
the column type) are presented:

- **Type inference:** detect the types of columns in a dataframe
- **Essentials:** type, unique values, missing values, outliers
- **Quantile statistics:** minimum value, Q1, median, Q3, maximum, interquartile range, upper, lower
- **Descriptive statistics:** mean, variance, standard deviation, coefficient of variation, kurtosis, skewness
- **Graphs:** Histogram, boxplot, countplot, pie, scatterplot
- **Correlations:** correlation matrix, heatmap
- **Duplicates:** total number of duplicate row and number of times they are repated  
- **Missing value:** number of missing values, dendrogram of missing values




## Installation
You can install using the pip package manager by running
```bash
pip install EasyReport
```
    
## Examples
### For Classification Problem
```python
import pandas as pd
from EasyReport.easy_report import EdaReport

#Read the dataset
df = pd.read_csv("Dataset")

report = EdaReport(data = df,target_column = 'target_column_name')
report.summary()
```

### For Regression Problem
```python
import pandas as pd
from EasyReport.easy_report import EdaReport

#Read the dataset
df = pd.read_csv("Dataset")

report = EdaReport(data = df,target_column = 'target_column_name',regression = True)
report.summary()
```
## Author

- [@Sumegh20](https://www.linkedin.com/in/sumegh-sen/)

