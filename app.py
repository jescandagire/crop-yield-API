import flask
from flask import Flask, jsonify, request, render_template
import json
import pickle
import statsmodels.api as sm
import numpy as np


app = Flask(__name__)

def load_models():
    file_name = "models/test_file.pickle"
    # with open(file_name, 'rb') as pickled:
    #     data = pickle.load(pickled)
    #     model = data['model']
    model = sm.load(file_name)
    return model

@app.route('/')
def home():
	return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # parse input features from request
    # print("hello")
    # request_json = request.get_json()
    # print(request_json)

    # for rendering the results from html
    float_features = [float(x) for x in request.form.values()]
    # load model
    model = load_models()
    prediction = model.predict(np.array(float_features))[0]








    # x = request.args.getlist("input")
    # x = [float(v) for v in x]
    # print(x)
    # x = 
    # x = [1.00000, 0.30103, 1.00000, 0.00000,0.00000, 0.00000, 1.00000, 1.00000, 0.00000, 0.00000, 0.00000, 1.00000,0.00000]
 
    # load model
    # model = load_models()
    # print("||||||||||||||||||")
    # print(type(model))
    # prediction = model.predict(np.array(x))[0]
    print(prediction)
    response = json.dumps({'response': prediction})
    return response, 200
    # response = json.dumps({'response': 'yahhhh!'})
    # return response, 200


if __name__ == '__main__':
    application.run(debug=True)