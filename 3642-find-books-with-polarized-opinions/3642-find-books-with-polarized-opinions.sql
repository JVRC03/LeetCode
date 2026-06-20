select 
b.book_id, b.title, b.author, b.genre, b.pages, MAX(r.session_rating) - MIN(session_rating) as rating_spread, ROUND((count(*) - (select count(*) from reading_sessions where session_rating = 3 and book_id = b.book_id)) / count(*), 2) as polarization_score
from books as b
inner join reading_sessions as r
on b.book_id = r.book_id
group by r.book_id
having count(*) > 4 and polarization_score >= 0.6 and min(session_rating) <= 2 and max(session_rating) >= 4
order by polarization_score desc, b.title desc;