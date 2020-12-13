import flask
from flask import Flask, jsonify, request, render_template
import json
import pickle
import statsmodels.api as sm
import numpy as np
from sklearn.preprocessing import LabelEncoder


app = Flask(__name__)

def load_models():
    file_name = "models/test_file2.pickle"
    # file_name = "models/test_file.pickle"
    # with open(file_name, 'rb') as pickled:
    #     data = pickle.load(pickled)
    #     model = data['model']
    model = sm.load(file_name)
    return model

# @app.route('/')
# def home():
# 	return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # parse input features from request
    request_json = request.get_json()
    print(request_json)
    data_list = []

    # constant_value = request_json['constant']
    # data_list.append(constant_value)

    # farm_size = request_json['farm_size']
    # data_list.append(farm_size)

    # marital_status_married = request_json['marital_status_married']
    # data_list.append(marital_status_married)

    # marital_status_single = request_json['marital_status_single']
    # data_list.append(marital_status_single)

    # education_primary = request_json['education_primary']
    # data_list.append(education_primary)

    # education_secondary = request_json['education_secondary']
    # data_list.append(education_secondary)

    # education_tertiary = request_json['education_tertiary']
    # data_list.append(education_tertiary)

    # land_ownership_no = request_json['land_ownership_no']
    # data_list.append(land_ownership_no)

    # land_ownership_yes = request_json['land_ownership_yes']
    # data_list.append(land_ownership_yes)

    # age_group_adult = request_json['age_group_adult']
    # data_list.append(age_group_adult)

    # age_group_eldery = request_json['age_group_eldery']
    # data_list.append(age_group_eldery)

    # age_group_young_adult = request_json['age_group_young_adult']
    # data_list.append(age_group_young_adult)

    # age_group_youth = request_json['age_group_youth']
    # data_list.append(age_group_youth)
    ##################################################################################

    labelencoder = LabelEncoder()

#for marital status
    marital_status = request_json['marital_status']

    #the way it was encoded in the model
    marital_status_encoded = {'married': 0, 'single': 1}

    for key in marital_status_encoded:
    	if key == marital_status:
    	# if key in marital_status:
    		marital_status = marital_status_encoded[key]

    #appending to the array
    data_list.append(marital_status)

#for education
    education = request_json['education']

    #the way it was encoded in the model
    education_encoded = {'primary': 0, 'secondary': 1, 'tertiary': 2}

    for key in education_encoded:
    	if key == education:
    	# if key in marital_status:
    		education = education_encoded[key]

    #appending to the array
    data_list.append(education)


#for land ownership
    land_ownership = request_json['land_ownership']

    #the way it was encoded in the model
    land_ownership_encoded = {'no': 0, 'yes': 1}

    for key in land_ownership_encoded:
    	if key == land_ownership:
    		land_ownership = land_ownership_encoded[key]


    #appending to the array
    data_list.append(land_ownership)


#for farm_size
    farm_size = request_json['farm_size']
    farm_size = float(farm_size)
    farm_size = np.log10(farm_size)
    data_list.append(farm_size)


#for age group
    age_group = request_json['age_group']
    
    if age_group == '18-25':
    	age_group = 'youth'
    elif age_group == '26-35':
    	age_group = 'young_adult'
    elif age_group == '36-45':
    	age_group = 'adult'
    else:
    	age_group = 'eldery'


    #the way it was encoded in the model
    age_group_encoded = {'adult': 0, 'eldery': 1, 'young_adult': 2, 'youth': 3}

    for key in age_group_encoded:
    	if key == age_group:
    		age_group = age_group_encoded[key]

    #appending to the array
    data_list.append(age_group)
    

    #changing the string values in the list to float values
    x = [float(v) for v in data_list]


#with the web app

    # for rendering the results from html
    # float_features = [float(x) for x in request.form.values()]
    # # load model
    # model = load_models()
    # prediction = model.predict(np.array(float_features))[0]

###############################################




#with jeremy

    # x = request.args.getlist("input")
    # x = [float(v) for v in x]
    # print(x)
    # x = 
    # x = [1.00000, 0.30103, 1.00000, 0.00000,0.00000, 0.00000, 1.00000, 1.00000, 0.00000, 0.00000, 0.00000, 1.00000,0.00000]
 
    # load model
    # model = load_models()
    # # print("||||||||||||||||||")
    # # print(type(model))
    # prediction = model.predict(np.array(x))[0]
    # print(prediction)
    # response = json.dumps({'response': prediction})
    # return response, 200

########################################################

    # load model and predict
    model = load_models()
    prediction = model.predict(np.array(x))[0]
    # prediction = 19.098765
    prediction = 10**prediction
    response = json.dumps({'response': prediction})

    return response, 200


if __name__ == '__main__':
    application.run(debug=True)
