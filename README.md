"# House_prediction" 
House Price Prediction Using Machine Learning
Project Overview

This project focuses on predicting house prices using machine learning techniques.
The model is trained on the California Housing Dataset and aims to estimate the median house value based on various socio-economic and geographic features.

This project demonstrates a complete machine learning regression pipeline, including data preprocessing, feature scaling, model training, and evaluation.

Dataset

Dataset Name: California Housing Dataset

Source: Scikit-learn (fetch_california_housing)

Number of Instances: 20,640

Number of Features: 8

Features

MedInc – Median income in the block group

HouseAge – Median house age

AveRooms – Average number of rooms per household

AveBedrms – Average number of bedrooms per household

Population – Population of the block group

AveOccup – Average occupancy per household

Latitude – Latitude of the location

Longitude – Longitude of the location

Target Variable

MedHouseVal – Median house value (in $100,000s)

Technologies Used

Python

NumPy

Pandas

Matplotlib

Seaborn

Scikit-learn

Google Colab / Jupyter Notebook

Machine Learning Workflow

Data loading

Exploratory data analysis

Feature selection

Train–test split

Feature scaling using StandardScaler

Model training

Model evaluation

Models Implemented
1. Linear Regression (Baseline Model)

Used as a baseline regression model

Helps understand linear relationships between features and target

2. Random Forest Regressor (Improved Model)

Captures non-linear relationships

Provides better accuracy compared to linear regression

Feature Scaling

Feature scaling was applied using StandardScaler

fit_transform() used on training data

transform() used on test data to avoid data leakage

Model Evaluation Metrics

The models were evaluated using:

Root Mean Squared Error (RMSE)

R² Score (Coefficient of Determination)

Performance Summary

Linear Regression:

RMSE ≈ 0.73

R² Score ≈ 0.60

Random Forest Regressor:

RMSE ≈ 0.51

R² Score ≈ 0.80

Random Forest significantly outperformed Linear Regression.
