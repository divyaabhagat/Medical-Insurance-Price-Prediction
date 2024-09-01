import numpy as np
from flask import Flask, render_template,request,jsonify
from KNN_MODEL.utils import MedicalInsurance

app=Flask(__name__)
#defining home api
@app.route('/')
def get_home_api():
    return render_template('index.html')
#defning prediction api

@app.route('/predict_charges',methods=['GET',"POST"])
def get_insurance():
    if request.method=='POST':

        data=request.form
        print('>>>>>',data)

        age= eval(data['age'])
        gender=data['gender']
        bmi=float(data['bmi'])
        smoker=data['smoker']
        children=int(data['children'])
        region=data['region']

        med_obj=MedicalInsurance(age,gender,bmi,smoker,children,region)
        charges=med_obj.get_predict_charges()[0]
        return jsonify({"Result":f"Predicted medical insurance price is {np.around(charges,2)}"})
    
    else:
        age= eval(request.args.get('age'))
        gender=request.args.get('gender')
        bmi=float(request.args.get('bmi'))
        smoker=request.args.get('smoker')
        children=int(request.args.get('children'))
        region=request.args.get('region')
        medical = MedicalInsurance(age,gender,bmi,smoker,children,region)
        charges1 = medical.get_predicted_charges()

        return render_template("index.html",charges=charges1)
    
if __name__ == "__main__":
    app.run()