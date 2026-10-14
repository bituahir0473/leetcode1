# Write your MySQL query statement below
select employee.name,Bonus .bonus from employee left join Bonus on employee.empId = Bonus.empid where bonus <1000 or Bonus is Null;