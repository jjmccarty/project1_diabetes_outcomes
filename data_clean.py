"""
THIS FILE IS DEPRECATED AND NOT USED IN THE FINAL SOLUTION/MODEL.

Utilities to extractdata from the specified diabetes source csv and provides a 
cleaned dataframe. 
"""

# Dependencies

import pandas as pd

midwest=['MI', 'OH', 'IN', 'IL', 'WI', 'MO', 'IA', 'MN', 'ND', 'SD', 'NE', 'KS']
northeast = ['PA', 'NY', 'VT', 'MA', 'CT', 'RI', 'NJ', 'NH', 'DE', 'MD', 'ME','DC']
southwest= ['TX', 'OK', 'AR', 'LA', 'MS', 'AL', 'GA', 'FL', 'SC', 'NC', 'VA', 'WV', 'KY', 'TN' ]
west=['MT', 'WY', 'CO', 'NM', 'AZ', 'UT', 'ID', 'OR', 'NV', 'CA', 'WA' ]
non_cont= ['HI', 'VI','AK', 'GU','PR']

def getDiabetesDF_OverallCrude():
    """
    Retrieves the overall_crude value for the diabetes rates in US population
    Args:None
    Returns:Dataframe of diabetes values
    """
    df = getDataFrameForFile('overall_crude')
    #do cleaning work here
    cleanBasicData(df)
    return df 
        
def getDiabetesDF_OverallAgeAdjusted():
    """
    Retrieves the overall_adjusted value for the diabetes rates in US population
    Args:None
    Returns:Dataframe of diabetes values
    """
    df = getDataFrameForFile('overall_ageadjusted')
    #do cleaning work here
    cleanBasicData(df)
    return df 

def getDiabetesDF_BySex_Crude():
    """
    Retrieves the diabetes rates in US population for male/female 
    Args:None
    Returns:Dataframe of diabetes values
    """
    df = getDataFrameForFile('female_crude')
    #do cleaning work here
    cleanBasicData(df)
    return df 


def getDiabetesDF_BySex_AgeAdjusted():
    """
    Retrieves the diabetes rates in US population for male/female adjusted by age
    Args:None
    Returns:Dataframe of diabetes values
    """
    df = getDataFrameForFile('female_ageadjusted')
    #do cleaning work here
    cleanBasicData(df)
    return df 

def getDiabetesDF_ByAge():
    """
    Retrieves the diabetes rates in US population by age
    Args:None
    Returns:Dataframe of diabetes values
    """
    df = getDataFrameForFile('age_18to44')
    #do cleaning work here
    cleanBasicData(df)
    return df 

def getDiabetesDF_ByEthnicity():
    """
    Retrieves the diabetes rates in US population by ethnicity 
    Args:None
    Returns:Dataframe of diabetes values
    """
    df = getDataFrameForFile('ethno_asian_crude')
    #do cleaning work here
    cleanBasicData(df)
    return df 

def cleanBasicData(df):
    """
    Cleans the dataframe and creates the Region data based on state/location
    Args:df - the dataframe values to clean/update
    Returns:None
    """
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
    
    df.loc[df['LocationAbbr'].isin (midwest),"Region"]='Midwest'
    df.loc[df['LocationAbbr'].isin (northeast),"Region"]='Northeast'
    df.loc[df['LocationAbbr'].isin (southwest),"Region"]='Southwest'
    df.loc[df['LocationAbbr'].isin (west),"Region"]='West'
    df.loc[df['LocationAbbr'].isin (non_cont),"Region"]='Non Cont'



def getDataFrameForFile(filename):
    """
    Retrieves the csv data for the filename specified for all years as a 
    single concatenated dataframe 
    Args: filename - the base name of the file to retrieve
    Returns:Dataframe of diabetes values
    """
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