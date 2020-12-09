import pandas as pd
import streamlit as st
import ta
import yfinance as yf

# Disable the deprecation warning for file uploader encoding
st.set_option('deprecation.showfileUploaderEncoding', False)


@st.cache
def get_fundamental_data():
    """Download fundamental data for the first 100 cryptocurrencies on Yahoo Finance."""
    components = pd.read_html('https://finance.yahoo.com/cryptocurrencies/?count=100&offset=0')[0]
    return components.drop(['1 Day Chart', '52 Week Range'], axis=1).set_index('Symbol')


@st.cache
def get_ohlcv_data(asset):
    """Download daily OHLCV data for a given currency pair."""
    return yf.download(asset)


def main():
    components = get_fundamental_data()
    title = st.empty()
    st.sidebar.title('Options')

    def label(symbol):
        """Create label for a given currency pair."""
        symbol_info = components.loc[symbol]
        return symbol + ' - ' + symbol_info.Name

    if st.sidebar.checkbox('View cryptocurrencies list'):
        st.dataframe(components[['Name',
                                 'Price (Intraday)',
                                 'Change',
                                 '% Change',
                                 'Market Cap',
                                 ]])

    st.sidebar.subheader('Asset')
    asset = st.sidebar.selectbox('Select asset', components.index.sort_values(), index=3, format_func=label)
    title.title(components.loc[asset].Name)

    if st.sidebar.checkbox('View fundamentals', True):
        st.table(components.loc[asset])
    ohlcv_data_raw = get_ohlcv_data(asset)
    ohlcv_data = ohlcv_data_raw.copy().dropna()
    ohlcv_data.index.name = None

    section = st.sidebar.slider('Number of quotes', min_value=30, max_value=min([2000, ohlcv_data.shape[0]]), value=500,
                                step=10)

    adj_close_data = ohlcv_data[-section:]['Adj Close'].to_frame('Adj Close')
    ohlcv_ta_data = ohlcv_data.copy()
    ohlcv_ta_data = ta.add_all_ta_features(ohlcv_ta_data, 'Open', 'High', 'Low', 'Close', 'Volume', fillna=True)
    momentum = ohlcv_ta_data[['momentum_rsi',
                              'momentum_roc',
                              'momentum_tsi',
                              'momentum_uo',
                              'momentum_stoch',
                              'momentum_stoch_signal',
                              'momentum_wr',
                              'momentum_ao',
                              'momentum_kama',
                              ]]
    volatility = ohlcv_ta_data[['volatility_atr',
                                'volatility_bbm',
                                'volatility_bbh',
                                'volatility_bbl',
                                'volatility_bbw',
                                'volatility_bbp',
                                'volatility_bbhi',
                                'volatility_bbli',
                                'volatility_kcc',
                                'volatility_kch',
                                'volatility_kcl',
                                'volatility_kcw',
                                'volatility_kcp',
                                'volatility_kchi',
                                'volatility_kcli',
                                'volatility_dcl',
                                'volatility_dch',
                                ]]

    sma = st.sidebar.checkbox('SMA')
    if sma:
        period = st.sidebar.slider('SMA period', min_value=5, max_value=500, value=20, step=1)
        ohlcv_data[f'SMA {period}'] = ohlcv_data['Adj Close'].rolling(period).mean()
        adj_close_data[f'SMA {period}'] = ohlcv_data[f'SMA {period}'].reindex(adj_close_data.index)

    sma2 = st.sidebar.checkbox('SMA2')
    if sma2:
        period2 = st.sidebar.slider('SMA2 period', min_value=5, max_value=500, value=100, step=1)
        ohlcv_data[f'SMA2 {period2}'] = ohlcv_data['Adj Close'].rolling(period2).mean()
        adj_close_data[f'SMA2 {period2}'] = ohlcv_data[f'SMA2 {period2}'].reindex(adj_close_data.index)

    st.subheader('Chart')
    st.line_chart(adj_close_data)

    if st.sidebar.checkbox('View momentum indicators'):
        st.subheader('Apply Technical Indicators')
        st.code("""
            data = ta.add_all_ta_features(ohlcv_ta_data, 'Open', 'High', 'Low', 'Close', 'Volume', fillna=True)
        """, language='python')
        st.header(f'Momentum Indicators')
        transpose = momentum.iloc[[-5, -4, -3, -2, -1]].transpose()
        st.table(transpose.style.background_gradient(cmap='Blues', axis=1))
        for col in momentum.columns:
            st.subheader(f'Momentum Indicator: {col}')
            st.line_chart(ohlcv_ta_data[-section:][col].to_frame(col))

    if st.sidebar.checkbox('View volatility indicators'):
        st.subheader('Apply Technical Indicators')
        st.code("""
            data = ta.add_all_ta_features(ohlcv_ta_data, 'Open', 'High', 'Low', 'Close', 'Volume', fillna=True)
        """, language='python')
        st.header(f'Volatility Indicators')
        transpose = volatility.iloc[[-5, -4, -3, -2, -1]].transpose()
        st.table(transpose.style.background_gradient(cmap='Blues', axis=1))
        for col in volatility.columns:
            st.subheader(f'Momentum Indicator: {col}')
            st.line_chart(ohlcv_ta_data[-section:][col].to_frame(col))

    if st.sidebar.checkbox('Personal portfolio analysis'):
        st.subheader(f'{asset} personal portfolio analysis')
        file_buffer = st.file_uploader("Choose a .csv or .xlxs file. Column names must be 'rate' and 'price'",
                                       type=['xlsx', 'csv'])
        if file_buffer is not None:
            file = pd.read_excel(file_buffer)
            file = pd.DataFrame(file)
            st.table(file.style.background_gradient(cmap='Blues'))
            weighted_rate = (file['price'] * file['rate']).sum() / file['price'].sum()
            daily_price = ohlcv_data.Close.iloc[-1]
            perf = {'buying price': weighted_rate, 'current price': daily_price}
            performance = pd.DataFrame(perf, columns=['buying price', 'current price'], index=[asset])
            st.table(performance.style.background_gradient(cmap='Blues', axis=1))

    if st.sidebar.checkbox('View statistics'):
        st.subheader('Statistics')
        st.table(adj_close_data.describe())

    if st.sidebar.checkbox('View quotes'):
        st.subheader(f'{asset} historical closing prices')
        st.write(adj_close_data)

    st.sidebar.title('About')
    st.sidebar.info('Lorem ipsum')


if __name__ == '__main__':
    main()
