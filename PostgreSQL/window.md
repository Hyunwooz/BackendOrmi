## WINDOW 함수

### **분류 1**

1. 탐색 함수 : LEAD, LAG, FIRST_VALUE, LAST_VALUE
2. 번호 지정 함수 : RANK, DENSE_RANK, PERCENT_RANK, CUME_DIST, NTILE
3. 집계 분석 함수 : 집계 함수들, AVG, COUNT, SUM, MAX, MIN

### **분류 2**

-   그룹 내 순위 관련 함수(RANKING FAMILY)
    -   RANK, DENSE_RANK, ROW_NUMBER
-   그룹 내 집계 관련 함수(WINDOW AGGREGATE FAMILY)
    -   SUM, MAX, MIN, AVG, COUNT
-   그룹 내 행 순서 관련 함수
    -   LAG, LEAD, FIRST_VALUE, LAST_VALUE, NTH_VALUE
-   그룹 내 비율 관련 함수
    -   CUME_DIST, PERCENT_RANK, NTILE

### **문법**

-   함수 이름(컬럼, OFFSET) OVER (PARTITION BY 파티션*컬럼 ORDER BY 정렬*컬럼)
    -   OFFSET : 값을 가져올 행의 위치. 기본 값은 1이고 생략 가능
-   함수 이름(컬럼) OVER (PARTITION BY 파티션*컬럼 ORDER BY 정렬*컬럼)
-   필요에 따라 PARTITION BY는 생략 가능

RANK() OVER (ORDER BY 기준칼럼)
RANK() OVER ( PARTITION by 특정영역(값) ORDER BY created_at) AS rank_created_at

### **2.1 RANK()**

파티션 내에서 현재 행의 순위를 부여한다. 동일 값인 경우 동일 순위가 부여되고, 다음 순위는 동일값의 수만큼 건너뛰어 부여된다.

### **2.2 DENSE_RANK()**

파티션 내에서 현재 행의 순위를 부여한다. 동일 값인 경우 동일 순위가 부여되고, 다음 순위는 건너뛰지 않고 순차 번호로 부여 된다.

### 예시

```sql
select
  id,
  first_name,
  last_name,
  country,
  created_at,
  age,
  RANK() OVER ( PARTITION by country ORDER BY created_at) AS rank_created_at
from users
where id between 1 and 20
order by country, age
```

### Raking With Group By

```sql
select
  user_id,
  sum(sale_price) as total
from order_items
group by user_id
```

LAG는 이전 행의 필드를 읽고, LEAD는 다음 행의 필드를 읽습니다.

```sql
select
  id,
  first_name,
  last_name,
  lag(id) over(order by id) as id_prev,
  lead(id) over(order by id) as id_next
 from users
 where id in (1,2,3,4,5)
 order by id
```

날짜 차이 구하기

```sql
select
  id,
  user_id,
  created_at,
  lag(created_at) over(order by created_at) as created_at_prev,
  extract('epoch' from  created_at - (lag(created_at) over(order by created_at))) as prev_visit_second
 from events
 where user_id = 16006
 order by created_at
```

### 3.2 FIRST_VALUE, LAST_VALUE

FIRST_VALUE은 그룹 내의 첫값을 구하고, LAST_VALUE는 마지막 값을 구합니다.

단, LAST_VALUE는 지금까지 읽은 행의 집합을 의미하기 때문에 항상 자기 자신입니다.

전체 그룹에 대한 마지막 값을 구하려면 ROWS 옵션을 주어야 합니다.

```sql
select
  country_name,
  refresh_date,
  FIRST_VALUE(confirmed) OVER (PARTITION BY country_name ORDER BY confirmed) as first,
  LAST_VALUE(confirmed) OVER (PARTITION BY country_name ORDER BY confirmed) as mid,
  LAST_VALUE(confirmed) OVER (PARTITION BY country_name ORDER BY confirmed ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as last
from world_covid
ORDER BY country_name
```

-   ROW : 부분집합인 윈도우 크기를 물리적인 단위로 행 집합을 지정
-   UNBOUNDED PRECEDING : 윈도우의 시작 위치가 첫번째 ROW
-   UNBOUNDED FOLLOWING : 윈도우의 마지막 위치가 마지막 ROW
-   N PRECEDING : N번째 앞행
-   N FOLLOWING : N번째 뒤행

### 3.3 NTH_VALUE

현재 윈도우 프레임에 있는 N번째 행의 값을 반환합니다. 이 행이 없으면 NULL을 반환합니다.

```sql
SELECT
  id,
  email,
  created_at,
  NTH_VALUE(email, 5) OVER( ORDER BY id ) AS fifth_signup_user_email,
  NTH_VALUE(created_at, 5) OVER( ORDER BY id ) AS fifth_signup_user_created_at
FROM users

-- 각 제품의 브랜드별 1~3번 까지 제품ID 조회
select
  id,
  name,
  brand,
  category,
  retail_price,
  NTH_VALUE(id, 1) OVER (PARTITION BY brand ORDER BY retail_price desc) as first,
  NTH_VALUE(id, 2) OVER (PARTITION BY brand ORDER BY retail_price desc) as second,
  NTH_VALUE(id, 3) OVER (PARTITION BY brand ORDER BY retail_price desc) as third
from products
where brand IS NOT NULL
```

### 3.2 그룹 내 비율 관련 함수

**3.2.1 PERCENT_RANK()**

현재 행의 상대적 순위를 반환한다.

계산에 따라 0과 1사이의 범위에서 행의 백분율 순위를 계산한다.

```sql
select
  id,
  name,
  cost,
  PERCENT_RANK() OVER (ORDER BY cost) as percent_rank
from products
order by percent_rank
```

**3.2.2 CUME_DIST() - 누적분포**

**cumulative distribution**

-   0보다 크고 1보다 작거나 같은 값이 나옴.
-   n보다 값이 정렬순으로 이전이거나 같은 행의 갯수 / 현재 window 또는 파티션의 row 개수

```sql
select value,
  cume_dist() over(
    order by value
  ) cumulative_distribution
from value_list;
```

**3.2.3 NTILE(n)**

레코드의 집합을 n개의 영역으로 구분하고 소속 영역을 구한다. 인수 n은 나눌 영역의 개수를 지정한다.

```sql
-- ntile_number_age_section : 유저의 나이 4그룹으로 나누기
select
  id,
  first_name,
  last_name,
  country,
  age,
  NTILE(4) OVER ( ORDER BY age ) AS ntile_number_age_section
from users
where id between 1 and 20
order by age
```

### 4.1 SUM(value)

파티션별 윈도우 내에서 지정된 value의 합을 계산한다.

#### order_items에서 각 유저의 구매액 누적합계

```sql
SELECT
  id,
  order_id,
  user_id,
  product_id,
  ROUND(sale_price,2) as sale_price,
  ROUND(SUM(sale_price)
    OVER(
      PARTITION BY user_id
      ORDER BY created_at
      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
  , 2) AS cumulative_sum_amount
FROM order_items
ORDER BY user_id, created_at
```

#### 최근 30일 합계만 보고 싶을때

```sql
select
  value,
  sum(value) over( order by value ROWS BETWEEN 29 PRECEDING AND CURRENT ROW) as total
from value_list
order by id
```
