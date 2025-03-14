# Proyek-Analisis-Data

# Dashboard Kualitas Udara

Dashboard ini bertujuan untuk memberikan visualisasi dan analisis data kualitas udara dari berbagai stasiun pemantauan di Beijing. Data yang digunakan mencakup parameter-parameter kualitas udara seperti PM2.5, PM10, SO2, NO2, CO, dan O3.

## Fitur

- Menampilkan statistik deskriptif untuk setiap stasiun pemantauan.
- Visualisasi distribusi PM2.5 di setiap stasiun pemantauan.
- Visualisasi tren PM2.5 dari waktu ke waktu.
- Visualisasi matriks korelasi antar variabel kualitas udara.
- Sidebar interaktif untuk memilih stasiun pemantauan.

## Prasyarat

Pastikan telah menginstal library berikut sebelum menjalankan dashboard:
- `pandas`
- `matplotlib`
- `seaborn`
- `statsmodels`
- `scikit-learn`
- `streamlit`

Anda dapat menginstalnya menggunakan pip:
```bash
pip install pandas matplotlib seaborn statsmodels scikit-learn streamlit

Menjalankan Dashboard Streamlit:
```bash
streamlit run dashboard.py

Buka browser dan akses URL berikut:
```bash
