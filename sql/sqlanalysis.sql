SELECT SUM(Quantity * Price) AS Total_Revenue
FROM cleaned_data;

SELECT [Customer ID], SUM(Quantity * Price) AS Revenue
FROM cleaned_data
GROUP BY [Customer ID]
ORDER BY Revenue DESC;

SELECT Country, SUM(Quantity * Price) AS Revenue
FROM cleaned_data
GROUP BY Country
ORDER BY Revenue DESC;

SELECT 
    YEAR(InvoiceDate) AS Year,
    MONTH(InvoiceDate) AS Month,
    SUM(Quantity * Price) AS Revenue
FROM cleaned_data
GROUP BY YEAR(InvoiceDate), MONTH(InvoiceDate)
ORDER BY Year, Month;