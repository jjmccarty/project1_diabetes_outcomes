# Dependencies
import requests
import time
from dotenv import load_dotenv
import os
import pandas as pd
import json
import sys
import pathlib
import csv
import datetime


def getDiabetesDF_OverallCrude():
    df = getDataFrameForFile('overall_crude')
    #do cleaning work here
    cleanBasicData(df)
    return df 
        
def getDiabetesDF_OverallAgeAdjusted():
    df = getDataFrameForFile('overall_ageadjusted')
    #do cleaning work here
    cleanBasicData(df)
    return df 

def getDiabetesDF_BySex_Crude():
    df = getDataFrameForFile('female_crude')
    #do cleaning work here
    cleanBasicData(df)
    return df 

def getDiabetesDF_BySex_AgeAdjusted():
    df = getDataFrameForFile('female_ageadjusted')
    #do cleaning work here
    cleanBasicData(df)
    return df 

def getDiabetesDF_ByAge():
    df = getDataFrameForFile('age_18to44')
    #do cleaning work here
    cleanBasicData(df)
    return df 

def getDiabetesDF_ByEthnicity():
    df = getDataFrameForFile('ethno_asian_crude')
    #do cleaning work here
    cleanBasicData(df)
    return df 

def cleanBasicData(df):
    print(df.columns)
    df.drop(columns=['LocationDesc', 
                     'TopicID', 
                     'DataSource', 
                     'DataSourceUrl', 
                     'Question', 
                     'QuestionID', 
                     'StratificationCategory', 
                     'DataValueUnit', 
                     'DisplayOrder', 
                     'DataValueFootnoteSymbol'], inplace=True)
    
    print(df.columns)



def getDataFrameForFile(filename):
    print(f'----> Retrieving information for {filename}')
    df_list = []
    for year in range(2019, 2023):
        filepath = f'Resources/diabetes_{str(year)}_{filename}.csv'
        print(filepath)
        df_list.append(pd.read_csv(filepath))

    df = pd.concat(df_list, join='outer')
    return df


if __name__ == '__main__':
    print('Run data_clean.py')

    print(getDiabetesDF_OverallCrude().info())
    #print(getDiabetesDF_OverallAgeAdjusted().info())
    #print(getDiabetesDF_ByEthnicity().info())
    #print(getDiabetesDF_BySex_Crude().info())
    #print(getDiabetesDF_BySex_AgeAdjusted().info())
    #print(getDiabetesDF_ByAge().info())