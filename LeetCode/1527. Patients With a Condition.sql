# https://leetcode.com/problems/patients-with-a-condition/description/
# 맨 처음부터 DIAB1 이 들어있는 것 + 단어 이후에 DIAB1 으로 시작하는 것 두가지 경우를 모두 찾아야 함

# Write your MySQL query statement below
SELECT patient_id, patient_name, conditions
FROM patients
WHERE conditions LIKE "% DIAB1%" OR conditions LIKE "DIAB1%"
