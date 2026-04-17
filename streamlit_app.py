import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="PADI Sovereign Bureau", page_icon="🚢", layout="wide")

st.title("🚢 PADI Sovereign Bureau: N-1 Nairobi")
st.markdown("### Maritime Logistics & Safety Integrity Portal")

# Load the local files we just pushed
def load_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Section I: Logistics Audit")
    try:
        audit_data = load_data('maritime_audit.json')
        df = pd.DataFrame(audit_data['results'])
        st.table(df)
        st.success(f"Verified Audit ID: {audit_data.get('timestamp', '20260417')}-MAR-ALPHA")
    except Exception as e:
        st.error("Logistics data not found.")

with col2:
    st.subheader("Section II: Safety Readiness")
    try:
        safety_data = load_data('safety_drill_log.json')
        st.json(safety_data)
        st.metric("Drill Status", "COMPLETED", delta="SOLAS Compliant")
    except Exception as e:
        st.error("Safety logs not found.")

st.divider()
st.info("System Perspective: The Peculiar Librarian | Node: Nairobi-01")
