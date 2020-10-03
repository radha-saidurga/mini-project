#importing all the libraries
from flask import Flask, render_template, request
import tensorflow as tf
import keras
from keras.models import load_model
from keras.models import Sequential
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


app = Flask(__name__)


#Loading the saved model
m =  tf.keras.models.load_model('C:/Users/GOVIND/Desktop/mini project/atr.h5',compile=True,custom_objects=None)

#routes 
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        income = request.form['income']
        age = request.form['age']
        dailyRate = request.form['daily-rate']
        educationField = request.form['education-field']
        jobSatisfaction = request.form['job-satisfaction']
        jobRole = request.form['job-role']
        gender = request.form['gender']
        performance = request.form['performance']
        workingYears = request.form['working-years']
        workLife = request.form['work-life']
        years = request.form['years-at']
        print(income)
        print(age)
        print(dailyRate)
        print(educationField)
        print(jobSatisfaction)
        print(jobRole)
        print(gender)
        print(performance)
        print(workingYears)
        print(workLife)
        print(years)
        #give the all the values required
        result = m.predict(np.array([[age,dailyRate,educationField,jobSatisfaction,jobRole,income,gender,performance,workingYears,workLife,years]]))
        #result = m.predict(np.array([[0,1,1,2,9,1102,3456,2,0,1,5933,1,2,42,7,6]]))
        print(result)
        if result[0][0] == 1:
            #this is success
            return render_template('success.html')
        else:
            #this is failure
            return render_template('failure.html')
    else:
        #some other error
        return render_template('error.html')




# to run the flask application
# debug = flase in production environment
if __name__ == "__main__":
    app.run(debug=False)