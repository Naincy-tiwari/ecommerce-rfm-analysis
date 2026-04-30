-- =========================================
-- E-COMMERCE SALES SQL ANALYSIS
-- =========================================

-- Assumed table name: retail
-- Columns: Invoice, StockCode, Description, Quantity, InvoiceDate, Price, Customer_ID, Country


-- =========================================
-- 1. TOTAL REVENUE BY COUNTRY
-- =========================================
SELECT 
    Country,
    SUM(Quantity * Price) AS Total_Revenue
FROM retail
GROUP BY Country
ORDER BY Total_Revenue DESC;


-- =========================================
-- 2. TOP 10 CUSTOMERS BY REVENUE
-- =========================================
SELECT 
    Customer_ID,
    SUM(Quantity * Price) AS Total_Spending
FROM retail
GROUP BY Customer_ID
ORDER BY Total_Spending DESC
LIMIT 10;


-- =========================================
-- 3. MONTHLY REVENUE TREND
-- =========================================
SELECT 
    strftime('%Y-%m', InvoiceDate) AS Month,
    SUM(Quantity * Price) AS Monthly_Revenue
FROM retail
GROUP BY Month
ORDER BY Month;


-- =========================================
-- 4. TOP 10 SELLING PRODUCTS
-- =========================================
SELECT 
    Description,
    SUM(Quantity) AS Total_Quantity_Sold
FROM retail
GROUP BY Description
ORDER BY Total_Quantity_Sold DESC
LIMIT 10;


-- =========================================
-- 5. AVERAGE ORDER VALUE
-- =========================================
SELECT 
    AVG(Quantity * Price) AS Avg_Order_Value
FROM retail;


-- =========================================
-- 6. TOTAL ORDERS PER CUSTOMER
-- =========================================
SELECT 
    Customer_ID,
    COUNT(DISTINCT Invoice) AS Total_Orders
FROM retail
GROUP BY Customer_ID
ORDER BY Total_Orders DESC;


-- =========================================
-- 7. REVENUE BY COUNTRY (TOP 5)
-- =========================================
SELECT 
    Country,
    SUM(Quantity * Price) AS Revenue
FROM retail
GROUP BY Country
ORDER BY Revenue DESC
LIMIT 5;


-- =========================================
-- 8. CUSTOMER SEGMENT COUNT (RFM)
-- =========================================
-- (Works if you have rfm_segments table)
SELECT 
    Segment,
    COUNT(*) AS Total_Customers
FROM rfm_segments
GROUP BY Segment
ORDER BY Total_Customers DESC;


-- =========================================
-- 9. HIGH VALUE CUSTOMERS (SPENDING > 1000)
-- =========================================
SELECT 
    Customer_ID,
    SUM(Quantity * Price) AS Total_Spending
FROM retail
GROUP BY Customer_ID
HAVING Total_Spending > 1000
ORDER BY Total_Spending DESC;


-- =========================================
-- 10. DAILY REVENUE TREND
-- =========================================
SELECT 
    DATE(InvoiceDate) AS Date,
    SUM(Quantity * Price) AS Daily_Revenue
FROM retail
GROUP BY Date
ORDER BY Date;
