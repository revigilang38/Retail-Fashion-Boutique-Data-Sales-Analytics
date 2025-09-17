import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px


def run():
    st.title('Retail Fashion Boutique Data Sales Analytics 2025')
    st.subheader(
        'Halaman ini akan berisi terkait dengan EDA dari dataset Retail Fashion Boutique Data Sales Analytics 2025')
    st.markdown('---')
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRotZ9AvBpDiZWDoKopik5lx85mMs9CUPYQow&s',
             caption='Banner Fashion')

    # section dataframe
    st.markdown('## Dataframe')

    # showdateframe
    csv_path = r"D:\Hacktiv8\Milestone\p1-ftds045-rmt-m2-revigilang38\fashion_boutique_dataset.csv"
    data = pd.read_csv(csv_path)
    st.dataframe(data.head())

    # section visualization
    st.markdown('# Exploratory Data Analysis')

    # visual 1
    st.markdown("### 1) Distribusi Original Price")
    fig = plt.figure(figsize=(12, 6))
    sns.histplot(data=data, x='original_price')
    plt.title("Distribution of Original Price")
    plt.xlabel("Original Price ($)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    st.pyplot(fig)

    st.subheader("Insight")
    st.write("- Distribusi harga mayoritas di bawah $150")
    st.write("- Terdapat outlier untuk produk premium")

    # visual 2
    st.markdown("### 2) Distribusi Markdown Percentage")
    fig = plt.figure(figsize=(12, 6))
    sns.histplot(data=data, x='markdown_percentage')
    plt.title("Distribution of Markdown Percentage")
    plt.xlabel("Markdown")
    plt.ylabel("Frequency")
    plt.tight_layout()
    st.pyplot(fig)

    st.subheader("Insight")
    st.write("- Banyak produk tanpa diskon")
    st.write("- Sebagian kecil memiliki diskon besar hingga 60% kemungkinan untuk strategi pricing/marketing")

    # visual 3
    st.markdown("### 3) Current Price per Category")
    fig = plt.figure(figsize=(12, 6))
    sns.boxplot(data=data, x='category', y='current_price',
                order=data['category'].value_counts().index)
    plt.title("Current Price by Category")
    plt.xlabel("Category")
    plt.ylabel("Current Price ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig)
    st.subheader("Insight")
    st.write(
        "- Outerwear adalah kategori dengan harga paling tinggi secara rata-rata dan memiliki rentang harga yang paling lebar, ini menunjukkan produk-produk di kategori ini adalah yang paling premium.")
    st.write(
        "- Shoes menempati posisi kedua sebagai kategori termahal, menunjukkan produk sepatu secara umum memiliki harga di atas rata-rata")
    st.write(
        "- Produk Dresses memiliki variasi harga yang paling beragam, dari yang murah hingga yang mahal, mencerminkan adanya pilihan untuk berbagai segmen pasar.")
    st.write("- Bottoms dan Tops memiliki karakteristik harga yang serupa dan cenderung stabil di kisaran harga yang terjangkau")
    st.write(
        "- Accessories adalah kategori dengan harga paling terjangkau, menunjukkan produk di kategori ini cenderung memiliki harga yang lebih rendah dibandingkan kategori lainnya.")

    # visual 4
    st.markdown("### 4) Proporsi Penjualan per Kategori Produk")
    cat_counts = data['category'].value_counts()
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(cat_counts, labels=cat_counts.index, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title("Proportion of Sales by Product Category")
    plt.tight_layout()
    st.pyplot(fig)
    st.subheader("Insight")
    st.write("- Accessories jadi penjualan terbesar")
    st.write("- Distribusi penjualan per kategori sangat merata")

    # visual 5
    st.markdown("### 5) Trend Penjualan per Bulan")
    data['purchase_date'] = pd.to_datetime(data['purchase_date'])
    data['month'] = data['purchase_date'].dt.to_period('M')
    monthly_sales = data.groupby(
        'month').size().reset_index(name='sales_count')
    monthly_sales['month'] = monthly_sales['month'].dt.to_timestamp()
    fig = px.line(monthly_sales, x='month', y='sales_count',
                  title='Monthly Sales Trend')
    fig.update_layout(xaxis_title='Month', yaxis_title='Number of Sales')
    st.plotly_chart(fig)
    st.subheader("Insight")
    st.write("- Penjualan tertinggi terjadi pada bulan Juli 2025")


if __name__ == "__main__":
    run()
