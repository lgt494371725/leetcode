select class from courses
group by class
having count(distinct student)>=5
-- 因为有可能出现学生记录重复的情况