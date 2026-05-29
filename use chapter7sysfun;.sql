/*use chapter7db1;
SELECT MAX(u.gpa)
FROM user_profile u
WHERE u.university = '复旦大学';

use chapter7db2;
SELECT COUNT(*) as male_num,ROUND(AVG(u.gpa),1)
FROM user_profile u
WHERE u.gender = 'male';

use chapter7db3;
SELECT u.device_id,u.gender,
CASE 
    WHEN u.age < 20 THEN  '20岁以下'
    WHEN u.age >= 20 and u.age < 24 THEN '20到24岁'
    ELSE  '其他'
END
FROM user_profile u;
*/
SELECT MONTH(date),COUNT(DISTINCT device_id),COUNT(id)
FROM question_practice_detail
WHERE MONTH(date) = 8
GROUP BY MONTH(date);
