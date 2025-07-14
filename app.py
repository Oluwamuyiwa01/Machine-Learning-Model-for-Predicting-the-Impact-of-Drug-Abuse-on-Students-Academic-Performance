
from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load("Model/random_forest.pkl")

impact_mapping = {0: "No Impact", 1: "Low Impact", 2: "Moderate Impact", 3: "High Impact"}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        
        input_data = np.array([[
            int(data['age']),
            int(data['gender']),
            int(data['socioeconomic']),
            int(data['drug_type']),
            int(data['age_first_used']),
            int(data['drug_frequency']),
            int(data['reason_for_use']),
            int(data['family_support']),
            float(data['attendance']),
            float(data['gpa'])
        ]])

     
        prediction = model.predict(input_data)[0]
        predicted_impact = impact_mapping.get(prediction, "Unknown")

        return jsonify({'prediction': predicted_impact})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

