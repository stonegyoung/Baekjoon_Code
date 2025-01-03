-- 코드를 입력하세요
# 4:00
SELECT BOOK_ID, AUTHOR_NAME, 
    DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK INNER JOIN AUTHOR USING(AUTHOR_ID)
WHERE BOOK.CATEGORY = '경제'
ORDER BY PUBLISHED_DATE ASC
;