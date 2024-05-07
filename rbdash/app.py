import streamlit as st
import pandas as pd
import requests
import plotly.express as px

def get_btc_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    return response.json()

def get_lnd_data():
    response = requests.get("https://jsonplaceholder.typicode.com/comments")
    return response.json()


def main():
    st.title("Bitcoin Core & Lightning Node Dashboard")
    st.write("A simple dashboard to display statistics about your Bitcoin Core and Lightning node.")

    btc_data = get_btc_data()
    lnd_data = get_lnd_data()

    st.subheader("Bitcoin Core Node Information")
    st.write(f"Block Height: {btc_data[0]['id']}")
    st.write(f"Network Difficulty: {btc_data[1]['title']}")
    st.write(f"Mempool Size: {btc_data[2]['body']}")

    st.subheader("Lightning Node Information")
    st.write(f"Lightning Version: {lnd_data[0]['id']}")
    st.write(f"Active Channels: {lnd_data[1]['title']}")

    traffic_data = pd.DataFrame({"Incoming": [i for i in range(100)], "Outgoing": [i * 2 for i in range(100)]})
    line_chart = st.line_chart(traffic_data)

    for i in range(100, 200):
        new_data = {"Incoming": [i], "Outgoing": [i * 2]}
        traffic_data = traffic_data.append(new_data, ignore_index=True)
        time.sleep(1)
        line_chart.add_rows(new_data)

    st.subheader("Mempool Statistics")
    mempool_data = pd.DataFrame({"Unconfirmed Transactions": [i for i in range(100)], "Count": [i % 10 for i in range(100)]})
    fig = px.histogram(mempool_data, x="Unconfirmed Transactions", y="Count", title="Mempool Transaction Distribution")
    st.plotly_chart(fig)

    