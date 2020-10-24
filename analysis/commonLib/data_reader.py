from enum import Enum
import pandas as pd


class SuicideRawData(Enum):
    AGE_STANDARDIZED = 0
    SUICIDE_RATES = 1
    FACILITIES = 2
    SOCIOECONOMIC = 3
    HUMAN_RESOURCES = 4
    
class SuicideProcessedData(Enum):
    SUICIDE_RATES = 1
    FACILITIES = 2

class SuicideDataReader:
    
    def __init__(self):
        self.filepath = {}
        #raw data
        self.filepath.update({SuicideRawData.AGE_STANDARDIZED : '../../raw_data/age_standardized_suicide_rates.csv'})
        self.filepath.update({SuicideRawData.SUICIDE_RATES: '../../raw_data/crude_suicide_rates.csv'})
        self.filepath.update({SuicideRawData.FACILITIES:'../../raw_data/facilities.csv'})
        self.filepath.update({SuicideRawData.SOCIOECONOMIC:'../../raw_data/socioeconomic_indicator.csv'})
        self.filepath.update({SuicideRawData.HUMAN_RESOURCES:'../../raw_data/human_resources.csv'})
        #processed data
        self.filepath.update({SuicideProcessedData.SUICIDE_RATES: '../../processed_data/crude_suicide_rates.csv'})
        self.filepath.update({SuicideProcessedData.FACILITIES:'../../processed_data/facilities.csv'})
        
    def read_data(self, source, tidy = False):
        #check the arguments
        if (not isinstance(source,SuicideRawData)) and (not isinstance(source,SuicideProcessedData)):
            raise Exception('argument should be filled with SuicideRawData or SuicideProcessedData. '
                            'Try SuicideRawData.AGE_STANDARDIZED and/or SuicideProcessedData.FACILITIES')
            
        #read the data
        if (source == SuicideRawData.AGE_STANDARDIZED):
            data = pd.read_csv(self.filepath[source])
            data = data.rename(columns=lambda x: x.strip(' ').lower())
            data['sex'] = data['sex'].str.strip(' ')
            if (tidy):
                data = pd.melt(data, id_vars = ['country','sex'], var_name = 'year', value_name = 'age_standardized')
        elif (source == SuicideRawData.SUICIDE_RATES) | (source == SuicideProcessedData.SUICIDE_RATES):
            data = pd.read_csv(self.filepath[source])
            data = data.rename(columns=lambda x: x.strip(' ').lower())
            data['sex'] = data['sex'].str.strip(' ')
            if (tidy):
                data = pd.melt(data, id_vars = ['country','sex'], var_name = 'age_range', value_name = 'suicide_rate')
        else:
            data = pd.read_csv(self.filepath[source])
            data = data.rename(columns=lambda x: x.strip(' ').lower())
        
        return(data)