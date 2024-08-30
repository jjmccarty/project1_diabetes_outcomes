# Dependencies



import pandas as pd

midwest=['MI', 'OH', 'IN', 'IL', 'WI', 'MO', 'IA', 'MN', 'ND', 'SD', 'NE', 'KS']
northeast = ['PA', 'NY', 'VT', 'MA', 'CT', 'RI', 'NJ', 'NH', 'DE', 'MD', 'ME','DC']
southwest= ['TX', 'OK', 'AR', 'LA', 'MS', 'AL', 'GA', 'FL', 'SC', 'NC', 'VA', 'WV', 'KY', 'TN' ]
west=['MT', 'WY', 'CO', 'NM', 'AZ', 'UT', 'ID', 'OR', 'NV', 'CA', 'WA' ]
non_cont= ['HI', 'VI','AK', 'GU','PR']

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
    
    df.loc[df['LocationAbbr'].isin (midwest),"Region"]='Midwest'
    df.loc[df['LocationAbbr'].isin (northeast),"Region"]='Northeast'
    df.loc[df['LocationAbbr'].isin (southwest),"Region"]='Southwest'
    df.loc[df['LocationAbbr'].isin (west),"Region"]='West'
    df.loc[df['LocationAbbr'].isin (non_cont),"Region"]='Non Cont'



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