## SQL 기본 구문 정리

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

	같지않음 연산자

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
