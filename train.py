import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.metrics import accuracy_score, confusion_matrix, mean_absolute_error, r2_score
import joblib
import os

# Set seed for reproducibility
np.random.seed(42)

def generate_data(n_samples=250):
    # Features
    temp = np.random.uniform(5, 35, n_samples)
    rain_prob = np.random.uniform(0, 100, n_samples)
    social_reach = np.random.uniform(100, 2000, n_samples)
    is_weekend = np.random.randint(0, 2, n_samples)
    
    # Logic for Classification (Status)
    # Success if temp > 15 and rain_prob < 40, with some noise
    status_noise = np.random.uniform(0, 1, n_samples)
    status = ((temp > 15) & (rain_prob < 40)).astype(int)
    # Add noise: flip status for 5% of samples
    flip_indices = np.random.choice(n_samples, int(n_samples * 0.05), replace=False)
    status[flip_indices] = 1 - status[flip_indices]
    
    # Logic for Regression (Attendance)
    # Attendance depends on reach, weekend, and weather
    # Base 50 + 0.2*reach + 100*weekend + 2*temp - 0.5*rain_prob
    attendance = 50 + (0.2 * social_reach) + (100 * is_weekend) + (2 * temp) - (0.5 * rain_prob)
    # If status is 0 (Cancelled), attendance should be 0 or very low (let's say 0 for realism)
    attendance = np.where(status == 1, attendance, 0)
    # Add some noise to attendance for active events
    attendance = np.where(status == 1, attendance + np.random.normal(0, 20, n_samples), 0)
    attendance = np.maximum(0, attendance).astype(int)
    
    df = pd.DataFrame({
        'temp': temp,
        'rain_prob': rain_prob,
        'social_reach': social_reach,
        'is_weekend': is_weekend,
        'status': status,
        'attendance': attendance
    })
    return df

def train_models():
    print("Generating synthetic data...")
    df = generate_data(300)
    df.to_csv('smartevent_data.csv', index=False)
    
    X = df[['temp', 'rain_prob', 'social_reach', 'is_weekend']]
    y_cls = df['status']
    y_reg = df['attendance']
    
    # Split data
    X_train, X_test, y_cls_train, y_cls_test, y_reg_train, y_reg_test = train_test_split(
        X, y_cls, y_reg, test_size=0.2, random_state=42
    )
    
    # 1. Classification Model
    print("Training Decision Tree Classifier...")
    clf = DecisionTreeClassifier(max_depth=5, random_state=42)
    clf.fit(X_train, y_cls_train)
    
    y_cls_pred = clf.predict(X_test)
    acc = accuracy_score(y_cls_test, y_cls_pred)
    cm = confusion_matrix(y_cls_test, y_cls_pred)
    
    print(f"Classification Accuracy: {acc:.2f}")
    print("Confusion Matrix:")
    print(cm)
    
    # 2. Regression Model
    print("\nTraining Decision Tree Regressor...")
    reg = DecisionTreeRegressor(max_depth=5, random_state=42)
    reg.fit(X_train, y_reg_train)
    
    y_reg_pred = reg.predict(X_test)
    mae = mean_absolute_error(y_reg_test, y_reg_pred)
    r2 = r2_score(y_reg_test, y_reg_pred)
    
    print(f"Regression MAE: {mae:.2f}")
    print(f"Regression R2 Score: {r2:.2f}")
    
    # Save models
    os.makedirs('models', exist_ok=True)
    joblib.dump(clf, 'models/classifier.joblib')
    joblib.dump(reg, 'models/regressor.joblib')
    print("\nModels saved to 'models/' directory.")

if __name__ == "__main__":
    train_models()
