import pandas as pd

class Data_Getter:
    """
    This class shall  be used for obtaining the data from the source for training.

    Written By: iNeuron Intelligence
    Version: 1.0
    Revisions: None

    """
    def __init__(self, file_object, logger_object):
        self.training_file='Training_FileFromDB/InputFile.csv'
   
    def get_data(self):
        """
        Method Name: get_data
        Description: This method reads the data from source.
        Output: A pandas DataFrame.
        On Failure: Raise Exceptio

        """
        self.data= pd.read_csv(self.training_file) # reading the data file
        return self.data
       

