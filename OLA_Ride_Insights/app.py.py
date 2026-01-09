import streamlit as st
import psycopg2
import pandas as pd

# =========================
# Page Config
# =========================
st.set_page_config(
    page_title="OLA Ride Insights",
    layout="wide"
)

# =========================
# Header
# =========================
st.title("🚕 OLA Ride Insights Dashboard")
st.subheader("End-to-End Data Analytics Project")
st.write("PostgreSQL • SQL • Power BI • Streamlit")

# =========================
# Sidebar
# =========================
st.sidebar.title("📊 OLA Analytics")

section = st.sidebar.radio(
    "Select Section",
    [
        "📌 About Project",
        "📋 Business Questions & Answers",
        "🧮 SQL Business Logic",
        "📊 SQL Outputs (Live)",
        "📈 Power BI Dashboard"
    ]
)

# =========================
# PostgreSQL Connection
# =========================
@st.cache_data
def run_query(query):
    conn = psycopg2.connect(
        host="localhost",
        database="ola",
        user="postgres",
        password="3602",
        port="5432"
    )
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# =========================================================
# 1️⃣ ABOUT PROJECT
# =========================================================
if section == "📌 About Project":

    st.header("📌 About This Project")

    st.markdown("""
    ### 🧠 Business Problem
    OLA handles large-scale ride operations daily.  
    Business teams require **actionable insights** to improve:
    - Ride success rate
    - Revenue efficiency
    - Cancellation reduction
    - Customer & driver experience

    ### 🎯 Objective
    Design an **end-to-end analytics solution** that transforms raw ride data
    into **decision-ready dashboards**.

    ### 🏗️ Project Architecture
    ```
    PostgreSQL → SQL Views → Power BI → Streamlit
    ```

    ### 🛠 Tools Used
    - PostgreSQL – Data storage
    - SQL – KPI & business logic
    - Power BI – Visual analytics
    - Streamlit – Web deployment

    ✅ Interview-ready & industry-aligned project
    """)


# =========================================================
# 2️⃣ BUSINESS QUESTIONS & ANSWERS
# =========================================================
elif section == "📋 Business Questions & Answers":

    st.header("📋 Business Problems & Insights")

    st.markdown("""
    ### 🧠 Business Problem 1: Booking Performance
    **Question:**  
    How many bookings are successfully completed on the OLA platform?

    **Insight:**  
    ✔ Identified total successful bookings using SQL view  
    ✔ Helps measure platform reliability and operational efficiency  

    ---

    ### 🧠 Business Problem 2: Ride Cancellations
    **Question:**  
    Why are rides getting cancelled and who cancels more – customers or drivers?

    **Insight:**  
    ✔ Customer and driver cancellations analyzed separately  
    ✔ Cancellation reasons help improve user experience and driver policies  

    ---

    ### 🧠 Business Problem 3: Revenue Contribution
    **Question:**  
    Which vehicle types and payment methods generate maximum revenue?

    **Insight:**  
    ✔ Revenue analyzed by vehicle category  
    ✔ Payment method usage highlights customer payment preferences  

    ---

    ### 🧠 Business Problem 4: Customer Value
    **Question:**  
    Who are the top customers contributing maximum rides?

    **Insight:**  
    ✔ Top 5 customers identified using booking frequency  
    ✔ Useful for loyalty programs and targeted offers  

    ---

    ### 🧠 Business Problem 5: Service Quality
    **Question:**  
    How satisfied are customers and drivers across vehicle types?

    **Insight:**  
    ✔ Customer & driver ratings analyzed vehicle-wise  
    ✔ Helps identify underperforming vehicle categories  

    ---

    🎯 **Business Outcome:**  
    This analysis enables OLA to:
    - Reduce ride cancellations  
    - Improve revenue strategies  
    - Enhance customer & driver satisfaction  
    - Take data-driven operational decisions  
    """)


