import pandas as pd
import math
from scipy.stats import skew, kurtosis


class BasicStatistics:

    def __init__(self, data, target_column, regression):
        self.df = data
        self.target_column_name = target_column
        self.isRegression = regression

    def shape(self):
        """
        Print the shape of the dataset
        """
        print('\n-------------------------------------------------'
              'Data Shape-------------------------------------------------')
        print(f'The shape of the dataset is {self.df.shape}')

    def information(self):
        """
        Give the dataset basic information
        """
        print('\n-------------------------------------------------'
              'Data information-------------------------------------------------')
        self.df.info()

    def missing_values(self):
        """
        Shows the number of missing values
        """
        print('-------------------------------------------------'
              'Missing Value Table-------------------------------------------------')
        print(pd.DataFrame(self.df.isnull().sum(), columns=['# Missing Values']))
        print()

    def duplicates(self):
        """
        Showes all the duplicate rows in the dataset
        """
        print('---------------------------------------------------'
              'Duplicates Data---------------------------------------------------')
        print(f'\n Numbers of Duplicates Row: {self.df.duplicated().sum()}')
        if self.df.duplicated().sum() > 0:
            temp = pd.DataFrame(self.df[self.df.duplicated()].value_counts())
            temp = temp.rename(columns={0: '# Duplicates'})
            print(temp)

    def target_variable_statistical_summary(self):
        """
        Gives statistical values of the target variable
        """
        print('-------------------------------------------------', self.target_column_name,
              '-------------------------------------------------')
        try:
            if self.isRegression:
                self.numerical_statistical_summary(self.target_column_name)
            else:
                self.categorical_statistical_summary(self.target_column_name)
        except Exception as e:
            print(e)

    def categorical_statistical_summary(self, feature):
        """
        Gives statistical values of the categorical variable

        Parameters:
        ---------------------------------------------------
        Feature: (str) Name of the categorical variable
        """
        try:
            dec = {'Stat': ['values', 'inc_na', 'exc_na', '# missing values', '% missing values'],
                    'Values': [self.df[feature].unique(), len(self.df[feature].unique()),
                          self.df[feature].nunique(), self.df[feature].isnull().sum(),
                          round(self.df[feature].isnull().sum() / len(self.df), 2) * 100]
                    }
            temp = pd.DataFrame(dec)
            if self.df[feature].dtypes != 'object':
                print('Attribute type: Ordinal')
            else:
                print('Attribute type: Categorical')
            print(temp)
            print('\nCategory Count Table')
            print(self.df[feature].value_counts())
        except Exception as e:
            print(e)

    def numerical_statistical_summary(self, feature):
        """
        Gives statistical values of the numerical variable

        Parameters:
        ---------------------------------------------------
        Feature: (str) Name of the numarical variable
        """
        try:
            q1 = self.df[feature].quantile(0.25)
            q3 = self.df[feature].quantile(0.75)
            iqr = q3 - q1
            up = q3 + 1.5 * iqr
            lo = q1 - 1.5 * iqr

            dec = {'Stat': ['Minimum', '1st Quartile', 'Median', '3rd Quartile', 'Maximum', 'Mean', 'Variance',
                        'Standard deviation',
                        'Coefficient of variation (CV)', 'Skewness', 'Kartosis', '# Missing Values', '% Missing Values',
                        'IQR',
                        'lower', 'upper', '# Outlier_upper', '# Outlier_lower'],
                    'Values': [self.df[feature].min(), q1, self.df[feature].quantile(0.5), q3, self.df[feature].max(),
                          self.df[feature].mean(), self.df[feature].var(), math.sqrt(self.df[feature].var()),
                          math.sqrt(self.df[feature].var()) / self.df[feature].mean(),
                          skew(self.df[feature], axis=0, bias=True),
                          kurtosis(self.df[feature], axis=0, fisher=True, bias=True), self.df[feature].isnull().sum(),
                          round(self.df[feature].isnull().sum() / len(self.df) * 100, 2), iqr, lo, up,
                          len(self.df.loc[self.df[feature] < float(lo)]),
                          len(self.df.loc[self.df[feature] > float(up)])]
               }
            temp = pd.DataFrame(dec)
            print('Attribute type: Numerical')
            print(temp)
        except Exception as e:
            print(e)

    def correlation(self):
        """
        Show the correlation matrix
        """
        print('------------------------------------------------------'
              'Correlation----------------------------------------------------\n')
        try:
            print(self.df.corr())
        except Exception as e:
            print(e)
