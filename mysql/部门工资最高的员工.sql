select d.Name as Department, e.Name as Employee, Salary
from Employee e
join Department d on e.DepartmentId = d.Id 
where (e.DepartmentId , Salary) in 
    (
        select DepartmentId,max(Salary)
        from Employee
        group by DepartmentId
    );
