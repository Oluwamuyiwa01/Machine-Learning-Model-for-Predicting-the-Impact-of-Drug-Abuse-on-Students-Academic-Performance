#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("Model/random_forest.pkl")

# Mapping for predictions
impact_mapping = {0: "No Impact", 1: "Low Impact", 2: "Moderate Impact", 3: "High Impact"}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Convert input to numpy array
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

        # Make prediction
        prediction = model.predict(input_data)[0]
        predicted_impact = impact_mapping.get(prediction, "Unknown")

        return jsonify({'prediction': predicted_impact})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

