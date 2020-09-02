import pandas as pd

class Data_Getter_Pred:
    """
    This class shall  be used for obtaining the data from the source for prediction.

    Written By: iNeuron Intelligence
    Version: 1.0
    Revisions: None

    """
    def __init__(self, file_object, logger_object):
        self.prediction_file='MalwareData.csv'
   
    def get_data(self):
        """
        Method Name: get_data
        Description: This method reads the data from source.
        Output: A pandas DataFrame.

        """
        self.data= pd.read_csv(self.prediction_file) # reading the data file
        return self.data
  


