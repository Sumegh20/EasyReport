import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno


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
        if self.isRegression:
            fig, axes = plt.subplots(1, 2, figsize=(20, 5))
            fig.add_subplot(121)
            sns.histplot(x=self.target_column_name, data=self.df, color='red')
            fig.add_subplot(122)
            sns.boxplot(x=self.target_column_name, data=self.df)
        else:
            plt.figure(figsize=(10, 7))
            sns.countplot(self.df[self.target_column_name])
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
        fig, axes = plt.subplots(1, 2, figsize=(20, 5))
        fig.add_subplot(121)
        values = self.df[feature].value_counts()
        labels = self.df[feature].unique()
        plt.pie(values, autopct='%.0f%%', labels=labels)
        fig.add_subplot(122)
        if self.isRegression:
            sns.boxplot(x=feature, y=self.target_column_name, data=self.df)
        else:
            sns.countplot(x=feature, data=self.df, palette='muted', hue=self.target_column_name)
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
        fig, axes = plt.subplots(1, 3, figsize=(20, 5))
        fig.add_subplot(131)
        sns.histplot(x=feature, data=self.df, color='red')
        fig.add_subplot(132)
        sns.boxplot(x=feature, data=self.df)
        fig.add_subplot(133)
        if self.isRegression:
            sns.scatterplot(x=feature, y=self.target_column_name, data=self.df)
        else:
            sns.histplot(x=feature, data=self.df, hue=self.target_column_name)
        plt.show()

    def missing_value_plot(self):
        """
        A bar chart visualization of the nullity of the given DataFrame.
        """
        msno.bar(self.df, color='blue')

    def correlation_heatmap(self):
        """
        Show the correlation heatmap
        """
        plt.figure(figsize=(20, 20))
        sns.heatmap(self.df.corr(), annot=True)
        plt.show()
