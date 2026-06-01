

SELECT q.device_id,q.question_id,q.result
FROM question_practice_detail  q 
INNER JOIN user_profile  u
ON q.device_id = u.device_id
WHERE u.university = '浙江大学';

SELECT *
FROM question_practice_detail qpd 
INNER JOIN user_profile up
ON qpd.device_id = up.device_id
WHERE qpd.question_id = 111 and qpd.result = 'right';

SELECT *
FROM question_practice_detail q
INNER JOIN user_profile u
on q.device_id = u.device_id
WHERE u.university = '北京大学' and u.gender='female';

SELECT
    device_id, gender, age, gpa
FROM user_profile
WHERE gender='male';
