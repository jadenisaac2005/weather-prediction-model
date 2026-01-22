<div align="center">

# 🌦️ Weather Prediction Model  
### 📊 Using K-Nearest Neighbors (KNN) & Multiple Linear Regression  

📍 Bangalore Weather Data (1990–2022)  
🧠 Machine Learning • Classification & Regression

</div>

---

## 📖 Overview
This project applies **machine learning techniques** to historical weather data to predict
rainfall occurrence and temperature trends.  
The dataset contains approximately **12,000 daily weather records** collected from Bangalore city.

---

## 🎯 Objectives
- 🌧️ Classify rainfall occurrence using **KNN**
- 🌡️ Predict maximum temperature using **Linear Regression**
- 📊 Analyze historical climate patterns

---

## 📊 Dataset Information
- **Location:** Bangalore City  
- **Time Period:** 1990 – 2022  
- **Records:** ~12,000  
- **Format:** CSV  

### Features Used
- `tavg` – Average temperature  
- `tmin` – Minimum temperature  
- `tmax` – Maximum temperature  
- `prcp` – Precipitation  

---

## 🧠 Algorithms Used

### 🔹 K-Nearest Neighbors (KNN)
- Supervised classification algorithm  
- Classifies rainfall based on similarity to historical data  
- Distance-based and non-parametric  

**Why KNN?**
- Handles non-linear patterns well  
- Simple and intuitive  
- Effective with large datasets  

---

### 🔹 Multiple Linear Regression
- Supervised regression algorithm  
- Predicts continuous temperature values  
- Models linear relationships between variables  

**Why Linear Regression?**
- Easy to interpret  
- Computationally efficient  
- Provides insight into feature influence  

---

## 🛠️ Tools & Technologies
- **Python 🐍**
- **Pandas** – Data manipulation  
- **NumPy** – Numerical computation  
- **Scikit-learn** – Machine learning models  
- **OS Module** – File and path handling  

---

## 🧹 Data Preprocessing
- Removed rows with missing values  
- Converted precipitation into binary rainfall labels  
- Applied feature scaling for KNN  
- Split data into training and testing sets (80/20)

---

## 🤖 Model Training

### 🌧️ Rainfall Prediction (KNN)
- Uses temperature features  
- Applies standardization  
- Classifies rainfall occurrence  

---

### 🌡️ Temperature Prediction (Linear Regression)
- Uses temperature and precipitation features  
- Learns linear relationships  
- Predicts maximum daily temperature  

---

## ⚙️ System Workflow
1️⃣ Load dataset  
2️⃣ Preprocess data  
3️⃣ Train KNN and Linear Regression models  
4️⃣ Perform predictions  

---

## 📤 Output
🚫 Output and evaluation metrics are intentionally excluded as per project requirements.

---

## 📈 Results & Observations
- KNN effectively captures rainfall patterns  
- Linear Regression models temperature trends accurately  

---

## 🏁 Conclusion
This project demonstrates how **machine learning models** can be applied to real-world weather
data for both **classification and regression tasks**.

The combined approach provides a comprehensive framework for climate analysis.

---

## 🗂️ Project Structure

Weather-Prediction-Model/
│
├── dataset/
│   └── Bangalore_1990_2022_BangaloreCity.csv
├── knn_model.py
├── linear_regression_model.py
└── README.md

<div align="center">

</div>
