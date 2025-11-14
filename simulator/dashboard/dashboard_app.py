import requests
import pandas as pd
import streamlit as st

API_BASE = "http://localhost:8000"


st.set_page_config(page_title="Water Pump Monitor", layout="wide")
st.title("Water Pump Monitoring Dashboard")


@st.cache_data(ttl=5)
def fetch_latest():
    url = f"{API_BASE}/readings/latest"
    r = requests.get(url, timeout=5)
    r.raise_for_status()
    data = r.json()
    if not data:
        return pd.DataFrame()
    df = pd.DataFrame.from_dict(data, orient="index")
    return df.reset_index(names=["pump_id"])


@st.cache_data(ttl=5)
def fetch_alerts(limit: int = 50):
    url = f"{API_BASE}/alerts"
    r = requests.get(url, params={"limit": limit}, timeout=5)
    r.raise_for_status()
    return r.json()


st.write("This dashboard displays the latest readings and recent alerts "
         "from the Water Pump Monitor API.")

if st.button("Refresh data"):
    st.cache_data.clear()

df = fetch_latest()
alerts = fetch_alerts()

st.subheader("Latest readings")

if df.empty:
    st.write("No readings available yet. Start the API and simulator to see data.")
else:
    st.dataframe(df)
    st.line_chart(df.set_index("pump_id")[["flow", "pressure"]])

st.subheader("Recent alerts")

if not alerts:
    st.write("No alerts.")
else:
    for alert in alerts:
        st.write(
            f"[{alert['timestamp']}] {alert['pump_id']} - "
            f"{alert['level'].upper()}: {alert['message']}"
        )