# =========================================================
# 3️⃣ SQL BUSINESS LOGIC
# =========================================================
elif section == "🧮 SQL Business Logic":

    st.header("🧮 SQL Business Logic & KPI Design")

    st.markdown("""
    All KPIs are calculated at **database level** using SQL views  
    to ensure **performance, scalability, and reusability**.
    """)

    st.subheader("📌 KPI 1: Total Successful Bookings")
    st.code("""
CREATE OR REPLACE VIEW vw_total_successful_bookings AS
SELECT COUNT(*) AS total_successful_bookings
FROM rides
WHERE UPPER(TRIM("Booking_Status")) = 'SUCCESS';
""", language="sql")

    st.subheader("📌 KPI 2: Revenue by Payment Method")
    st.code("""
CREATE OR REPLACE VIEW vw_payment_method_distribution AS
SELECT
    "Payment_Method",
    COUNT(*) AS total_transactions
FROM rides
GROUP BY "Payment_Method";
""", language="sql")

    st.subheader("📌 KPI Coverage Using SQL")
    st.markdown("""
    ✔ Booking success & failure rate  
    ✔ Revenue by vehicle & payment method  
    ✔ Cancellation analysis (customer & driver)  
    ✔ Customer & driver ratings  

    📌 *SQL views act as a single source of truth for Power BI & Streamlit*
    """)


# =========================================================
# 4️⃣ SQL OUTPUTS (LIVE)
# =========================================================
elif section == "📊 SQL Outputs (Live)":

    st.header("📊 Live KPI Outputs (From PostgreSQL)")

    col1, col2, col3 = st.columns(3)

    df1 = run_query("SELECT * FROM vw_total_successful_bookings;")
    df2 = run_query("SELECT * FROM vw_customer_cancellations;")
    df3 = run_query("SELECT * FROM vw_total_successful_revenue;")

    col1.metric("✅ Successful Bookings", df1.iloc[0, 0])
    col2.metric("❌ Customer Cancellations", df2.iloc[0, 0])
    col3.metric("💰 Total Revenue", f"₹ {df3.iloc[0,0]:,.0f}")

    st.markdown("---")

    st.subheader("💳 Payment Method Usage")
    df4 = run_query("SELECT * FROM vw_payment_method_distribution;")
    st.dataframe(df4, use_container_width=True)
    st.bar_chart(df4.set_index("Payment_Method"))

    st.markdown("---")

    st.subheader("👥 Top 5 Customers by Rides")
    df5 = run_query("SELECT * FROM vw_top_5_customers;")
    st.dataframe(df5, use_container_width=True)


# =========================================================
# 5️⃣ POWER BI DASHBOARD (SCREENSHOTS)
# =========================================================
# =========================================================
# 4️⃣ POWER BI DASHBOARD
# =========================================================
elif section == "📈 Power BI Dashboard":

    st.header("📈 Power BI Business Dashboards")

    power_bi_url = "https://app.powerbi.com/groups/me/reports/932fd5d0-11cf-40f1-91a2-4258be3e49cb/cd964a6e0e127189e221?experience=power-bi"

    st.markdown("""
    This dashboard is designed using **Power BI** and connected with **PostgreSQL**.

    ### 🔍 Insights Covered
    - Overall booking performance
    - Vehicle type comparison
    - Revenue & payment analysis
    - Cancellation breakdown (customer & driver)
    - Driver & customer ratings
    """)

    st.warning(
        "⚠ Live Power BI embedding is restricted due to college/organizational tenant policy.\n\n"
        "✔ The report is **published on Power BI Service** and accessible via the link below.\n"
        "✔ Screenshots are shown for quick visual reference."
    )

    # 🔗 Power BI Link
    st.markdown(f"🔗 **[Open Live Power BI Dashboard]({power_bi_url})**")

    # 🔘 Button
    st.link_button("📊 View Power BI Dashboard", power_bi_url)

    st.divider()

    # 📸 Screenshots
    st.subheader("📌 Overall Performance")
    st.image("images/overall.png", use_container_width=True)

    st.subheader("🚗 Vehicle Type Analysis")
    st.image("images/vehicle_type.png", use_container_width=True)

    st.subheader("💰 Revenue Analysis")
    st.image("images/revenue.png", use_container_width=True)

    st.subheader("❌ Cancellation Analysis")
    st.image("images/cancellation.png", use_container_width=True)

    st.subheader("⭐ Ratings Analysis")
    st.image("images/ratings.png", use_container_width=True)

    st.success("✔ Power BI dashboards successfully integrated with Streamlit")

# =========================
# Footer
# =========================
st.markdown("---")
st.caption("© OLA Ride Insights | Built by Zishan Alam")
