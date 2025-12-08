

from flask import Flask, render_template, request, send_file

import numpy as np
import joblib
from generate_report import create_pdf

app = Flask(__name__)

model = joblib.load('stress_model.pkl')
scaler = joblib.load('scaler.pkl')

stress_map = {0: 'Low Stress', 
              1: 'Moderate Stress', 
              2: 'High Stress'}

advice = {
    "Low Stress": ("20 min jogging", "https://open.spotify.com/playlist/37i9dQZF1DWWEJlAGA9gs0"),
    "Moderate Stress": ("30 min cycling","https://open.spotify.com/playlist/37i9dQZF1DWXe9gFZP0gtP"),
    "High Stress": ("Deep breathing", "https://open.spotify.com/playlist/37i9dQZF1DWU0ScTcjJBdj"),
}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    vals = [float(request.form[x]) for x in request.form]

    # Scale & predict
    scaled_vals = scaler.transform([vals])
    pred = model.predict(scaled_vals)[0]

    stress=stress_map[pred]
    exercise, music = advice[stress]



   
    return render_template(
        "result.html",
        stress=stress,
        exercise=exercise,
        music=music
    ) 


@app.route('/download_report')
def download_report():
    stress = request.args.get("stress")
    exercise = request.args.get("exercise")

    pdf_path = create_pdf(stress, exercise)
    return send_file(pdf_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
