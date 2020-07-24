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
    
    data.append(int(item[0]))
    
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
    
    #data = [12, 0, 1, 0, 0, 0, 1, 0, 0, 0]
    prediction = int(model.predict([data])[0])
    #prediction = 150


    return render_template('home.html',pred='Total Bike ride counts on {} at {}:00 Hrs will be {}'.format(item[2], item[0],prediction))



#@app.route('/predict_api',methods=['POST'])
#def predict_api():
#    data = request.get_json(force=True)
#    data_unseen = pd.DataFrame([data])
#    prediction = prediction = np.round(model.predict([data_unseen])[0])
#    output = prediction.Label[0]
#    return jsonify(output)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)


#if __name__ == "__main__":
#    app.run(debug=True)