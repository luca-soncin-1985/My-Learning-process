SELECT n,
    case 
        when n IN(select p FROM bst) AND p is null then 'Root'
        when n IN(select p FROM bst) then 'Inner'
        else 'Leaf'
    end as Type
FROM bst b
ORDER BY n;
        
