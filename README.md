# Car Sales Dashboard

This is an interactive data visualization web application that explores a dataset of car sales advertisements. It allows users to inspect vehicle prices, mileage, model years, and types through histograms and scatter plots.

The dashboard was built using:

- `pandas` for data manipulation
- `plotly.express` for data visualizations
- `streamlit` for building the web interface

## Features

- 📊 Histogram of vehicle prices
- 🚗 Scatter plot of odometer readings vs price
- ✅ Interactive checkbox to filter prices under $20,000

## Setup Instructions

To run this dashboard locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
2. **Create and activate a virtual environment**:
   ```bash
   conda create -n car_sales_env python=3.11
   conda activate car_sales_env
3. **Install required packages**:
   ```bash
   pip install pandas streamlit plotly.express altair
4. **Start Streamlit app**:
   ```bash
   streamlit run app.py
5. **Open the link provided by Streamlit (usually http://localhost:8501) in your browser.** 

## Dataset

The dataset used in this project is vehicles_us.csv, which contains information on car sales listings, such as price, model year, vehicle type, and mileage.

## Streamlit app URL

https://sprint4-cars.onrender.com/