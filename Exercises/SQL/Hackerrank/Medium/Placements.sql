with friend_table as (
    Select friend_id as id_of_friend, salary as salary_of_friend
    from friends
    join packages on friend_id = packages.id
    ),
    join_table as (
    select friends.id as id, friend_id, salary
    from friends
    join packages on friends.id = packages.id
    )
select name 
from students
join join_table on students.id = join_table.id
join friend_table on friend_table.id_of_friend = join_table.friend_id
where salary_of_friend > salary
order by salary_of_friend;
