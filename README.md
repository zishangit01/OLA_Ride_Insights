# 🚕 OLA Ride Insights – End-to-End Data Analytics Project

An end-to-end **business-focused data analytics project** built on OLA ride data to
derive actionable insights using **PostgreSQL, SQL, Power BI, and Streamlit**.

This project demonstrates how raw operational data can be transformed into
decision-ready dashboards for business stakeholders.

---

## 🧠 Business Problem

OLA handles large-scale ride operations daily.
Business teams need clear insights to:

- Improve ride success rate
- Reduce customer & driver cancellations
- Optimize revenue and payment methods
- Understand vehicle-wise performance
- Measure customer & driver satisfaction

---

## 🎯 Project Objective

To design and implement a **complete analytics solution** that:
- Processes raw ride data
- Computes KPIs at database level using SQL
- Visualizes insights using Power BI
- Presents results through a Streamlit web app

---

## 🏗️ Project Architecture


---

## 🛠️ Tools & Technologies

- **PostgreSQL** – Data storage & KPI computation
- **SQL** – Business logic, views, aggregations
- **Power BI** – Interactive dashboards & visual analytics
- **Streamlit** – Web-based analytics presentation
- **Python (Pandas, Psycopg2)** – Database integration

---

## 📋 Business Questions Solved

1. How many bookings are successfully completed?
2. Why are rides cancelled and who cancels more?
3. Which vehicle types generate maximum revenue?
4. Which payment methods are most preferred?
5. Who are the top customers by ride frequency?
6. How satisfied are customers and drivers?

Each question is answered using **SQL views + Power BI + Streamlit outputs**.

---

## 🧮 SQL Business Logic

All KPIs are calculated at the **database level** using SQL views for:
- Performance
- Scalability
- Single source of truth

Example:
```sql
CREATE VIEW vw_total_successful_bookings AS
SELECT COUNT(*) AS total_successful_bookings
FROM rides
WHERE UPPER(TRIM(booking_status)) = 'SUCCESS';

Click **Commit changes** ✅

---

## 🔥 NEXT STEPS (VERY IMPORTANT)

Ab mujhe bolo:
> **“README done”**

Uske baad main tumhe next ye sab dunga:
1. 🎥 **10–12 minute explanation video script (spoken English)**
2. 🧠 **Interview answers (SQL + Power BI + Streamlit)**
3. 📄 **Internship submission explanation**
4. 🧾 **Resume bullet points**
5. 🔗 **LinkedIn post content**

---

💯 Honest feedback:  
Tumhara project **real company internship level** ka ho gaya hai.  
Ab bas presentation polish karni hai — aur wo hum karwa denge 🚀
