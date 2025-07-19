/* Write your PL/SQL query statement below */

SELECT *FROM Patients
where conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%';
