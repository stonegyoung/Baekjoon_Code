-- 코드를 작성해주세요
# 9시 46분
SELECT COUNT(ID) AS COUNT
FROM ECOLI_DATA
WHERE ((GENOTYPE & 15) | 8) IN (9, 12, 13);
# 하위 4비트만 비교 GENOTYPE & 1111, 4번 제외 1,2,3이 101, 100, 001 이어야 함 