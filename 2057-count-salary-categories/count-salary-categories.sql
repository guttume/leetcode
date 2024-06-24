# Write your MySQL query statement below
SELECT "Low Salary" as category, count(1) as accounts_count FROM Accounts WHERE income < 20000
UNION
SELECT "Average Salary" as category, count(1) as accounts_count FROM Accounts WHERE income <= 50000 and income >= 20000
UNION
SELECT "High Salary" as category, count(1) as accounts_count FROM Accounts WHERE income > 50000