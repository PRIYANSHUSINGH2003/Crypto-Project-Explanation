import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

def train_model(data, variable1, variable2):
    # Prepare feature columns
    feature_cols = [
        f'Days_Since_High_Last_{variable1}_Days',
        f'%_Diff_From_High_Last_{variable1}_Days',
        f'Days_Since_Low_Last_{variable1}_Days',
        f'%_Diff_From_Low_Last_{variable1}_Days'
    ]

    # Target variables
    target_high = f'%_Diff_From_High_Next_{variable2}_Days'
    target_low = f'%_Diff_From_Low_Next_{variable2}_Days'

    # Drop rows with NaN values
    data = data.dropna(subset=feature_cols + [target_high, target_low])

    X = data[feature_cols]
    y_high = data[target_high]
    y_low = data[target_low]

    # Split the data
    X_train, X_test, y_train_high, y_test_high = train_test_split(X, y_high, test_size=0.2, random_state=42)
    X_train, X_test, y_train_low, y_test_low = train_test_split(X, y_low, test_size=0.2, random_state=42)

    # Scale the data
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Train models
    model_high = RandomForestRegressor()
    model_high.fit(X_train, y_train_high)

    model_low = RandomForestRegressor()
    model_low.fit(X_train, y_train_low)

    # Evaluate accuracy
    high_accuracy = model_high.score(X_test, y_test_high)
    low_accuracy = model_low.score(X_test, y_test_low)

    return model_high, model_low, high_accuracy, low_accuracy, scaler

def predict_outcomes(model_high, model_low, scaler, input_data):
    # Convert input data to DataFrame with correct feature names
    input_df = pd.DataFrame([input_data], columns=[
        'Days_Since_High_Last_7_Days',
        '%_Diff_From_High_Last_7_Days',
        'Days_Since_Low_Last_7_Days',
        '%_Diff_From_Low_Last_7_Days'
    ])
    input_scaled = scaler.transform(input_df)
    high_pred = model_high.predict(input_scaled)[0]
    low_pred = model_low.predict(input_scaled)[0]
    return high_pred, low_pred
