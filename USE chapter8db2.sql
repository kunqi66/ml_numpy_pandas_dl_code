SELECT qd.id,qpd.device_id,qpd.question_id,qpd.result
FROM question_detail qd LEFT JOIN question_practice_detail qpd
ON qd.question_id = qpd.question_id
WHERE qd.difficult_level = 'hard';

SELECT up.*
FROM user_profile up LEFT JOIN question_practice_detail qpd
ON up.device_id = qpd.device_id
LEFT JOIN question_detail qd
ON qpd.question_id = qd.question_id
WHERE qd.difficult_level='hard' AND qpd.result='right';

SELECT COUNT(DISTINCT up.id)
FROM user_profile up 
LEFT JOIN question_practice_detail qpd
ON up.device_id = qpd.device_id
LEFT JOIN question_detail qd
ON qpd.question_id=qd.question_id
WHERE qd.difficult_level = 'easy' AND qpd.result='wrong';

