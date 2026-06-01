SELECT u.university,AVG(u.question_cnt) AS avg_question_cnt
FROM user_profile u
GROUP BY u.university
ORDER BY avg_question_cnt;

SELECT u.gender,u.university,
COUNT(id) AS user_num, AVG(u.question_cnt) AS avg_question_cnt,
AVG(u.answer_cnt) AS avg_answer_cnt
FROM user_profile u
GROUP BY u.gender,u.university
