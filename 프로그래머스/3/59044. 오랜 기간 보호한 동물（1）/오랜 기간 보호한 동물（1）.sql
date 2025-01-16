-- 코드를 입력하세요
# 8:49
SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS AS I LEFT JOIN ANIMAL_OUTS AS O 
    ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.NAME IS NULL AND I.NAME IS NOT NULL
ORDER BY I.DATETIME ASC
LIMIT 3
;