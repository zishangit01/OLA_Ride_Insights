# 🚕 OLA Ride Insights – End-to-End Data Analytics Project

An end-to-end, business-focused data analytics project built on OLA ride data to
deliver actionable insights using **PostgreSQL, SQL, Power BI, and Streamlit**.

This project demonstrates how raw operational data is transformed into
**decision-ready dashboards** for business stakeholders.

---

## 🧠 Business Problem

OLA manages large-scale ride operations daily. Business teams need clear insights to:

- Improve ride success rate  
- Reduce customer and driver cancellations  
- Optimize revenue and payment methods  
- Analyze vehicle-wise performance  
- Measure customer and driver satisfaction  

---

## 🎯 Project Objective

To design and implement a complete end-to-end analytics solution that:

- Processes raw ride data stored in PostgreSQL  
- Computes KPIs at the database level using SQL views  
- Visualizes insights through Power BI dashboards  
- Delivers results via a Streamlit web application  

---

## 🏗️ Project Architecture

PostgreSQL (Raw Ride Data)  
↓  
SQL Views & Business KPIs  
↓  
Power BI Dashboards  
↓  
Streamlit Web Application  

This architecture ensures:
- High performance  
- Reusable KPIs  
- A single source of truth for analytics  

---

## 🛠️ Tools & Technologies

- PostgreSQL – Data storage and KPI computation  
- SQL – Business logic, aggregations, and views  
- Power BI – Interactive business dashboards  
- Streamlit – Web-based analytics deployment  
- Python (Pandas, Psycopg2) – Database connectivity  

---

## 📋 Business Questions Solved

1. How many bookings are successfully completed?  
2. Who cancels more—customers or drivers?  
3. Which vehicle types generate the highest revenue?  
4. Which payment methods are most preferred?  
5. Who are the top customers by ride frequency?  
6. How satisfied are customers and drivers?  

Insights are delivered using:
**SQL Views + Power BI Visuals + Streamlit Live Outputs**

---

## 🧮 SQL Business Logic

All KPIs are calculated at the database level using SQL views.

### Example: Total Successful Bookings

```sql
CREATE OR REPLACE VIEW vw_total_successful_bookings AS
SELECT COUNT(*) AS total_successful_bookings
FROM rides
WHERE UPPER(TRIM(booking_status)) = 'SUCCESS';

SQL views act as a single source of truth for both Power BI and Streamlit.

## 📊 Live SQL Outputs (Streamlit)

The Streamlit application connects directly to PostgreSQL and displays:

- Total successful bookings  
- Customer cancellations  
- Total revenue (₹)  
- Payment method usage  
- Top 5 customers by rides  

These KPIs are fetched live from the database and update dynamically.
## 📈 Power BI Business Dashboards

Power BI dashboards provide visual insights on:

- Overall booking performance  
- Vehicle type comparison  
- Revenue and payment trends  
- Cancellation breakdown (customer & driver)  
- Driver and customer ratings  

⚠ Live Power BI embedding is restricted due to organizational tenant policy.  
✔ The report is published on Power BI Service  
✔ Dashboard screenshots are shown inside Streamlit for quick reference

## 📁 Repository Structure

```
OLA_Ride_Insights/
│
├── app.py                       # Streamlit application
├── ola_sql_business_logic.sql   # SQL views & KPI logic
├── images/                      # Power BI dashboard screenshots
├── powerbi/                     # Power BI (.pbix) file
├── reports/                     # End-to-end project report (PDF)
├── data/                        # Dataset (if applicable)
```

## 🚀 Outcome

This project demonstrates:

- End-to-end data analytics workflow  
- Strong SQL and database design skills  
- Business-focused Power BI dashboards  
- Live KPI integration using Streamlit  
- Industry-aligned analytics project execution  
## 🔗 Project Links

- 📊 Power BI Dashboard (Service):  
  https://app.powerbi.com/groups/me/reports/932fd5d0-11cf-40f1-91a2-4258be3e49cb

- 🧑‍💻 Streamlit App (Local Demo):  
  Run `streamlit run app.py`

- 🗄 SQL Business Logic:  
  `ola_sql_business_logic.sql`

- 📄 End-to-End Business Report:  
  `reports/OLA_Ride_Insights_End_to_End_Analytics_Report.pdf`

---

## 👤 Author

**Zishan Alam**  
Aspiring Data Analyst  
📍 Bangalore, India



