import os

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Use the service name defined in your docker-compose.yml
API_URL = os.getenv("API_URL")

st.set_page_config(page_title="Inventory Manager", layout="centered")
st.title("📦 Item Manager")

success_status_code = 200

# --- CREATE SECTION ---
with st.form("add_item_form"):
    st.subheader("Add New Item")
    title = st.text_input("Item Title")
    desc = st.text_area("Description")
    submit = st.form_submit_button("Save to Database")

    if submit:
        payload = {"title": title, "description": desc}
        response = requests.post(f"{API_URL}/items", json=payload)

        if response.status_code == success_status_code:
            st.success(f"Added: {response.json()['title']}")
        else:
            st.error("Failed to save item.")

# --- READ SECTION ---
st.divider()
st.subheader("Current Inventory")

if st.button("Refresh List"):
    res = requests.get(f"{API_URL}/items")
    if res.status_code == success_status_code:
        items = res.json()
        if items:
            st.table(items)
        else:
            st.info("No items found in SQLite.")
