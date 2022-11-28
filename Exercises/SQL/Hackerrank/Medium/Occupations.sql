SELECT ods.name,ops.name,oss.name,oas.name 
FROM
    (SELECT name, 
        (SELECT COUNT(DISTINCT name)+1 FROM occupations od2
       WHERE od2.name < od1.name AND od2.occupation = od1.occupation) As rw
       FROM occupations od1 WHERE occupation = "Doctor" ORDER BY name ASC) As ods
RIGHT OUTER JOIN
(SELECT name, 
      (SELECT COUNT(DISTINCT name)+1 FROM occupations od2
       WHERE od2.name < od1.name AND od2.occupation = od1.occupation) As rw
       FROM occupations od1 WHERE occupation = "Professor" ORDER BY name ASC) As ops
ON ods.rw = ops.rw
LEFT OUTER JOIN
(SELECT name, 
      (SELECT COUNT(DISTINCT name)+1 FROM occupations od2
       WHERE od2.name < od1.name AND od2.occupation = od1.occupation) As rw
       FROM occupations od1 WHERE occupation = "Singer" ORDER BY name ASC) AS oss
ON ops.rw = oss.rw
LEFT OUTER JOIN
(SELECT name, 
      (SELECT COUNT(DISTINCT name)+1 FROM occupations od2
       WHERE od2.name < od1.name AND od2.occupation = od1.occupation) As rw
       FROM occupations od1 WHERE occupation = "Actor" ORDER BY name ASC) AS oas
ON ops.rw = oas.rw;
