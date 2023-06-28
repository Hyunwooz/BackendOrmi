## SQL 기본 구문 정리

### 기본

```sql
	-- select
	select 식

	-- 기본구조
	select 가져올 칼럼들, from 테이블

	-- 갯수 제한
	select 가져올 칼럼들, from 테이블 limit 숫자

	-- 중복제거
	select distinct 가져올 칼럼들,
	from 테이블

	--select 'hello'+'world' 오류
	select concat('hello','world')
	select 'hello'||'world'

	-- prodcut, 별칭 붙이기
	select
		id as product_id,
		category as product_category,
		name as product_name,
		retail_price as product_retail_price,
		cost as product_cost,
		(retail_price-cost) as procuct_porfit
	from products;

	-- 모든 정보
	select * from users;
	-- 유저의 이메일
	select email from users;

	select id, first_name, last_name, concat(first_name,' ', last_name), email, country from "users";
```

### 연산자

```sql

	!= : 같지 않음
    <> : 같지 않음

	논리 연산
	AND, OR, NOT

	BETWEEN 연산
	BETWEEN a AND b = a이상 b이하
	BETWEEN 20 AND 30 = 20이상 30이하

	IN 연산
	IN A = A안에 값과 일치하는 값을 조회
	IN ('a','b','c', ...) = a이거나 b이거나 c인것 ... 인것들

	-- IN 예제
	select *
	from users
	where id in (1978,4834,37153,49725,61293,63470,74653,80628,84078,41307,44567,45095,60864,97606,9432,20729,21930,33675);

	-- Where
	select * from 테이블 where 조건문;
	-- 예시 테이블 user , first_name이 michale인 레코드만 가져오기
	select * from users where first_name = 'michale';

	LIKE 연산
    대소문자를 안가림
    `%`는 와일드카드

	-- product의 name안에 Young이 포함된 레코드를 조회합니다.
	select *
	from products
	where name like '%Young%';

	-- product의 name이 Hurley 로 시작되는 레코드를 조회합니다.
	select *
	from products
	where name like 'Hurley%';

	-- product의 name이 T-shirt 로 끝나는 레코드를 조회합니다.
	select *
	from products
	where name like '%T-shirt';

	-- 언더바는 한개의 글자를 포함합니다.
	-- 아래 예제는 'Da'로 시작되는 5자의 단어를 조회합니다.
	select distinct first_name
	from users
	where first_name like 'Da___'

	-- NULL 값을 갖는 값(0은 값이 있는 것입니다.)
	IS NULL

	select *
	from order_items
	where shipped_at IS NULL;
	where shipped_at IS NOT NULL;
```

### 내장 함수

```sql
	-- count 함수는 해당 항목 레코드의 개수를 반환하는 함수입니다.
	select count(id)
	from users;
	-- 아래와 같이 중복을 제거해서 카운팅하기도 합니다.
	select count(distinct city)
	from users;

	select sum(retail_price)
	from products

	select avg(cost)
	from products;

	select max(cost), max(retail_price)
	from products;

	select min(cost), min(retail_price)
	from products;

	-- 분산
	select variance(retail_price)
	from products

	-- 표준편차
	select stddev(retail_price)
	from products

	-- 특정 항목을 기준으로 그룹화하여 조회할 수 있습니다.
	select country, count(id)
	from users
	group by country;

	select country, city, count(id)
	from users
	group by country, city;
```

### HAVING, ORDER BY

```sql
	-- HAVING
	-- 그룹화된 데이터에 조건을 부여합니다.
	-- count(id)가 4000이상 인 것

	select
	country,
	count(id) as user_count
	from users
	group by country
	having count(id) >= 4000;

	-- ORDER BY
	-- 오름차순 : ASC(기본, 작은 수에서 큰 수로)생략 가능
	-- 내림차순 : DESC(큰 수에서 작은 수로)
	select *
	from users
	order by age;

	select *
	from users
	order by age desc, first_name;

	select *
	from users
	order by created_at desc
	limit 10

```

### 작성 순서

1. from
2. where
3. group by
4. having
5. select
6. order by
7. limit

```sql
	select country, count(id) as user_count
	from users
	where age <= 20
	group by country
	having count(id) >= 500
	order by user_count desc
	limit 5;
```

### 숫자 함수

```sql
-- 숫자 함수
-- round 함수는 해당 항목 레코드의 숫자를 반올림하여 출력하는 함수입니다.
select round(반올림할 숫자, 자릿수);

-- trunc 함수는 해당 항목 레코드의 숫자를 내림(절삭)하여 출력하는 함수입니다.
select trunc(숫자, 자릿수)

-- mod 함수는 해당 항목 레코드의 숫자를 나누기하여 나머지를 출력하는 함수입니다.
select mod(숫자,나눌값)

-- power 함수는 해당 항목 레코드의 숫자를 제곱하여 출력하는 함수입니다.
select power(숫자,승수)

-- sqrt 함수는 해당 항목 레코드의 제곱근을 출력하는 함수입니다.
select sqrt(숫자)


```

### 문자열 함수

