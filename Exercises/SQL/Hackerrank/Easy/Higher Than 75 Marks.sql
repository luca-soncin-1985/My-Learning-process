SELECT name
FROM students
WHERE marks > 75
ORDER by RIGHT(name, 3) ASC, id ASC;
