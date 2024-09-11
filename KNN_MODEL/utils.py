import numpy as np
import pickle
import json
import config

class MedicalInsurance():
    def __init__(self,age,gender,bmi,smoker,children,region):
        self.age=age
        self.gender=gender.lower()
        self.bmi=bmi
        self.smoker=smoker.lower()
        self.children=children
        self.region='region_' + region

    def load_model(self):
        with open(config.model_path,'rb') as file:
            self.model=pickle.load(file)

        with open(config.scale_model_path,'rb') as file:
            self.scale=pickle.load(file)    

        with open(config.json_path,'r') as file:
            self.json_data=json.load(file)   

    def get_predict_charges(self):
        self.load_model()

        test_array=np.zeros(len(self.json_data['columns']))
        test_array[0]=self.age
        test_array[1]=self.json_data['gender'][self.gender]
        test_array[2]=self.bmi
        test_array[3]=self.json_data['smoker'][self.smoker]
        test_array[4]=self.children
        region1_index=self.json_data['columns'].index(self.region)
        test_array[region1_index]=1

        predict_charges=self.model.predict([test_array])
        return predict_charges

