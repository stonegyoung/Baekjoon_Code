-- 코드를 입력하세요
# 2:41
SELECT CAR_ID, CAR_TYPE, DAILY_FEE, OPTIONS
FROM CAR_RENTAL_COMPANY_CAR
WHERE FIND_IN_SET('네비게이션', OPTIONS) # 'A,B,C' 형태로 되어 있을 때 찾음
# WHERE OPTIONS LIKE '%네비게이션%'
ORDER BY CAR_ID DESC;