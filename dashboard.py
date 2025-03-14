import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Menyiapkan URL dataset
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

# Membaca data untuk setiap stasiun dan menyimpannya dalam dictionary
dataframes = {}
for station, url in urls.items():
    dataframes[station] = pd.read_csv(url)

# Judul Dashboard
st.title('Dashboard Kualitas Udara')

# Sidebar untuk memilih stasiun
selected_station = st.sidebar.selectbox('Pilih Stasiun', list(dataframes.keys()))

# Menampilkan data statisi deskriptif
st.header(f'Statistik Deskriptif - {selected_station}')
st.write(dataframes[selected_station].describe())

# Visualisasi distribusi PM2.5
st.header(f'Distribusi PM2.5 - {selected_station}')
plt.figure(figsize=(10, 6))
sns.histplot(dataframes[selected_station]['PM2.5'], bins=30, kde=True)
plt.title(f'Distribusi PM2.5 di stasiun {selected_station}')
plt.xlabel('PM2.5')
plt.ylabel('Frequency')
st.pyplot(plt)

# Visualisasi tren PM2.5 dari waktu ke waktu
st.header(f'Tren PM2.5 dari waktu ke waktu - {selected_station}')
combined_data = pd.concat(dataframes.values(), keys=dataframes.keys()).reset_index()
combined_data['datetime'] = pd.to_datetime(combined_data[['year', 'month', 'day', 'hour']])
plt.figure(figsize=(12, 6))
sns.lineplot(data=combined_data[combined_data['level_0'] == selected_station], x='datetime', y='PM2.5')
plt.title(f'Tren PM2.5 dari waktu ke waktu di stasiun {selected_station}')
plt.xlabel('Waktu')
plt.ylabel('PM2.5')
st.pyplot(plt)

# Visualisasi heatmap korelasi antar variabel
st.header(f'Matriks Korelasi - {selected_station}')
correlation_matrix = dataframes[selected_station][['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title(f'Matriks Korelasi Antar Variabel Kualitas Udara - {selected_station}')
st.pyplot(plt)
