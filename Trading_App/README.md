# Stock Price Prediction App

This project contains a **Streamlit** web application for predicting stock price percentage changes using machine learning models. The app uses various stock features, including technical indicators like moving averages and RSI, to forecast the next day's adjusted close price.

## Features
- Input daily stock data such as `High`, `Low`, `Previous Close`, and `Volume`.
- Calculate features like `RSI`, `SMA`, `EMA`, and Bollinger Bands.
- Predict today's stock percentage changes using a pre-trained model based on Previous Day's features.

## Files in the Repository
- `app.py`: The main Streamlit application script.
- `Trading_model.pkl`: The pre-trained model for predictions.
- `Trading_scaler.pkl`: Scaler used for data preprocessing.
- `requirements.txt`: List of required Python packages.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/NikitaEmberi/MyLearning
   ```
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app
   ```bash
   streamlit run Trading_App/app.py
   ```

[Know Today's Closing Stock Price](https://know-todays-closing-stock-price.streamlit.app/)


## Dependencies
- Python 3.8+
- Streamlit
- scikit-learn
- joblib
- pandas

