import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
import xgboost as xgb

df = pd.read_csv("marksVsRank.csv", index_col=0)
X = df[['Marks', 'Year']]
y = df['Rank']
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)

model = xgb.XGBRegressor(
                    objective="reg:squarederror", 
                    n_estimators=500, 
                    learning_rate=0.1, 
                    max_depth=5)

history = model.fit(
    X_train_scaled, y_train, 
    eval_set=[(X_train_scaled, y_train), (X_val_scaled, y_val)], 
    eval_metric="mae", verbose=True
)

# Predictions
y_pred = model.predict(X_val_scaled)

# Performance Evaluation
mae = mean_absolute_error(y_val, y_pred)
rmse = np.sqrt(mean_squared_error(y_val, y_pred))
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Root Mean Squared Error (RMSE): {rmse}")

#Testing
test_sample_1 = np.array([[680, 2023]])
test_sample_1_scaled = scaler.transform(test_sample_1)
predicted_rank_1 = model.predict(test_sample_1_scaled)
print(f"Predicted Rank for 680 marks in 2023: {int(predicted_rank_1[0])}")

test_sample_2 = np.array([[450, 2022]])
test_sample_2_scaled = scaler.transform(test_sample_2)
predicted_rank_2 = model.predict(test_sample_2_scaled)
print(f"Predicted Rank for 450 marks in 2022: {int(predicted_rank_2[0])}")