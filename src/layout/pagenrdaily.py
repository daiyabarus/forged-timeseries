import pandas as pd
import streamlit as st


class NRDaily:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def transform_data(self):
        pass  # Add your transformation logic here

    def plot_chart(self):
        st.write("NR Data Visualization Coming Soon...")


def nr_daily_page(df: pd.DataFrame):
    nr_page = NRDaily(df)
    nr_page.transform_data()
    nr_page.plot_chart()
