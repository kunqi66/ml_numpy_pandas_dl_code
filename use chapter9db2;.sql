

SELECT u.university,AVG(u.question_cnt) AS avg_question_cnt,
AVG(u.answer_cnt) AS avg_answer_cnt
FROM user_profile u
GROUP BY u.university
HAVING avg_question_cnt < 5
OR avg_answer_cnt < 20;

