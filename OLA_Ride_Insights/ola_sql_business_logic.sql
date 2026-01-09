/* ============================================================
   PROJECT: OLA RIDES DATA ANALYSIS
   AUTHOR : Zishan Alam
   PURPOSE: Booking performance, cancellations, revenue,
            customer & driver behavior analysis
   DATABASE: PostgreSQL
   ============================================================ */


/* ============================================================
   SECTION 2: BUSINESS VIEWS (DASHBOARD READY)
   ============================================================ */

-- View 1: Total successful bookings
select * from vw_total_successful_bookings;

CREATE OR REPLACE VIEW vw_total_successful_bookings AS
SELECT
    COUNT(*) AS total_successful_bookings
FROM rides
WHERE UPPER(TRIM("Booking_Status")) = 'SUCCESS';

-- View 2: Total cancellations by customers
select * from vw_customer_cancellations;

CREATE OR REPLACE VIEW vw_customer_cancellations AS
SELECT
    COUNT(*) AS cancelled_by_customer
FROM rides
WHERE "Booking_Status" ILIKE '%customer%';


-- View 3: Driver cancellation reasons distribution
select * from vw_driver_cancellation_reasons;

CREATE OR REPLACE VIEW vw_driver_cancellation_reasons AS
SELECT
    "Canceled_Rides_by_Driver" AS cancellation_reason,
    COUNT(*) AS total_cancellations
FROM rides
WHERE "Canceled_Rides_by_Driver" IS NOT NULL
GROUP BY "Canceled_Rides_by_Driver";


-- View 4: Top 5 customers by total rides
select * from vw_top_5_customers;

CREATE OR REPLACE VIEW vw_top_5_customers AS
SELECT
    "Customer_ID",
    COUNT("Booking_ID") AS total_rides
FROM rides
GROUP BY "Customer_ID"
ORDER BY total_rides DESC
LIMIT 5;


-- View 5: Average ride distance by vehicle type
select * from vw_avg_distance_by_vehicle;

CREATE OR REPLACE VIEW vw_avg_distance_by_vehicle AS
SELECT
    "Vehicle_Type",
    ROUND(AVG(ride_distance_num), 2) AS avg_ride_distance
FROM rides
GROUP BY "Vehicle_Type";


-- View 6: Driver rating range for Prime Sedan
select * from vw_prime_sedan_driver_ratings;

CREATE OR REPLACE VIEW vw_prime_sedan_driver_ratings AS
SELECT
    MAX(driver_ratings_num) AS max_driver_rating,
    MIN(driver_ratings_num) AS min_driver_rating
FROM rides
WHERE "Vehicle_Type" = 'Prime Sedan';


-- View 7: Average customer rating by vehicle type
select * from vw_avg_customer_rating_by_vehicle;

CREATE OR REPLACE VIEW vw_avg_customer_rating_by_vehicle AS
SELECT
    "Vehicle_Type",
    ROUND(AVG(customer_rating_num), 2) AS avg_customer_rating
FROM rides
GROUP BY "Vehicle_Type";


-- View 8: Total revenue from successful bookings
select * from vw_total_successful_revenue;

CREATE OR REPLACE VIEW vw_total_successful_revenue AS
SELECT
  SUM(booking_value_num) AS total_successful_value
FROM rides
WHERE TRIM(UPPER("Booking_Status")) = 'SUCCESS';

-- View 9: Incomplete rides with reasons
select * from vw_incomplete_rides_reasons;

CREATE OR REPLACE VIEW vw_incomplete_rides_reasons AS
SELECT
    "Booking_ID",
    "Incomplete_Rides_Reason"
FROM rides
WHERE UPPER(TRIM("Incomplete_Rides")) = 'YES';


-- View 10: Payment method distribution
select * from vw_payment_method_distribution;

CREATE OR REPLACE VIEW vw_payment_method_distribution AS
SELECT
    "Payment_Method",
    COUNT(*) AS total_transactions
FROM rides
GROUP BY "Payment_Method";


/* ============================================================
   END OF PROJECT
   ============================================================ */

---Retrieve all successful bookings
SELECT *
FROM rides
WHERE LOWER("Booking_Status") = 'success';


---Find the average ride distance for each vehicle type
SELECT
  "Vehicle_Type",
  AVG(ride_distance_num) AS avg_distance
FROM rides
GROUP BY "Vehicle_Type";

--Get the total number of cancelled rides by customers
SELECT COUNT(*)
FROM rides
WHERE TRIM("Booking_Status") = 'Canceled by Customer';

---List the top 5 customers who booked the highest number of rides
SELECT 
  "Customer_ID",
  COUNT("Booking_ID") AS total_rides
FROM rides
GROUP BY "Customer_ID"
ORDER BY total_rides DESC
LIMIT 5;

--Get the number of rides cancelled by drivers due to personal and car-related issues

SELECT COUNT(*)
FROM rides
WHERE "Canceled_Rides_by_Driver" ILIKE '%personal%'
  AND "Canceled_Rides_by_Driver" ILIKE '%car%';

SELECT DISTINCT "Canceled_Rides_by_Driver"
FROM rides;

SELECT COUNT(*)
FROM rides
WHERE TRIM("Canceled_Rides_by_Driver") = 'Personal & Car related issue';

--Find the maximum and minimum driver ratings for Prime Sedan bookings

SELECT
  MAX(driver_ratings_num) AS max_rating,
  MIN(driver_ratings_num) AS min_rating
FROM rides
WHERE "Vehicle_Type" = 'Prime Sedan';

--Retrieve all rides where payment was made using UPI
SELECT *
FROM rides
WHERE "Payment_Method" = 'UPI';

--Find the average customer rating per vehicle type

SELECT
  "Vehicle_Type",
  ROUND(AVG(customer_rating_num), 2) AS avg_customer_rating
FROM rides
GROUP BY "Vehicle_Type";

--Calculate the total booking value of rides completed successfully:

SELECT
  SUM(booking_value_num) AS total_successful_value
FROM rides
WHERE "Booking_Status" = 'Success';

 --List all incomplete rides along with the reason

SELECT
  "Booking_ID",
  "Incomplete_Rides_Reason"
FROM rides
WHERE "Incomplete_Rides" = 'Yes';

