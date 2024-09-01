import streamlit as st
from forex_python.converter import CurrencyRates, CurrencyCodes

c = CurrencyRates()
code = CurrencyCodes()

st.title("Aplikasi Konversi Mata Uang ASEAN")

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

from_currency_label = st.selectbox(
    'Pilih mata uang awal:',list(asean_currencies.keys())
)
from_currency = asean_currencies[from_currency_label]

to_currency_label = st.selectbox(
    'Pilih mata uang tujuan:',list(asean_currencies.keys())
)
to_currency = asean_currencies[to_currency_label]

amount = st.number_input("Masukkan jumlah uang:", min_value=0.0, format="%.2f")

if st.button("Konversi"):
    if from_currency != to_currency:
        try:
            converted_amount = c.convert(from_currency, to_currency, amount)
            symbol = code.get_symbol(to_currency)

            st.success(f"{amount:.2f} {from_currency} = {symbol} {converted_amount:.2f} {to_currency}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Mata uang awal dan tujuan tidak boleh sama!")

