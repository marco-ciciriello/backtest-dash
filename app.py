import streamlit as st
from multiapp import MultiApp
from apps import home, stock, twitter

app = MultiApp()

# Application pages
app.add_app('Home', home.app)
app.add_app('Stock', stock.app)
app.add_app('Twitter', twitter.app)

app.run()
