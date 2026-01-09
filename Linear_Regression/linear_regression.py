import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load dataset
# Get the path of the folder where THIS script is saved
base_dir = os.path.dirname(os.path.abspath(__file__))
# Build the path to the dataset relative to the script location
csv_path = os.path.join(base_dir, '..', 'dataset', 'Bangalore_1990_2022_BangaloreCity.csv')
# Load the file
df = pd.read_csv(csv_path)
# This removes any row where tavg, tmin, prcp, or tmax is missing
df = df.dropna(subset=['tavg', 'tmin', 'tmax', 'prcp'])

# 2. Features (Multiple Independent Variables) and Target
X = df[['tavg', 'tmin', 'prcp']]
y = df['tmax'] # Target continuous variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Multiple Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Evaluate Performance
y_pred = model.predict(X_test)
print(f"R-squared Score: {r2_score(y_test, y_pred):.4f}")
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.4f}")

# Show individual influence of each variable (for your report)
for col, coef in zip(X.columns, model.coef_):
    print(f"Influence of {col} on Max Temp: {coef:.4f}")
