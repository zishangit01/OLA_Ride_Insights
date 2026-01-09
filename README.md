# 🚕 OLA Ride Insights – End-to-End Data Analytics Project

An end-to-end **business-focused data analytics project** built on OLA ride data to
derive actionable insights using **PostgreSQL, SQL, Power BI, and Streamlit**.

This project demonstrates how raw operational data can be transformed into
**decision-ready dashboards** for business stakeholders.

---

## 🧠 Business Problem

OLA handles large-scale ride operations on a daily basis.
Business teams require **actionable insights** to:

- Improve ride success rate
- Reduce customer & driver cancellations
- Optimize revenue and payment methods
- Analyze vehicle-wise performance
- Measure customer & driver satisfaction

---

## 🎯 Project Objective

To design and implement a **complete end-to-end analytics solution** that:

- Processes raw ride data stored in PostgreSQL
- Computes KPIs at database level using SQL views
- Visualizes insights using Power BI dashboards
- Presents results through a Streamlit web application

---

## 🏗️ Project Architecture

PostgreSQL (Raw Ride Data)
↓
SQL Views & Business KPIs
↓
Power BI Dashboards
↓
Streamlit Web Application

yaml
Copy code

This architecture ensures:
- High performance
- Reusability of KPIs
- Single source of truth for analytics

---

## 🛠️ Tools & Technologies

- **PostgreSQL** – Data storage & KPI computation  
- **SQL** – Business logic, aggregations, views  
- **Power BI** – Interactive business dashboards  
- **Streamlit** – Web-based analytics deployment  
- **Python (Pandas, Psycopg2)** – Database connectivity  

---

## 📋 Business Questions Solved

1. How many bookings are successfully completed?
2. Why are rides cancelled and who cancels more – customers or drivers?
3. Which vehicle types generate maximum revenue?
4. Which payment methods are most preferred by customers?
5. Who are the top customers by ride frequency?
6. How satisfied are customers and drivers across vehicle types?

Each question is answered using a combination of:
**SQL Views + Power BI Visuals + Streamlit Live Outputs**

---

## 🧮 SQL Business Logic

All KPIs are calculated at the **database level** using SQL views to ensure:

- Performance
- Scalability
- Consistency across tools

### Example: Total Successful Bookings
```sql
CREATE OR REPLACE VIEW vw_total_successful_bookings AS
SELECT COUNT(*) AS total_successful_bookings
FROM rides
WHERE UPPER(TRIM(booking_status)) = 'SUCCESS';
SQL views act as a single source of truth for both Power BI and Streamlit.

📊 Live SQL Outputs (Streamlit)
The Streamlit application connects directly to PostgreSQL and displays:

Total successful bookings

Customer cancellations

Total revenue (₹)

Payment method usage

Top 5 customers by rides

These metrics are fetched live from the database.

📈 Power BI Business Dashboards
Power BI dashboards provide visual insights on:

Overall booking performance

Vehicle type comparison

Revenue & payment trends

Cancellation breakdown (customer & driver)

Driver & customer ratings

⚠ Live Power BI embedding is restricted due to organizational tenant policy.
✔ The report is published on Power BI Service
✔ Screenshots are included for quick visual reference inside Streamlit

📁 Repository Structure
powershell
Copy code
OLA_Ride_Insights/
│
├── app.py                       # Streamlit application
├── ola_sql_business_logic.sql   # SQL views & KPI logic
├── images/                      # Power BI dashboard screenshots
├── powerbi/                     # Power BI (.pbix) file
├── reports/                     # Project report (PDF)
├── data/                        # Dataset (if applicable)
🚀 Outcome
This project demonstrates:

Strong SQL & database fundamentals

Business-oriented problem solving

Dashboard storytelling using Power BI

End-to-end analytics project ownership

✅ Industry-aligned | Internship-ready | Interview-ready

👤 Author
Zishan Alam
Aspiring Data Analyst
📍 Bangalore, India