```sql
-- substr 문자열의 일부만 출력할 수 있습니다.  substr == substring
select substr(문자열, 시작 위치, 길이)

-- left 문자열을 왼쪽에서 얼만큼 자를 지 설정한 후에 조회할 수 있습니다.
select left(문자열,길이)

-- right 문자열을 왼쪽에서 얼만큼 자를 지 설정한 후에 조회할 수 있습니다.
select right(문자열,길이)

-- concat 여러 문자열을 하나로 연결할 수 있습니다.
select concat('paul', '-', 'lab')

-- lower 문자열을 모두 소문자로 변경합니다.
select lower('Abc')

-- upper 문자열을 모두 대문자로 변경합니다.
select upper('abc')

-- initcap 앞에 문자만 대문자로 만들어 줍니다.
select initcap('abcde')

-- replace 바꾸고 싶은 값으로 대상 값을 교체합니다.
select replace('hello world', 'world', 'sql')

-- length 문자열의 길이를 출력합니다. count 비교해서 기억해주세요.
select length('hello world')

-- POSITION 문자열의 위치를 구합니다. 여기서 INDEX는 1부터 시작합니다. 찾는 문자가 없을 경우 0을 반환합니다.
select POSITION('b' IN 'abcdef');

-- coalesce은 해당 컬럼에 NULL값이 있는 경우 다른 값으로 채워넣을 수 있습니다.
select coalesce(name, '담당자 지정 안됨')
from weniv_event

-- ascii 아스키코드 번호로 리턴하는 함수입니다.
select ascii('A');


```

### 형변환

```sql
-- CAST(데이터 AS 타입명)
-- 데이터::타입명

-- 문자열 -> 숫자로 바꾸는거
-- 문자열 -> 자연수(INTEGER)
-- 문자열 -> FLOAT

select CAST('123' AS INT);
select '123' + '123' # 에러;
select CAST('123' AS INT) + CAST('123' AS INT);
select CAST('123.123' AS FLOAT);

-- 숫자형 (정수,실수)
select CAST('123' AS NUMERIC);
select CAST('123.123' AS NUMERIC);

-- 형변환 다른 문법
select '123'::INT;
select '123.123'::NUMERIC;
select '123.123'::TEXT;

-- 숫자(INTEGER) -> 문자
-- 숫자(FLOAT) -> 문자
-- true, false -> 문자

select CAST(123 AS TEXT)
select CAST(123.123 AS TEXT)
select CAST(true AS TEXT)
select CAST(false AS TEXT)
select CAST(NULL AS TEXT)

-- 형변환 다른 문법
select 123::TEXT;
select 123.123::TEXT;
select true::TEXT;
```

### 날짜 함수

```sql
-- 1) DATE
-- 문자열 -> DATE
-- 2) DATETIME
-- 문자열 -> DATETIME

select DATE('2011-12-01 11:12:34')

SELECT '2011-12-01 11:12:34'::DATE;
SELECT '2011-12-01 11:12:34'::TIME;
SELECT '2011-12-01 11:12:34'::TIMESTAMP;

-- 현재 날짜,시간 구하기
SELECT CURRENT_DATE;
select current_timestamp;
select now();

-- 형변환 다른 문법
select '2023-1-1'::DATE

-- 예제
select created_at::DATE
from users

-- 날짜에서 YEAR,MONTH,DAY 뽑기
SELECT EXTRACT(YEAR FROM DATE '2023-1-1');
SELECT EXTRACT(MONTH  FROM DATE '2023-1-1');
SELECT EXTRACT(DAY FROM DATE '2023-1-1');

-- 타임스탬프에서 시간,분,초 뽑기
SELECT EXTRACT(HOUR FROM NOW());
SELECT EXTRACT(MINUTE FROM NOW());
SELECT EXTRACT(SECOND FROM NOW());

-- 응용
-- DATE
SELECT EXTRACT(DAY FROM CURRENT_DATE);

select extract(year from date(created_at))
from users

select extract(month from date(created_at))
from users

select extract(day from date(created_at))
from users

select extract(quarter from date(created_at))
from users

-- TIME
select extract(hour from created_at)
from users

select extract(minute from created_at)
from users

select extract(second from created_at)
from users
```

### 날짜 출력 포맷 변경

```sql
-- TO_CHAR(date_expr, format_string)
SELECT TO_CHAR(DATE '2023-01-25', 'YY/MM/DD') AS KR_format;
SELECT TO_CHAR(DATE '2023-01-25', 'YY-MM-DD') AS KR_format;
SELECT TO_CHAR(TIMESTAMP '2023-01-25 15:30:00', 'YY/MM/DD HH24:MI:SS') AS KR_format;

SELECT  TO_CHAR(created_at, 'YY/MM/DD') AS KR_format
FROM users;

SELECT TO_CHAR(created_at, 'YY-MM-DD') AS KR_format
FROM users;

SELECT TO_CHAR(created_at, 'YY/MM/DD HH24:MI:SS') AS formatted_date
FROM users;
```

### 날짜, 시간 차이 구하기

```sql
select DATE '2023-08-27' - DATE '2023-06-26' AS date_difference;
select '2023-08-27'::DATE - '2023-06-26'::DATE;

select TIME '12:30' - TIME '10:45' AS time_difference;
select TIMESTAMP '2023-06-27 12:30' - TIMESTAMP '2023-06-26 10:45' AS time_difference;

select delivered_at - created_at
from orders
where status = 'Complete'

-- interval 지정된 시간 간격을 추가 및 빼는 함수입니다.
-- DATE + interval

select '2023-1-25'::DATE + interval '5 day';
select '2023-1-25'::DATE - interval '5 day';
select '2023-1-25'::DATE + interval '5 month';
select '2023-1-25'::DATE - interval '5 month';
select '2023-1-25'::DATE + interval '5 year';
select '2023-1-25'::DATE - interval '5 year';

SELECT created_at + INTERVAL '5 DAY'
from users;
SELECT created_at - INTERVAL '5 DAY'
from users;

select NOW() + interval '1 day';
select NOW() - interval '1 day';

SELECT '2023-12-25 15:30:00'::TIMESTAMP + INTERVAL '10 MINUTE'
SELECT '2023-12-25 15:30:00'::TIMESTAMP - INTERVAL '10 MINUTE'

SELECT created_at + INTERVAL '10 minute'
from users
SELECT created_at - INTERVAL '10 minute'
from users
```
