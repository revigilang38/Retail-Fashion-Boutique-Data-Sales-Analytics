# Retail Fashion Boutique Data Sales Analytics 2025

Proyek ini bertujuan untuk membangun model *machine learning* yang mampu memprediksi kemungkinan suatu produk fashion akan dikembalikan (retur) berdasarkan berbagai atribut penjualan. Dengan memprediksi tingkat retur, bisnis *fashion boutique* dapat mengantisipasi kerugian, mengelola stok dengan lebih efisien, dan meningkatkan kepuasan pelanggan.

## **Objective**

Tujuan utama dari proyek ini adalah:

- **Memprediksi Retur Produk:** Mengidentifikasi produk yang memiliki risiko tinggi untuk diretur sebelum terjadi.
- **Analisis Penjualan:** Memahami tren penjualan berdasarkan kategori, merek, musim, dan harga.
- **Identifikasi Faktor Kunci:** Menganalisis faktor-faktor yang paling memengaruhi keputusan pelanggan untuk mengembalikan produk.
- **Rekomendasi Strategi:** Memberikan saran strategis untuk diskon dan pengelolaan stok agar lebih efektif.

## **Dataset**

Dataset yang digunakan berjudul **Retail Fashion Boutique Data Sales Analytics 2025** yang bersumber dari Kaggle. Dataset ini berisi catatan transaksi penjualan produk fashion, termasuk informasi seperti kategori produk, merek, musim, ukuran, warna, harga, diskon, stok, rating pelanggan, dan status retur.

## **Metodologi**

Proyek ini dikembangkan menggunakan metodologi *Data Science* dengan tahapan berikut:

1. **Analisis Data Eksplorasi (EDA):** Menganalisis distribusi data dan visualisasi untuk mendapatkan wawasan awal tentang pola penjualan dan faktor-faktor yang relevan.
2. **Pra-pemrosesan Data (Data Preprocessing):** Membersihkan data yang hilang, mengatasi *outlier*, dan melakukan *feature engineering* serta *encoding* pada data kategorikal.
3. **Pemodelan:** Menggunakan berbagai algoritma *machine learning* untuk masalah klasifikasi, seperti **K-Nearest Neighbors (KNN)**, **Decision Tree**, **Random Forest**, dan **Gradient Boosting**.
4. **Evaluasi Model:** Membandingkan performa model menggunakan metrik seperti **ROC-AUC**, **Precision**, dan **Recall** untuk menemukan model terbaik.
5. **Deployment:** Menerapkan model yang sudah dilatih ke dalam sebuah aplikasi web interaktif menggunakan **Streamlit**, memungkinkan pengguna untuk melakukan prediksi secara langsung.

## **Deployment**

Aplikasi ini sudah di-*deploy* dan dapat diakses secara publik melalui platform Hugging Face Spaces.
[**Link Aplikasi Streamlit**](https://huggingface.co/spaces/revigilang/fashion_boutique)
