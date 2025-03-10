import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

# Mengatur gaya visualisasi
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# Fungsi untuk memuat data hanya sekali
@st.cache_data
def load_data():
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
    
    dataframes = {}
    for station, url in urls.items():
        dataframes[station] = pd.read_csv(url)
    
    return dataframes

# Memuat data sekali di awal
dataframes = load_data()

# Sidebar untuk memilih stasiun
station = st.sidebar.selectbox("Pilih Stasiun", list(dataframes.keys()))

# Menampilkan data stasiun yang dipilih
st.title(f"Analisis Kualitas Udara untuk {station}")
st.write(dataframes[station].head())

# Fungsi plotting
def plot_distribution(df, station):
    plt.figure()
    sns.histplot(df["PM2.5"].dropna(), kde=True)
    plt.title(f"Distribusi PM2.5 di {station}")
    plt.xlabel("PM2.5")
    plt.ylabel("Frekuensi")
    st.pyplot(plt)

def plot_trend(df, station):
    plt.figure()
    df['year'] = pd.to_datetime(df['year'], format='%Y')
    plt.plot(df['year'], df['PM2.5'], marker='o')
    plt.title(f"Tren PM2.5 dari Waktu ke Waktu di {station}")
    plt.xlabel("Tahun")
    plt.ylabel("PM2.5")
    plt.grid(True)
    st.pyplot(plt)

def plot_correlation(df, station):
    plt.figure()
    corr = df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title(f"Heatmap Korelasi untuk {station}")
    st.pyplot(plt)

# Menampilkan plot jika dipilih di sidebar
if st.sidebar.checkbox("Tampilkan Plot Distribusi"):
    plot_distribution(dataframes[station], station)

if st.sidebar.checkbox("Tampilkan Plot Tren"):
    plot_trend(dataframes[station], station)

if st.sidebar.checkbox("Tampilkan Heatmap Korelasi"):
    plot_correlation(dataframes[station], station)

# Membuat HeatMap
def plot_heatmap(df, station):
    m = folium.Map(location=[39.93, 116.38], zoom_start=10)
    for i, row in df.iterrows():
        folium.Marker(location=[row['latitude'], row['longitude']], popup=row['station']).add_to(m)
    HeatMap(data=df[['latitude', 'longitude', 'value']].values.tolist()).add_to(m)
    st.write(m._repr_html_(), unsafe_allow_html=True)

if st.sidebar.checkbox("Tampilkan HeatMap"):
    plot_heatmap(dataframes[station], station)
