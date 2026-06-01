SELECT u.university ,qd.difficult_level,
COUNT(qp.question_id) / COUNT(DISTINCT qp.device_id)
AS avg_answer_cnt
FROM user_profile u LEFT JOIN question_practice_detail qp
ON u.device_id = qp.device_id
LEFT JOIN question_detail qd ON qp.question_id =  qd.question_id
WHERE qd.difficult_level is not NULL
GROUP BY u.university,qd.difficult_level;

