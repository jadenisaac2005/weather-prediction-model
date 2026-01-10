import os
import pandas as pd
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

# 1. Load  dataset
# Get the path of the folder where THIS script is saved
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, '..', 'dataset', 'Bangalore_1990_2022_BangaloreCity.csv')
df = pd.read_csv(csv_path)

# 2. Preprocessing: Handle missing values and create categorical label
df = df.dropna(subset=['tavg', 'tmin', 'tmax', 'prcp'])
df['is_raining'] = (df['prcp'] > 0).astype(int) # 1 for Rain, 0 for No Rain

# 3. Features (X) and Target (y)
X = df[['tavg', 'tmin', 'tmax']]
y = df['is_raining']

# 4. Standardize (Crucial for k-NN distance calculation)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 5. Run k-NN
knn = KNeighborsClassifier(n_neighbors=28) # K=5 is standard
knn.fit(X_train, y_train)

# Output Results
y_pred = knn.predict(X_test)
print(f"k-NN Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))
