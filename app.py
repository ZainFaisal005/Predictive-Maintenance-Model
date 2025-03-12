import os
import numpy as np
import pandas as pd
import joblib
import tensorflow as tf
from flask import Flask, request, render_template, jsonify

# Load the pre-trained models and preprocessor
preprocessor = joblib.load("preprocessor.pkl")
rf_model = joblib.load("random_forest_model.pkl")
ann_model = tf.keras.models.load_model("ann_model.h5")
lstm_model = tf.keras.models.load_model("lstm_model.h5")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from form
        data = request.form.to_dict(flat=True)

        # Convert data to DataFrame
        df = pd.DataFrame([data])

        # Convert numerical columns to correct data type
        numerical_cols = ['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']
        for col in numerical_cols:
            df[col] = pd.to_numeric(df[col])

        # Preprocess input data
        transformed_data = preprocessor.transform(df)

        # Make predictions
        rf_pred = rf_model.predict(transformed_data)
        ann_pred = (ann_model.predict(transformed_data) > 0.5).astype(int)
        lstm_pred = (lstm_model.predict(np.expand_dims(transformed_data, axis=1)) > 0.5).astype(int)

        # Majority voting for final decision
        final_pred = int((rf_pred[0] + ann_pred[0][0] + lstm_pred[0][0]) >= 2)

        # Convert to human-readable format
        result_text = "Failure" if final_pred == 1 else "Not Failure"

        return render_template('index.html', prediction_text=result_text)

    except Exception as e:
        return render_template('index.html', prediction_text="Error: " + str(e))

if __name__ == '__main__':
    app.run(debug=True)