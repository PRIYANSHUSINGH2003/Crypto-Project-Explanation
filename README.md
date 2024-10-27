# Cryptocurrency Data Analysis and Prediction

This project focuses on retrieving historical cryptocurrency data, calculating key financial metrics, and training a machine learning model to predict future price trends. The analysis uses Bitcoin data from the CoinGecko API, performs metric calculations, and applies a Random Forest Regressor for predictions.

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Retrieval](#data-retrieval)
- [Metrics Calculation](#metrics-calculation)
- [Machine Learning Model](#machine-learning-model)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The purpose of this project is to analyze historical cryptocurrency prices and develop a machine learning model that can predict future price highs and lows. The project utilizes Python, several data processing libraries, and machine learning techniques to provide insights into price trends.

## Project Structure
```
project/
│
├── data_retrieval.py         # Script to fetch historical data from the API
├── metrics_calculation.py    # Script to calculate financial metrics from historical data
├── ml_model.py               # Script to train and predict with the machine learning model
├── main.py                   # Main script to execute the entire workflow
├── requirements.txt          # List of dependencies
└── README.md                 # Project documentation
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/crypto-prediction.git
   ```
2. Change directory into the project folder:
   ```bash
   cd crypto-prediction
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the `main.py` script to fetch data, calculate metrics, and train the machine learning model:
   ```bash
   python main.py
   ```
2. The program will fetch cryptocurrency data, calculate metrics, save the data to an Excel file, train a model, and display prediction results.

## Data Retrieval
The `data_retrieval.py` script fetches historical cryptocurrency data using the CoinGecko API. It extracts essential features like Date, Open, High, Low, and Close prices for the specified cryptocurrency pair and time range.

## Metrics Calculation
The `metrics_calculation.py` script calculates various financial metrics, such as:
- High and Low prices over a rolling window of days.
- Percentage differences from the rolling Highs and Lows.
- Days since the last High and Low values.

These metrics help in understanding historical trends and serve as features for model training.

## Machine Learning Model
The `ml_model.py` script uses a `RandomForestRegressor` to predict future price highs and lows. It prepares feature columns, scales the data using `StandardScaler`, and trains two models to predict future high and low price differences.

### Model Features
- Days since the last High and Low values.
- Percentage difference from the last High and Low values.

## Results
The script displays the following results:
- Accuracy scores for predicting High and Low prices.
- Predictions for future high and low price changes based on sample input data.

## Contributing
Feel free to submit issues, fork the repository, or contribute code. Contributions are welcome to improve this project and extend its functionality.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
