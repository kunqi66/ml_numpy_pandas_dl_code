
SELECT u.university,
COUNT(q.question_id) / COUNT(DISTINCT q.device_id)
AS avf_answer_cnt
FROM user_profile u LEFT JOIN question_practice_detail q
ON u.device_id = q.device_id
GROUP BY u.university;

