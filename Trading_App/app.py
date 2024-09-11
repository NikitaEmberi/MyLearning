import streamlit as st
import pandas as pd
import joblib  # Correct import for joblib


def load_model():
  # Load the pre-trained model and scaler from disk
  model = joblib.load('Trading_App/Trading_model.pkl')  # Adjust path if needed
  scaler = joblib.load('Trading_App/Trading_scaler.pkl')  # Adjust path if needed
  return model, scaler

# Load model and scaler
model, scaler = load_model()

def calculate_features(high, low, adj_close, prev_close, volume):
  # Calculated Features
  high_low_spread = high - low
  
  # Handle division by zero for Close-Prev Close Ratio
  if prev_close != 0:
      close_prev_close_ratio = adj_close / prev_close
  else:
      st.warning("Previous Close Price cannot be zero for ratio calculation.")
      close_prev_close_ratio = 1  # Default value or handle as you see fit
  
  # Ask for moving averages if not provided (or user may provide them)
  sma_5 = st.number_input('5-Day Simple Moving Average (SMA)', value=adj_close)  # Placeholder default value
  sma_10 = st.number_input('10-Day Simple Moving Average (SMA)', value=adj_close)
  
  ema_5 = st.number_input('5-Day Exponential Moving Average (EMA)', value=adj_close)
  ema_10 = st.number_input('10-Day Exponential Moving Average (EMA)', value=adj_close)
  
  # RSI Calculation: We need some historical data, so let the user input it manually
  rsi = st.number_input('Relative Strength Index (RSI)', value=50.0)
  
  # Bollinger Bands
  bb_upper = st.number_input('Bollinger Band Upper', value=adj_close + 10)
  bb_lower = st.number_input('Bollinger Band Lower', value=adj_close - 10)
  
  # Volume Price Trend (VPT) Calculation
  if prev_close != 0:
      vpt = (volume * (adj_close - prev_close) / prev_close)
  else:
      st.warning("Previous Close Price cannot be zero for VPT calculation.")
      vpt = 0  # Default value or handle as you see fit

  # Return all features
  return [high_low_spread, close_prev_close_ratio, sma_5, sma_10, ema_5, ema_10, rsi, bb_upper, bb_lower, vpt]


# Function to predict the next day's percentage change
def predict_next_day(features):
    # Convert input features to DataFrame for prediction
  features_df = pd.DataFrame([features], columns=[
      'High-Low Spread', 'Close-Prev Close Ratio', 'SMA_5', 'SMA_10', 
      'EMA_5', 'EMA_10', 'RSI', 'BB_upper', 'BB_lower', 'VPT'
  ])
  
  # Scale the features
  features_scaled = scaler.transform(features_df)
  
  # Predict the next day's percentage change
  prediction = model.predict(features_scaled)
  return prediction[0]

# Streamlit App Layout
st.title('Stock Price Prediction App')

st.write("Enter the stock features below to predict the next day's Adjusted Close price.")

# Input Fields for Basic Features
high = st.number_input('High Price of previous Day', min_value=0.0, max_value=10000.0, step=0.01)
low = st.number_input('Low Price of Previous Day', min_value=0.0, max_value=10000.0, step=0.01)
adj_close = st.number_input('Adjusted Close Price of previous Day', min_value=0.0, max_value=10000.0, step=0.01)
prev_close = st.number_input('Previous Close Price', min_value=0.0, max_value=10000.0, step=0.01)
volume = st.number_input('Volume of Previous Day', min_value=0, max_value=10000000000000, step=1)


# Calculate or ask for additional features
features = calculate_features(high, low, adj_close, prev_close, volume)

# Predict Button
if st.button('Predict Next Day Percentage Change'):
  predicted_percentage_change = predict_next_day(features)
  st.write(f"The predicted percentage change for today is: {predicted_percentage_change:.2f}%")
