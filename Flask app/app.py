from flask import Flask,render_template,redirect,request
import pandas as pd
import pickle as pkl

app = Flask(__name__)

model = pkl.load(open('pipe.pkl','rb'))
@app.errorhandler(404)
def error(e):
    return redirect("/home")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def submit():
    if request.method=='POST':
    # Same form handling code as before
        disease = request.form.get('disease')
        fever = request.form.get('fever')
        cough = request.form.get('cough')
        fatigue = request.form.get('fatigue')
        difficulty_breathing = request.form.get('difficulty_breathing')
        gender = request.form.get('gender')
        blood_pressure = request.form.get('blood_pressure')
        cholesterol = request.form.get('cholesterol')
        age = request.form.get('age')

    form_data = {
        'Disease': [disease],
        'Fever': [fever],
        'Cough': [cough],
        'Fatigue': [fatigue],
        'Age':[age],
        'Difficulty Breathing': [difficulty_breathing],
        'Gender': [gender],
        'Blood Pressure': [blood_pressure],
        'Cholesterol Level': [cholesterol]
    }

    df = pd.DataFrame(form_data)
    val = model.predict(df)
    if val[0] == 0:
        return render_template("output.html",health_status = 'Congratulation !\nYour Health is Good')
    else:
        return render_template("output.html",health_status='Sorry\n Your health is Not Good')


if __name__=="__main__":
    app.run(debug=True,port=500)