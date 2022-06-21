from EasyReport.easy_report import EdaReport
import pandas as pd

df = pd.read_csv("C:/Users/SUMEGH/Downloads/insurance.csv")

if __name__ == '__main__':
    a = EdaReport(data = df,target_column = 'expenses',regression = True)
    a.summary()