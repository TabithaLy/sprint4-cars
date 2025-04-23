import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('vehicles_us.csv')

# Header
st.header("Car Sales Dashboard")

# Histogram
fig_hist = px.histogram(df, x='price', nbins=50, title='Distribution of Vehicle Prices')
st.plotly_chart(fig_hist)

# Scatter Plot
fig_scatter = px.scatter(df, x='odometer', y='price', color='type', title='Price vs. Odometer by Vehicle Type')
st.plotly_chart(fig_scatter)

# Checkbox - Filtered histogram
if st.checkbox('Show only vehicles under $20,000'):
    filtered_df = df[df['price'] < 20000]
    fig_filtered = px.histogram(filtered_df, x='price', nbins=50, title='Filtered Vehicle Price Distribution (< $20k)')
    st.plotly_chart(fig_filtered)
