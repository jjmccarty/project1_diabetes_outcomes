# Dependencies
import pandas as pd


def cleanBasicData(df):
    print(df.columns)
    
def getDataFrameForFile(filename):
    print(f'----> Retrieving information for {filename}')
    df = pd.read_csv(filename)
    return df

def getDiabetesDataframe():
    return getDataFrameForFile('Resources/diabetes.csv')

if __name__ == '__main__':
    print('Run data_outcomes.py')

    print(getDiabetesDataframe().info())
    