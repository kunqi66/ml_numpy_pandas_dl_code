SELECT DISTINCT u.university AS 大学 FROM user_profile u;
SELECT u.device_id AS user_infos_example FROM user_profile u;
SELECT u.device_id, u.university FROM user_profile AS u WHERE u.university = '北京大学';
SELECT u.device_id, u.gender, u.age, u.university FROM user_profile AS u WHERE u.age > 24;
SELECT u.device_id,u.gender,u.age,u.university FROM user_profile u;
SELECT * FROM user_profile;
SELECT * FROM user_profile u WHERE u.province = 'shanghai';
SELECT u.device_id,u.age,u.university FROM user_profile u WHERE u.gender = 'male';
SELECT DISTINCT u.province FROM user_profile u

 