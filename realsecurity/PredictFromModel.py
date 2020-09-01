import pandas as pd
import numpy as np
import joblib 
import logging

logger= logging.getLogger()


def predictionFromModel(path):
    #self.log_writer = logger.App_Logger(
    #pred_data_val.deletePredictionFile() #deletes the existing prediction file from last run!
    #data_getter=data_loader_prediction.Data_Getter_Pred(path)
    #data=data_getter.get_data()
    modelReload1=joblib.load('featselect.pkl')
    Data_new = modelReload1.transform(path)

    modelReload2=joblib.load('RFModelforMD.pkl')
    #modelReload2.predict(Legit_Test)

    #modelReload1=joblib.load('featselect.pkl')
    #Data_new = modelReload1.transform(Data)

    #Legit_Train, Legit_Test, Malware_Train, Malware_Test = train_test_split(Data_new, Target ,test_size=0.2)

    #modelReload2=joblib.load('RFModelforMD.pkl')
    result = modelReload2.predict(Legit_Test)

    final= pd.DataFrame(list(zip(result)),columns=['Predictions'])
    path="Prediction_Output_File/Predictions.csv"
    final.to_csv("Prediction_Output_File/Predictions.csv",header=True,mode='a+') #appends result to prediction file
    self.log_writer.log(self.file_object,'End of Prediction')
    return path