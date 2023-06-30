## 1. INSERT

테이블에 새 레코드를 삽입할 때 사용합니다.

```sql

INSERT INTO weniv_product (삽입할 열 이름1, 삽입할 열 이름2, ... )
VALUES (값1, 값2, ... );

INSERT INTO weniv_product (id, name, cost)
VALUES (11, 'mouse', 20000);

INSERT INTO weniv_product (id, name, cost)
VALUES (11, 'mouse', 20000);
```

## 2. UPDATE

조건에 맞는 기존 레코드를 수정할 수 있습니다. where로 여러개를 select하여 바꿀 수 있습니다.

```sql
UPDATE 테이블명
SET 컬럼명1 = 값1, 컬럼명2 = 값2, ...
WHERE 조건;

-- 하나의 레코드 업데이트
UPDATE weniv_product
SET cost = 210000
WHERE id = 1;

-- 여러개의 레코드 업데이트
UPDATE weniv_product
SET cost = cost + 500
WHERE cost < 1000;

-- 모든 레코드 업데이트
UPDATE weniv_product
SET cost = 50000
```

## 3. DELETE

기존 레코드를 삭제합니다.

```sql
-- 하나의 레코드 삭제
DELETE FROM weniv_product
WHERE id = 11;

-- 여러개의 레코드 삭제
DELETE FROM weniv_product
WHERE id = 11;

-- 모든 레코드 삭제
DELETE FROM weniv_product
```

## CREATE_TABLE

새 테이블 생성 - `customers`

```sql
데이터베이스에 새 테이블을 생성합니다. 테이블의 열 이름과 그에 맞는 데이터 타입(varchar, int, datetime 등)을 지정합니다.

CREATE TABLE 테이블명(
	컬럼명1 데이터_타입 [primary key],
	컬럼명2 데이터_타입
);

CREATE TABLE customers (
	customer_id serial PRIMARY KEY,
	name VARCHAR UNIQUE,
	email VARCHAR NOT NULL,
	active bool NOT NULL DEFAULT TRUE
);

customers 고객 이름(name)이 테이블에 있으면 그냥 무시(아무것도 하지 않음)합니다.

INSERT INTO customers (name, email)
VALUES('Microsoft','hotline@microsoft.com')
ON CONFLICT (name)
DO NOTHING;

해당 name이 존재하면 update를 합니다.

INSERT INTO customers (name, email)
VALUES('Microsoft','hotline@microsoft.com')
ON CONFLICT (name)
DO
   UPDATE SET email = EXCLUDED.email || ';' || customers.email;
```

## 2. ALTER TABLE

기존 테이블에 다양한 제약조건을 추가, 수정, 삭제합니다.

```sql
ALTER TABLE 테이블명
ADD 컬럼명 데이터_타입;

-- phone이라는 컬럼명을 추가하도록 하겠습니다.
ALTER TABLE sample_table
ADD phone VARCHAR(11);
```
