import pandas as pd
import streamlit as st
import pickle


with open('src/knn_tuned_pipeline.pkl', 'rb') as file:
    model = pickle.load(file)


def run():
    # title
    st.title('Retail Fashion Boutique Data Sales Analytics 2025')
    st.subheader(
        'Halaman ini berisi terkait dengan Prediksi Return Rate Fashion Boutique Data Sales Analytics 2025')
    st.markdown('---')
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRotZ9AvBpDiZWDoKopik5lx85mMs9CUPYQow&s',
             caption='Banner Fashion')

    # form
    with st.form(key="prediction_form"):
        st.markdown("### Masukkan Spesifikasi Produk")

        category = st.selectbox("category", options=[
                                "Dresses", "Tops", "Bottoms", "Outerwear", "Shoes", "Accessories"])
        brand = st.selectbox("Brand", options=[
                             "Zara", "H&M", "Forever21", "Mango", "Uniqlo", "Gap", "Banana Republic", "Ann Taylor"])
        season = st.selectbox(
            "Season", options=["Spring", "Summer", "Fall", "Winter"])
        size = st.selectbox(
            "Size", options=["XS", "S", "M", "L", "XL", "XXL", "No Size"])
        color = st.selectbox("Colour", options=[
                             "Black", "White", "Navy", "Gray", "Beige", "Red", "Blue", "Green", "Pink", "Brown", "Purple"])
        original_price = st.number_input(
            "Price ($)", min_value=0.0, max_value=300.0, value=99.99, step=0.01)
        markdown_percentage = st.number_input(
            "Discount (%)", min_value=0, max_value=60, value=10, step=1)
        stock_quantity = st.number_input(
            "Stock", min_value=0, max_value=50, value=10, step=1)
        customer_rating = st.number_input(
            "Rating Produk (1–5)", min_value=1.0, max_value=5.0, value=3.5, step=0.1)

        submit = st.form_submit_button(label="Predict")
    # dataframe
    data = pd.DataFrame([{
        "category": category,
        "brand": brand,
        "season": season,
        "size": size,
        "color": color,
        "original_price": original_price,
        "markdown_percentage": markdown_percentage,
        "stock_quantity": stock_quantity,
        "customer_rating": customer_rating
    }])

    # show data
    st.dataframe(data)

    if submit:
        prediction = model.predict(data)
        prediction_proba = model.predict_proba(data)

        if prediction[0] == 0:
            st.success(f"Prediksi: Produk Tidak Diretur")
        else:
            st.error(f"Prediksi: Produk Diretur")

        st.write(f"Probabilitas Tidak Diretur: {prediction_proba[0][0]:.2f}")
        st.write(f"Probabilitas Diretur: {prediction_proba[0][1]:.2f}")
        st.markdown('---')


if __name__ == '__main__':
    run()
