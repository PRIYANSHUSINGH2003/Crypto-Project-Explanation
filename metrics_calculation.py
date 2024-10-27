import pandas as pd

def calculate_metrics(data, variable1, variable2):
    # Historical High and Low calculations
    data[f'High_Last_{variable1}_Days'] = data['High'].rolling(window=variable1).max()
    data[f'Days_Since_High_Last_{variable1}_Days'] = (data['Date'] - data['Date'].shift(variable1)).dt.days
    data[f'%_Diff_From_High_Last_{variable1}_Days'] = ((data['Close'] - data[f'High_Last_{variable1}_Days']) / data[f'High_Last_{variable1}_Days']) * 100

    data[f'Low_Last_{variable1}_Days'] = data['Low'].rolling(window=variable1).min()
    data[f'Days_Since_Low_Last_{variable1}_Days'] = (data['Date'] - data['Date'].shift(variable1)).dt.days
    data[f'%_Diff_From_Low_Last_{variable1}_Days'] = ((data['Close'] - data[f'Low_Last_{variable1}_Days']) / data[f'Low_Last_{variable1}_Days']) * 100

    # Future High and Low calculations
    data[f'High_Next_{variable2}_Days'] = data['High'].shift(-variable2).rolling(window=variable2).max()
    data[f'%_Diff_From_High_Next_{variable2}_Days'] = ((data[f'High_Next_{variable2}_Days'] - data['Close']) / data['Close']) * 100

    data[f'Low_Next_{variable2}_Days'] = data['Low'].shift(-variable2).rolling(window=variable2).min()
    data[f'%_Diff_From_Low_Next_{variable2}_Days'] = ((data[f'Low_Next_{variable2}_Days'] - data['Close']) / data['Close']) * 100

    # Fill NaN values with 0 or forward fill
    data.fillna(0, inplace=True)

    return data

