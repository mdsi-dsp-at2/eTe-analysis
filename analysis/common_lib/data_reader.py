#A module to read and transform data related to suicide rate for further analysis.
#Data are stored in the raw_data folder for the original dataset and processed_data for the cleaned dataset.
from enum import Enum
import pandas as pd

class SuicideRawData(Enum):
    '''List of members to identify the name of each dataset stored in the raw_data folder.
       One enumerator member represents one file in the folder.
    '''
    AGE_STANDARDIZED = 0
    SUICIDE_RATES = 1
    FACILITIES = 2
    SOCIOECONOMIC = 3
    HUMAN_RESOURCES = 4
    MENTAH_HEALTH_POLL = 5
    
class SuicideProcessedData(Enum):
    '''List of members to identify the name of each cleaned dataset stored in the processed_data folder.
       One enumerator member represents one file in the folder.
    '''
    SUICIDE_RATES = 1
    FACILITIES = 2

class SuicideDataReader:
    ''' A SuicideDataReader object will read a CSV file stored in the raw_data or processed_data folder and load it into 
        a data frame. The object also able to transform the data frame into a tidy format (for particular files only, 
        e.g., AGE_STANDARDIZED and SUICIDE_RATES, as other files have come in a tidy form).
    '''
    
    def __init__(self, relative_path = '../../'):
        '''Initiate the SuicideDataReader object, including specifying the file path and file name of each 
           SuicideRawData and SuicideProcessedData member.
            
           Argument:
               relative_path: the location of the raw_data or processed_data folder relative to the location of the script
        '''
        self.filepath = {}
        #raw data
        self.filepath.update({SuicideRawData.AGE_STANDARDIZED : relative_path+'raw_data/age_standardized_suicide_rates.csv'})
        self.filepath.update({SuicideRawData.SUICIDE_RATES : relative_path+'raw_data/crude_suicide_rates.csv'})
        self.filepath.update({SuicideRawData.FACILITIES : relative_path+'raw_data/facilities.csv'})
        self.filepath.update({SuicideRawData.SOCIOECONOMIC : relative_path+'raw_data/socioeconomic_indicator.csv'})
        self.filepath.update({SuicideRawData.HUMAN_RESOURCES : relative_path+'raw_data/human_resources.csv'})
        self.filepath.update({SuicideRawData.MENTAH_HEALTH_POLL : relative_path+'raw_data/mental_health_poll_updated.csv'})
        #processed data
        self.filepath.update({SuicideProcessedData.SUICIDE_RATES : relative_path+'processed_data/crude_suicide_rates.csv'})
        self.filepath.update({SuicideProcessedData.FACILITIES : relative_path+'processed_data/facilities.csv'})
        
    def read_data(self, source, tidy = False):
        '''Read the CSV file and load it into a data frame.
        
           Argument:
               source (enum): the member name of the dataset that will be loaded, e.g., SuicideRawData.AGE_STANDARDIZED 
               tidy (bool): is the dataset needs to be transformed into a tidy form (only applied to AGE_STANDARDIZED &
                             SUICIDE_RATES)
           
           Return:
               a data frame that store the dataset
        '''
        #check the arguments, where it only allows to be filled with the member of SuicideRawData or SuicideProcessedData
        if (not isinstance(source,SuicideRawData)) and (not isinstance(source,SuicideProcessedData)):
            raise Exception('argument should be filled with SuicideRawData or SuicideProcessedData. '
                            'Try SuicideRawData.AGE_STANDARDIZED and/or SuicideProcessedData.FACILITIES')
            
        #read the data and load them into a dataframe
        data = pd.read_csv(self.filepath[source])
        #for consistency purposes, change the case of the column names into a lower case and remove extra spaces
        data = data.rename(columns=lambda x: x.strip(' ').lower())
        
        #additional process applied to a particular dataset, such as AGE_STANDARDIZED and SUICIDE_RATES
        #1. remove extra spaces from a particular column
        #2. these dataset doesn't come in a tidy format, so if the users requested, the function will transform the dataset
        #   into the tidy form
        if (source == SuicideRawData.AGE_STANDARDIZED):
            #remove the extra spaces in the value of sex's column to ensure the filtering able to return valid rows
            #(no need to add spaces when performs the filtering)
            data['sex'] = data['sex'].str.strip(' ')
            if (tidy):
                #gather the suicide rates in multiple columns of years into two columns: year to keep the reference year, 
                #and age_standardized to store the value
                data = pd.melt(data, id_vars = ['country','sex'], var_name = 'year', value_name = 'age_standardized')
        elif (source == SuicideRawData.SUICIDE_RATES) or (source == SuicideProcessedData.SUICIDE_RATES):
            #remove the extra spaces in the value of sex's column to ensure the filtering able to return valid rows
            #(no need to add spaces when performs the filtering)
            data['sex'] = data['sex'].str.strip(' ')
            if (tidy):
                #gather the suicide rates in multiple columns of ages into two columns: age_range to keep the list of age 
                #range, and suicide_rate to store the value
                data = pd.melt(data, id_vars = ['country','sex'], var_name = 'age_range', value_name = 'suicide_rate')
        
        return(data)

    

