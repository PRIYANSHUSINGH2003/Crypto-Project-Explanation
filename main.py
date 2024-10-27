from data_retrieval import fetch_crypto_data
from metrics_calculation import calculate_metrics
from ml_model import train_model, predict_outcomes
import pandas as pd

if __name__ == "__main__":
    # Fetch and prepare the data
    crypto_pair = "bitcoin/usd"
    start_date = "2024-01-01"
    data = fetch_crypto_data(crypto_pair, start_date)
    print(data)  # To see the full response from the API

    # Calculate metrics
    variable1 = 7
    variable2 = 5
    data_with_metrics = calculate_metrics(data, variable1, variable2)

    # Save to Excel
    excel_file = "crypto_historical_data.xlsx"
    with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
        data_with_metrics.to_excel(writer, sheet_name='Historical Data', index=False)

    print(f"Data saved to {excel_file}")
    # Print the entire DataFrame
    print(data_with_metrics)
    # Train machine learning model
    model_high, model_low, high_accuracy, low_accuracy, scaler = train_model(data_with_metrics, variable1, variable2)
    print(f"High Accuracy: {high_accuracy}, Low Accuracy: {low_accuracy}")

    # Predict future outcomes for sample input
    input_data = [10, -5, 20, -3]  # Example input values for features
    high_pred, low_pred = predict_outcomes(model_high, model_low, scaler, input_data)
    print(f"High Prediction: {high_pred}, Low Prediction: {low_pred}")
