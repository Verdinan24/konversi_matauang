import requests
import streamlit as st

st.title("Aplikasi Konversi Mata Uang ASEAN")

# Daftar mata uang negara-negara ASEAN
asean_currencies = {
    'Indonesia (IDR)': 'IDR',
    'Malaysia (MYR)': 'MYR',
    'Singapura (SGD)': 'SGD',
    'Thailand (THB)': 'THB',
    'Filipina (PHP)': 'PHP',
    'Vietnam (VND)': 'VND',
    'Brunei (BND)': 'BND',
    'Kamboja (KHR)': 'KHR',
    'Laos (LAK)': 'LAK',
    'Myanmar (MMK)': 'MMK',
    'Timor Leste (USD)': 'USD'
}

from_currency_label = st.selectbox('Pilih mata uang awal:', list(asean_currencies.keys()))
from_currency = asean_currencies[from_currency_label]

to_currency_label = st.selectbox('Pilih mata uang tujuan:', list(asean_currencies.keys()))
to_currency = asean_currencies[to_currency_label]

amount = st.number_input("Masukkan jumlah uang:", min_value=0.0, format="%.2f")

if st.button("Konversi"):
    if from_currency != to_currency:
        try:
            api_key = '6b48d67e8ecbc41cab19a3b3'  # API key Anda
            url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}/{amount}"

            response = requests.get(url)
            data = response.json()

            if data['result'] == 'success':
                converted_amount = data['conversion_result']
                st.success(f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
            else:
                st.error("Error dalam konversi mata uang")

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Mata uang awal dan tujuan tidak boleh sama!")
