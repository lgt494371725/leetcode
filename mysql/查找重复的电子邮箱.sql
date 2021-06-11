笨办法
select distinct p1.Email 
from Person p1,Person p2
where p1.Id != p2.Id and p1.Email = p2.Email 
简单的
select Email from Person
group by Email
having count(*)>1

