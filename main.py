import streamlit as st
import pandas as pd
from datetime import datetime

# إعداد الصفحة لإعطاء طابع سيادي واحترافي
st.set_page_config(page_title="Axion Pay | Uganda Digital Sovereignty", layout="wide")

# إضافة التنسيق الجمالي
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #006747; color: white; }
    .gov-card { padding: 20px; border-radius: 10px; background-color: white; border-left: 5px solid #006747; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# القائمة الجانبية (Navigation)
menu = ["🏠 Home", "🆔 Digital ID (KYC)", "🐝 Hive Tracker (KTB)", "💰 Axion Micro-Finance", "📊 Gov Dashboard"]
choice = st.sidebar.selectbox("Navigate System", menu)

# --- 1. الصفحة الرئيسية ---
if choice == "🏠 Home":
    st.title("🇺🇬 Axion Pay: The Digital Backbone for Rural Uganda")
    st.subheader("Bridging the gap between Wood, Honey, and Digital Finance.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("### 30M+ \n Rural Citizens target")
    with col2:
        st.success("### 100% \n Transparent Ledger")
    with col3:
        st.warning("### Vision 2040 \n Alignment")

    st.write("---")
    st.markdown("### Why Axion Pay?")
    st.write("We provide a digital ecosystem where a carpenter in Bweyale can sell a beehive, and a farmer in Kiryandongo can secure a loan using honey as collateral.")

# --- 2. الهوية الرقمية (قوة الإقناع الحكومي) ---
elif choice == "🆔 Digital ID (KYC)":
    st.title("Secure Identity Management")
    st.write("Integrated with NIRA (Simulation) for secure transactions.")
    
    with st.form("kyc_form"):
        name = st.text_input("Full Name (As per NIN)")
        nin = st.text_input("National ID Number (NIN)")
        location = st.selectbox("District", ["Kiryandongo", "Kampala", "Gulu", "Mbarara"])
        uploaded_file = st.file_uploader("Upload ID Photo")
        if st.form_submit_button("Verify Identity"):
            st.success(f"Identity for {name} verified against National Database.")

# --- 3. تتبع خلايا النحل (الربط بين الورشة والمنصة) ---
elif choice == "🐝 Hive Tracker (KTB)":
    st.title("Asset Tracking: Cypress KTB Beehives")
    st.write("Every hive produced is a digital asset.")
    
    # محاكاة لإضافة خلية جديدة من ورشتك
    with st.expander("Register New Hive (Carpenter Entry)"):
        h_id = st.text_input("Hive Serial Number", value="KTB-UG-001")
        wood_type = st.selectbox("Wood Type", ["Cypress", "Pine"])
        st.write("Quality Check: 120° Angle ✅ | 3.2cm Top Bars ✅")
        if st.button("Generate QR Code & Register"):
            st.qr_code(f"https://axion-pay.ug/track/{h_id}")
            st.success("Hive Registered in Sovereignty Ledger.")

# --- 4. التمويل الأصغر (المال والسمعة) ---
elif choice == "💰 Axion Micro-Finance":
    st.title("Honey-Collateral Loans")
    st.write("Empowering farmers through the Parish Development Model (PDM).")
    
    amount = st.slider("Loan Amount (UGX)", 50000, 1000000, 200000)
    repayment = amount * 1.05  # فائده بسيطة 5% فقط للعدل
    st.write(f"Repayment Amount: **{repayment:,.0f} UGX** via Honey supply.")
    if st.button("Apply for Hive Financing"):
        st.balloons()
        st.success("Application sent to Axion Liquidity Pool.")

# --- 5. لوحة بيانات الحكومة (الباب الكبير) ---
elif choice == "📊 Gov Dashboard":
    st.title("🏛 National Monitoring & Evaluation")
    st.write("Real-time data for policymakers.")
    
    # محاكاة بيانات حقيقية للحكومة
    chart_data = pd.DataFrame({
        'Parish': ['Bweyale', 'Kiryandongo Town', 'Mutunda'],
        'Active Hives': [120, 85, 200],
        'Financial Flow (UGX)': [4500000, 3100000, 7200000]
    })
    st.bar_chart(chart_data.set_index('Parish'))
    st.table(chart_data)
    st.download_button("Download Full Economic Report (CSV)", "data.csv", "text/csv")
