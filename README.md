Weather Prediction Model

Using K-Nearest Neighbors (KNN) and Multiple Linear Regression

1. Introduction
1.1 Project Overview

Weather prediction is an important application of data science with real-world relevance in
agriculture, transportation, disaster management, and urban planning.

This project analyzes historical weather data from Bangalore city (1990–2022) and applies
machine learning techniques to predict weather conditions.
The dataset consists of approximately 12,000 daily observations.

Two supervised learning algorithms are used:

K-Nearest Neighbors (KNN) for rainfall classification

Multiple Linear Regression for temperature prediction

1.2 The Algorithm: K-Nearest Neighbors (KNN)

KNN is a supervised, instance-based learning algorithm that classifies data points based on the
majority class among their nearest neighbors.
It is effective for problems where decision boundaries are non-linear and sufficient historical
data is available.

1.3 The Algorithm: Multiple Linear Regression

Multiple Linear Regression models the relationship between a dependent variable and multiple
independent variables.
It is used in this project to predict maximum temperature based on other weather attributes.

1.4 Similarity Metric

Distance and similarity metrics are used to measure how close data points are in a
multidimensional feature space.
Although Euclidean distance is used in implementation, cosine similarity is conceptually relevant
for understanding vector-based comparisons.

2. Implementation Details & Code
2.1 Importing Libraries

The project is implemented in Python using the following libraries:

Pandas for data manipulation

NumPy for numerical computation (used internally)

Scikit-learn for machine learning models

OS module for file and path handling

2.2 Loading the Dataset

The dataset is stored in CSV format and loaded using Pandas.
Each row represents a single day, and each column represents a weather attribute such as
temperature or precipitation.

2.3 Matrix Creation (Data Preprocessing)

Data preprocessing ensures the quality of input data:

Rows with missing values are removed

Precipitation values are converted into a binary rainfall label

Data is split into training and testing sets

2.4 Model Training (KNN)

The KNN model is trained to classify whether rainfall occurs on a given day.

Key steps include:

Selecting temperature-related features

Applying feature standardization

Training the model using nearest-neighbor distance calculations

2.5 Model Training (Multiple Linear Regression)

The Multiple Linear Regression model is trained to predict maximum daily temperature.

Key steps include:

Selecting relevant temperature and precipitation features

Learning linear relationships between variables

Estimating regression coefficients for interpretation

2.6 System Execution

The system executes the following steps sequentially:

Data loading

Data preprocessing

Model training

Prediction

This modular structure ensures reproducibility and clarity.

3. Output

The output and evaluation metrics are intentionally excluded as per project requirements.

4. Results and Findings

The models demonstrate the effectiveness of machine learning techniques in weather prediction.

KNN captures rainfall-related patterns using historical similarity

Linear Regression effectively models temperature relationships

5. Conclusion

This project demonstrates how supervised machine learning algorithms can be applied to real-world
weather data.

By combining classification (KNN) and regression (Linear Regression), the system provides a
comprehensive framework for analyzing climatic trends.

Future improvements may include advanced models, additional features, and time-series forecasting
methods.

Project Structure
Weather-Prediction-Model/
│
├── dataset
├── knn_model.py
├── linear_regression_model.py
└── README.md
