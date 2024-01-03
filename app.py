from flask import Flask,render_template,request
from args import *
import numpy as np, pickle
with open('Model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('Scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    #return 'I am in first page'
    #print(request.method)
    #print(request.form)
    if request.method=='POST':
        bedrooms=request.form['bedrooms']
        bathrooms=request.form['bathrooms']
        sft=request.form['sft']
        location=request.form['location']
        status=request.form['status']
        property_type=request.form['property type']
        direction=request.form['direction']
        input_array=np.array([[bedrooms,bathrooms,location,sft,status,direction,property_type]])
        t_array=scaler.transform(input_array)
        prediction=model.predict(t_array)[0]
        return render_template('index.html',location_mapping = location_mapping,status_mapping=status_mapping,
                               direction_mapping=direction_mapping,property_type_mapping=property_type_mapping,prediction=prediction)
    else:
        return render_template('index.html',location_mapping = location_mapping,status_mapping=status_mapping,
                               direction_mapping=direction_mapping,property_type_mapping=property_type_mapping)
    return render_template('index.html')
@app.route('/second')
def second():
    return 'I am in second page'

@app.route('/third')
def third():
    return ' I am third page'
app.run(use_reloader=True,debug=True)