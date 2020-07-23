from flask import Flask,request, url_for, redirect, render_template, jsonify
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
cols = ['hour', 'is_holiday', 'day_of_week']

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
    item = [x for x in request.form.values()]
    data = []

    # As the The training data was dummified one, so we have to pass the 
    # test data in the same format ('hour','is_holiday','day_of_week')
    
    data.append(item[0])
    
    # is holiday
    if item[1] == 'Yes':
        data.append(0)
        data.append(1)
    else:
        data.append(1)
        data.append(0)
        
    # fri, mon, sat , sun, thu, tue, wed
    if item[2] == 'Fri':
        data.append(1)
        data.append(0)
        data.append(0)
        data.append(0)
        data.append(0)
        data.append(0)
        data.append(0)
    
    elif item[2] == 'Mon':
        data.append(0)
        data.append(1)
        data.append(0)
        data.append(0)
        data.append(0)
        data.append(0)
        data.append(0)
    
    
    elif item[2] == 'Sat':
        data.append(0)
        data.append(0)
        data.append(1)
        data.append(0)
        data.append(0)
        data.append(0)
        data.append(0)
    
    elif item[2] == 'Sun':
        data.append(0)
        data.append(0)
        data.append(0)
        data.append(1)
        data.append(0)
        data.append(0)
        data.append(0)
    
    
    elif item[2] == 'Thu':
        data.append(0)
        data.append(0)
        data.append(0)
        data.append(0)
        data.append(1)
        data.append(0)
        data.append(0)
    
    elif item[2] == 'Tue':
        data.append(0)
        data.append(0)
        data.append(0)
        data.append(0)
        data.append(0)
        data.append(1)
        data.append(0)
    else:
        data.append(0)
        data.append(0)
        data.append(0)
        data.append(0)
        data.append(0)
        data.append(0)
        data.append(1)
    
    prediction = np.round(model.predict([data])[0])

    
    return render_template('home.html',pred='Total Bike ride counts for the day will be {}'.format(prediction))



#@app.route('/predict_api',methods=['POST'])
#def predict_api():
#    data = request.get_json(force=True)
#    data_unseen = pd.DataFrame([data])
#    prediction = predict_model(model, data=data_unseen)
#    output = prediction.Label[0]
#    return jsonify(output)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)