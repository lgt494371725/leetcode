select s1.Score as Score,
(select count(distinct s2.Score)+1 from scores s2 where s2.score>s1.score) as `Rank`
from scores s1
order by s1.score desc