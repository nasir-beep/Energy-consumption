# Energy Consumption Platform

## Overview
Energy Consumption Platform is a machine learning web application built using Python and Streamlit. The application predicts energy consumption classes using building and environmental data.

## Problem Statement
The project addresses the challenge of predicting energy consumption to improve energy efficiency and support sustainable energy management.

## Features
- Machine learning energy prediction
- Interactive Streamlit dashboard
- Real-time prediction
- Random Forest classification model
- Modern UI design
- Reusable saved model

## Dataset Inputs
The model uses:
- Temperature
- Humidity
- SquareFootage
- Occupancy
- RenewableEnergy

Target variable:
- Energy_Class

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib
- Streamlit

## Machine Learning Models
- Decision Tree
- Random Forest

Random Forest was selected as the final model.

## Evaluation Metrics
- Accuracy
- Precision
- Recall
- Confusion Matrix

## Installation

Install dependencies:

```bash
pip install pandas numpy matplotlib scikit-learn streamlit joblib
```

## Run the App

```bash
py -m streamlit run app.py
```

Then open:

http://localhost:8501

or visit:

https://energy-consumptiongit-jusk7vhcykjsh3jszpejt6.streamlit.app/

## How to Use
1. Open the Streamlit app
2. Enter input values
3. Click Predict Energy Class
4. View prediction results

## Future Improvements
- Charts and analytics
- Feature importance visualization
- Cloud deployment
- Advanced dashboard UI

## Author
Ntokozo Ngomane - Data Science Student
