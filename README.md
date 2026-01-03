🌦️ Weather Trend Predictor

Real-time Data Analysis with Python & NumPy

📖 Overview

The goal of this project is to demonstrate how to bridge the gap between real-world data acquisition and mathematical modeling. Instead of using complex Machine Learning libraries, 
this project uses Vectorized NumPy operations to calculate the rate of temperature change (slope) and predict the weather for the upcoming hour.

🚀 Key Features

Live Data Fetching: Connects to the Open-Meteo API to get real-time meteorological data.

Automated Forecasting: Uses a linear trend model to predict the next hour's temperature.

NumPy Optimization: Employs np.diff(), np.mean(), and slicing for high-performance calculations.

Clean Formatting: Utilizes Python f-strings with sign flags (e.g., +0.50°C) for clear trend reporting.

🛠️ Technical Stack

Language: Python 3.x

Libraries: * NumPy: Data manipulation and statistical calculations.

Requests: Handling HTTP API calls.

📈 How the Prediction Works

The script follows a 3-step mathematical process:
Extraction: Pulls the last 3 hours of temperature data into a NumPy array.
Difference Calculation: Uses $np.diff(temps)$ to find the change between each hour ($\Delta t$).
Linear Projection: Calculates the average change ($\bar{\Delta}$) and adds it to the current temperature ($T_{now}$).

$$T_{predicted} = T_{now} + \frac{1}{n} \sum_{i=1}^{n} \Delta t_i$$

📂 Installation & Usage

1. Clone the Repository:
   ```bash
   git clone https://github.com/ayush-130904/weather_prediction.git
   cd weather__prediction

2. Install Dependencies:
   ```bash
   pip install numpy requests

3. Run the Script:
   ```bash
   python weather_prediction.py


📊 Sample Output

Recent Temps (Last 3h): [12.5, 13.2, 14.1]
Average Trend: +0.80°C per hour
Current Temperature: 14.1°C
Predicted Temperature (Next Hour): 14.90°C

📝 Future Improvements

Add Matplotlib integration to visualize the trend line.

Incorporate Humidity and Pressure into the prediction logic.

Store historical predictions in a local SQL database to track accuracy.



