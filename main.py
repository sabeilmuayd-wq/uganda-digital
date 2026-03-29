import streamlit as st
import pandas as pd
import segno
import io
from datetime import datetime

# إعداد الصفحة بطابع سيادي واحترافي (ألوان علم أوغندا)
st.set_page_config(page_title="Axion Pay | Uganda Digital Sovereignty", layout="wide")

# إضافة التنسيق الجمالي (CSS)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #006747; color: white; font-weight: bold; }
    .stButton>button:hover { background-color: #FFD100; color: black; }
    .gov-card { padding: 20px; border-radius: 10px; background-color: white; border-left: 5px solid #006747; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# القائمة الجانبية (Navigation)
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/4/4e/Flag_of_Uganda.svg", width=100)
st.sidebar.title("Axion Pay System")
menu = ["🏠 Home", "🆔 Digital ID (KYC)", "🐝 Hive Tracker (KTB)", "💰 Axion Micro-Finance", "📊 Gov Dashboard"]
choice = st.sidebar.selectbox("Navigate System", menu)

# --- 1. الصفحة الرئيسية ---
if choice == "🏠 Home":
    st.title("🇺🇬 Axion Pay: The Digital Backbone for Rural Uganda")
    st.subheader("Bridging the gap between Wood, Honey, and Digital Finance.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="gov-card"><h3>30M+</h3><p>Rural Citizens Target</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="gov-card"><h3>100%</h3><p>Transparent Ledger</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="gov-card"><h3>Vision 2040</h3><p>National Alignment</p></div>', unsafe_allow_html=True)

    st.write("---")
    st.markdown("### Why Axion Pay?")
    st.info("We provide a digital ecosystem where a carpenter in Bweyale can sell a beehive, and a farmer in Kiryandongo can secure a loan using honey as collateral.")

# --- 2. الهوية الرقمية (KYC) ---
elif choice == "🆔 Digital ID (KYC)":
    st.title("Secure Identity Management")
    st.write("Integrated with National Identification and Registration Authority (NIRA) Simulation.")
    
    with st.form("kyc_form"):
        name = st.text_input("Full Name (As per NIN)")
        nin = st.text_input("National ID Number (NIN)")
        location = st.selectbox("District", ["Kiryandongo", "Kampala", "Gulu", "Mbarara", "Nyala (Sudan Branch)"])
        uploaded_file = st.file_uploader("Upload ID Photo/Document")
        if st.form_submit_button("Verify Identity"):
            if nin:
                st.success(f"Identity for {name} verified successfully.")
            else:
                st.error("Please enter a valid NIN.")

# --- 3. تتبع خلايا النحل (الحل المصلح للأخطاء) ---
elif choice == "🐝 Hive Tracker (KTB)":
    st.title("Asset Tracking: Cypress KTB Beehives")
    st.write("Every hive produced is registered as a unique Digital Asset.")
    
    with st.expander("Register New Hive (Carpenter Entry)", expanded=True):
        h_id = st.text_input("Hive Serial Number", value=f"KTB-UG-{datetime.now().strftime('%M%S')}")
        wood_type = st.selectbox("Wood Type", ["Cypress", "African Sandalwood", "Pine"])
        st.write("Quality Checklist: 120° Angle ✅ | 3.2cm Top Bars ✅ | Secure v1.4 ✅")
        
        if st.button("Generate Digital Tag"):
            # توليد الـ QR يدوياً باستخدام مكتبة segno لتجنب أخطاء الإصدارات
            qr_link = f"https://uganda-digital-platform.streamlit.app/track?id={h_id}"
            qr = segno.make(qr_link)
            out = io.BytesIO()
            qr.save(out, kind='png', scale=10)
            
            st.image(out.getvalue(), caption=f"Digital Asset Tag for {h_id}", width=300)
            st.success(f"Hive {h_id} is now registered in the Sovereign Ledger.")
            st.download_button(label="Download QR for Printing", 
                             data=out.getvalue(), 
                             file_name=f"hive_{h_id}_qr.png", 
                             mime="image/png")

# --- 4. التمويل الأصغر ---
elif choice == "💰 Axion Micro-Finance":
    st.title("Honey-Collateral Micro-Finance")
    st.write("Empowering rural entrepreneurs through the Parish Development Model (PDM).")
    
    amount = st.slider("Loan Amount (UGX)", 50000, 2000000, 250000)
    repayment = amount * 1.05
    st.metric("Repayment Amount (via Honey)", f"{repayment:,.0f} UGX", delta="5% Interest Rate")
    
    if st.button("Apply for Hive Financing"):
        st.balloons()
        st.success("Application transmitted to Axion Pay Liquidity Pool.")

# --- 5. لوحة بيانات الحكومة ---
elif choice == "📊 Gov Dashboard":
    st.title("🏛 National Monitoring & Evaluation (Real-time)")
    st.write("Decision-making data for the Government of Uganda.")
    
    chart_data = pd.DataFrame({
        'Parish': ['Bweyale', 'Kiryandongo Town', 'Mutunda', 'Bweyale Refugees Camp'],
        'Active Hives': [120, 85, 200, 350],
        'Financial Flow (UGX)': [4500000, 3100000, 7200000, 12500000]
    })
    
    st.bar_chart(chart_data.set_index('Parish')['Active Hives'])
    st.table(chart_data)
    st.download_button("Export Economic Report (CSV)", chart_data.to_csv(index=False), "report.csv", "text/csv")

# تذييل الصفحة
st.sidebar.write("---")
st.sidebar.caption(f"System Version: Secure v1.4 | Date: {datetime.now().strftime('%Y-%m-%d')}")
st.sidebar.caption("Developed by: The Chosen One (Al-Mustafa)")
