from statistics import BasicStatistics
from graphs import Graphs


class EasyReport:
    """
    Do Exploratory Data Analysis(EDA) and return it.

    parameters:
    ---------------------------------------------------
    data: (DataFrame) Dataset
    target_column: (str) Name of the target column
    regression: (bool) for Regression poblem it is True
                       for Classification problem it is False (default)

    """

    def __init__(self, data, target_column, regression=False):
        self.df = data
        self.target_column_name = target_column
        # Creating column list with all the columns element except the target column
        self.columns = [i for i in self.df.columns if i != self.target_column_name]
        # Creating a list of categorical variable
        self.Categorical = [i for i in self.columns if self.df[i].dtypes == object or self.df[i].nunique() < 10]
        # Creating a list of numerical variable
        self.Numerical = [i for i in self.columns if self.df[i].dtypes != object and i not in self.Categorical]
        self.isRegression = regression
        self.graph = Graphs(data, target_column, regression)
        self.stat = BasicStatistics(data, target_column, regression)

    def summary(self):
        """
        Return a EDA report of the given dataset
        """
        self.stat.shape()
        self.stat.description()
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
