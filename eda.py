import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st


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
    st.write("- Distribusi harga mayoritas di bawah $1 50")
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
    plt.ylabel("Current Price")
    plt.tight_layout()
    st.pyplot(fig)

    st.subheader("Insight")
    st.write("- Perbedaan  harga antar kategori terlihat jelas, Kateogri Outerwear memiliki nilai lebih tinggi")

    # visual 4
    st.markdown("### 4) Proporsi Penjualan per Kategori Produk")
    cat_counts = data['category'].value_counts()
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(cat_counts, labels=cat_counts.index, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title("Sales Share by Product Category")
    plt.tight_layout()
    st.pyplot(fig)

    st.subheader("Insight")
    st.write("- Accessories jadi penjualan terbesar")
    st.write("- Distribusi penjualan per kategori sangat merata")

    # visual 5
    st.markdown("### 5) Return Rate per Brand")
    brand_returnrate = (data.groupby('brand')['is_returned'].mean(
    ).sort_values(ascending=False) * 100).reset_index()
    fig = plt.figure(figsize=(12, 6))
    sns.barplot(data=brand_returnrate, x='brand', y='is_returned')
    plt.title("Return Rate by brand")
    plt.xlabel("Brand")
    plt.ylabel("Return Rate")
    plt.tight_layout()
    st.pyplot(fig)

    st.subheader("Insight")
    st.write("- Beberapa brand menunjukkan return rate lebih tinggi seperti (Ann Taylor) yang dimana harus melakukan untuk Quality Check yang lebih baik")


if __name__ == "__main__":
    run()
