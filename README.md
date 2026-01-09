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
