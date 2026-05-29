SELECT u.device_id,u.gender,u.age
FROM user_profile u
WHERE u.age >= 20 and u.age <= 23;

SELECT u.device_id,u.gender,u.age,u.university
FROM user_profile u
WHERE u.university <> '复旦大学';

SELECT u.device_id,u.gender,u.age,u.university
FROM chapter6db1.user_profile u
WHERE u.age is not NULL;


use chapter6db2;
SELECT u.device_id,u.gender,u.age,u.university,u.gpa
FROM user_profile u
WHERE u.gpa > 3.5 and gender = 'male';

SELECT u.device_id,u.gender,u.age,u.university,u.gpa
FROM user_profile u
WHERE u.university = '北京大学' AND u.gpa > 3.7;

SELECT u.device_id,u.gender,u.age,u.university,u.gpa
FROM user_profile u
WHERE u.university IN ('北京大学','复旦大学','山东大学');

SELECT u.device_id,u.gender,u.age,u.university,u.gpa
FROM user_profile u
WHERE (u.university = '复旦大学' and u.gpa >3.8) or (u.university = '山东大学' and u.gpa > 3.5);

SELECT u.device_id,u.age,u.university
FROM user_profile u
WHERE u.university LIKE('%北京%');