import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for visualizations
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# Define URLs for each station's data
urls = {
    "Aotizhongxin": "https://raw.githubusercontent.com/ulfasyabania/Proyek-Analisis-Data/refs/heads/main/PRSA_Data_Aotizhongxin_20130301-20170228.csv",
    "Changping": "https://raw.githubusercontent.com/ulfasyabania/Proyek-Analisis-Data/refs/heads/main/PRSA_Data_Changping_20130301-20170228.csv",
    "Dingling": "https://raw.githubusercontent.com/ulfasyabania/Proyek-Analisis-Data/refs/heads/main/PRSA_Data_Dingling_20130301-20170228.csv",
    "Dongsi": "https://raw.githubusercontent.com/ulfasyabania/Proyek-Analisis-Data/refs/heads/main/PRSA_Data_Dongsi_20130301-20170228.csv",
    "Guanyuan": "https://raw.githubusercontent.com/ulfasyabania/Proyek-Analisis-Data/refs/heads/main/PRSA_Data_Guanyuan_20130301-20170228.csv",
    "Gucheng": "https://raw.githubusercontent.com/ulfasyabania/Proyek-Analisis-Data/refs/heads/main/PRSA_Data_Gucheng_20130301-20170228.csv",
    "Huairou": "https://raw.githubusercontent.com/ulfasyabania/Proyek-Analisis-Data/refs/heads/main/PRSA_Data_Huairou_20130301-20170228.csv",
    "Nongzhanguan": "https://raw.githubusercontent.com/ulfasyabania/Proyek-Analisis-Data/refs/heads/main/PRSA_Data_Nongzhanguan_20130301-20170228.csv",
    "Shunyi": "https://raw.githubusercontent.com/ulfasyabania/Proyek-Analisis-Data/refs/heads/main/PRSA_Data_Shunyi_20130301-20170228.csv",
    "Tiantan": "https://raw.githubusercontent.com/ulfasyabania/Proyek-Analisis-Data/refs/heads/main/PRSA_Data_Tiantan_20130301-20170228.csv",
    "Wanliu": "https://raw.githubusercontent.com/ulfasyabania/Proyek-Analisis-Data/refs/heads/main/PRSA_Data_Wanliu_20130301-20170228.csv",
    "Wanshouxigong": "https://raw.githubusercontent.com/ulfasyabania/Proyek-Analisis-Data/refs/heads/main/PRSA_Data_Wanshouxigong_20130301-20170228.csv"
}

# Read data for each station and store in a dictionary
dataframes = {}
for station, url in urls.items():
    dataframes[station] = pd.read_csv(url)

# Sidebar for selecting station
station = st.sidebar.selectbox("Select Station", list(dataframes.keys()))

# Display selected station data
st.title(f"Air Quality Data Analysis for {station}")
st.write(dataframes[station].head())

# Plotting functions
def plot_distribution(df, station):
    plt.figure()
    sns.histplot(df["PM2.5"].dropna(), kde=True)
    plt.title(f"Distribution of PM2.5 in {station}")
    plt.xlabel("PM2.5")
    plt.ylabel("Frequency")
    st.pyplot(plt)

def plot_trend(df, station):
    plt.figure()
    plt.plot(df["year"], df["PM2.5"], marker='o')
    plt.title(f"Trend of PM2.5 over Time in {station}")
    plt.xlabel("Year")
    plt.ylabel("PM2.5")
    plt.grid(True)
    st.pyplot(plt)

def plot_correlation(df, station):
    plt.figure()
    corr = df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title(f"Correlation Heatmap for {station}")
    st.pyplot(plt)

# Display plots
if st.sidebar.checkbox("Show Distribution Plot"):
    plot_distribution(dataframes[station], station)

if st.sidebar.checkbox("Show Trend Plot"):
    plot_trend(dataframes[station], station)

if st.sidebar.checkbox("Show Correlation Heatmap"):
    plot_correlation(dataframes[station], station)
