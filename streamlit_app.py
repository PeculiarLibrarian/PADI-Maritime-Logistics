import streamlit as st

st.set_page_config(page_title="PADI Sovereign Bureau", layout="wide", page_icon="🏛️")

st.title("🏛️ Nairobi-01 Node: Sovereign Bureau")
st.sidebar.markdown("### The Peculiar Librarian\n**Global IP & Audit Node**")

tabs = st.tabs(["🛒 IP Storefront", "📥 Secure Intake", "🛡️ Settlement Logic"])

with tabs[0]:
    st.header("Intellectual Property & Services")
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("### 📦 PADI Standard v2.1")
        st.write("Complete technical documentation and SHACL schemas.")
        st.link_button("View on Gumroad (Reviews)", "https://gumroad.com", use_container_width=True)
        
    with col2:
        st.info("### 🔍 Institutional Audit")
        st.write("One-on-one maritime data validation via Wise/Payoneer.")
        st.link_button("Request B2B Invoice", "mailto:samuel@example.com", use_container_width=True)

with tabs[2]:
    st.header("Financial Sovereignty")
    st.write("This node utilizes a **Multi-Rail Settlement System**:")
    st.markdown("""
    * **Tier 1 (Retail):** Gumroad (Credit Card / Apple Pay)
    * **Tier 2 (Institutional):** Wise (Direct Bank Transfer)
    * **Tier 3 (Alternative):** Payoneer Global Core
    """)
    st.success("Redundancy Level: High (Sovereign Compliant)")
