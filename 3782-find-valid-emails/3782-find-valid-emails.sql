select *from Users
where REGEXP_LIKE(email, '^[A-Za-z0-9_]*@[A-Za-z]*\.com$')