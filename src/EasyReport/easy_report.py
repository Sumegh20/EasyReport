import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno
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


class Graphs:

    def __init__(self, data, target_column, regression):
        self.df = data
        self.target_column_name = target_column
        self.isRegression = regression

    def target_variable_plot(self):
        """
        For Classification problem
            It draws the Count plot of the target variable
        For Regression problem
            It draws Histogram, Box plot of the target variable
        """
        d1 = self.df.copy()

        if self.isRegression:
            fig = plt.figure(figsize=(15, 5))
            ax1 = fig.add_subplot(1, 2, 1)
            sns.histplot(x=self.target_column_name, data=d1, color='red', ax=ax1)
            ax2 = fig.add_subplot(1, 2, 2)
            sns.boxplot(x=self.target_column_name, data=d1, ax=ax2)
        else:
            plt.figure(figsize=(10, 7))
            sns.countplot(d1[self.target_column_name])
            plt.title("Plot the target column " + self.target_column_name, size=20)
            plt.ylabel("Count", size=20)
            plt.xlabel("Classes", size=20)
            plt.show()

    def categorical_graphical_summary(self, feature):
        """
        For Classification problem
            It draws the Pie diagram and Countplot(Based on the target variable) of a categorical variable
        For Regression problem
            It draws the Pie diagram of a categorical variable and Boxplot of the target variable based
            on the categorical variable

        Parameters:
        ---------------------------------------------------
        Feature: (str) Name of the categorical variable
        """
        d1 = self.df.copy()

        if d1[feature].isnull().sum() > 0:
            d1[feature] = d1[feature].fillna('Missing')

        fig = plt.figure(figsize=(15, 5))
        fig.add_subplot(1, 2, 1)
        values = d1[feature].value_counts()
        labels = d1[feature].unique()
        plt.pie(values, autopct='%.0f%%', labels=labels)

        ax2 = fig.add_subplot(1, 2, 2)
        if self.isRegression:
            sns.boxplot(x=feature, y=self.target_column_name, data=d1, ax=ax2)
        else:
            sns.countplot(x=feature, data=d1, palette='muted', hue=self.target_column_name, ax=ax2)

        fig.tight_layout(pad=3.0)
        plt.show()

    def numerical_graphical_summary(self, feature):
        """
        For Classification problem
            It draws Histogram, Box plot and Histogram (Based on the target variable) of a numerical variable
        For Regression problem
            It draws Histogram, Box plot of a numerical variable and Scatter plot (target variable VS
            numerical variable)

        Parameters:
        ---------------------------------------------------
        Feature: (str) Name of the numerical variable
        """
        d1 = self.df.copy()

        fig = plt.figure(figsize=(20, 5))
        ax1 = fig.add_subplot(1, 3, 1)
        sns.histplot(x=feature, data=d1, color='red', ax=ax1)
        ax2 = fig.add_subplot(1, 3, 2)
        sns.boxplot(x=feature, data=d1, ax=ax2)
        ax3 = fig.add_subplot(1, 3, 3)
        if self.isRegression:
            sns.scatterplot(x=feature, y=self.target_column_name, data=d1, ax=ax3)
        else:
            sns.histplot(x=feature, data=d1, hue=self.target_column_name, ax=ax3)

        fig.tight_layout(pad=3.0)
        plt.show()

    def missing_value_plot(self):
        """
        A bar chart visualization of the nullity of the given DataFrame.
        """
        d1 = self.df.copy()
        msno.bar(d1, color='#52be80')

    def correlation_heatmap(self):
        """
        Show the correlation heatmap
        """
        d1 = self.df.copy()
        plt.figure(figsize=(20, 20))
        sns.heatmap(d1.corr(), annot=True)
        plt.show()


class EdaReport:
    """
    Do Exploratory Data Analysis(EDA) and return it.

    parameters:
    --------------------------------------------------------------------
    data: (DataFrame) Dataset
    target_column: (str) Name of the target column
    regression: (bool) for Regression problem it is True
                       for Classification problem it is False (default)

    """

    def __init__(self, data, target_column, regression=False):
        self.df = data
        self.target_column_name = target_column
        self.isRegression = regression
        self.graph = Graphs(data, target_column, regression)
        self.stat = BasicStatistics(data, target_column, regression)

        try:
            # Creating column list with all the columns element except the target column
            self.columns = [i for i in self.df.columns if i != self.target_column_name]

            # Creating a list of categorical variable
            self.Categorical = [i for i in self.columns if self.df[i].dtypes == object or self.df[i].nunique() < 10]

            # Creating a list of numerical variable
            self.Numerical = [i for i in self.columns if self.df[i].dtypes != object and i not in self.Categorical]
        except Exception as e:
            print(e)

    def summary(self):
        """
        Return a EDA report of the given dataset
        """
        try:
            self.stat.shape()
            self.stat.information()
            print()
            self.stat.target_variable_statistical_summary()
            self.graph.target_variable_plot()
            print()
            for i in self.Categorical:
                print('----------------------------------------------------', i,
                      '---------------------------------------------------\n')
                self.stat.categorical_statistical_summary(i)
                self.graph.categorical_graphical_summary(i)
                print('\n')
            for i in self.Numerical:
                print('----------------------------------------------------', i,
                      '----------------------------------------------------\n')
                self.stat.numerical_statistical_summary(i)
                self.graph.numerical_graphical_summary(i)
                print('\n')
            self.stat.correlation()
            self.graph.correlation_heatmap()
            self.stat.duplicates()
            print()
            self.stat.missing_values()
            self.graph.missing_value_plot()
        except Exception as e:
            print(e)
