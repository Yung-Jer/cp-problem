# Write your MySQL query statement below
select (select distinct salary from Employee order by salary desc limit 1 offset 1) as SecondHighestSalary;

# Or (Suggested Answer)

SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary;