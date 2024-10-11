### Database

체계적인 데이터 모음

데이터 : 저장이나 처리에 효율적인 형태로 변환된 정보

데이터베이스 역할 : 데이터를 저장하고 조작(CRUD)

[기존의 데이터 저장 방식]

- 파일(File) 이용
    
    어디에서나 쉽게 사용 가능
    
    데이터를 구조적으로 관리하기 어려움
    
- 스프레드 시트(Spreadsheet) 이용
    
    테이블의 열과 행을 사용해 데이터를 구조적으로 관리 가능
    
    크기의 한계 - 일반적으로 약 100만 행까지만 저장가능
    
    보안의 한계 - 단순히 파일이나 링크 소유 여부에 따른 단순한 접근 권한 기능 제공
    

### 관계형 데이터베이스(Relational Database)

데이터 간에 관계가 있는 데이터 항목들의 모음

- 테이블, 행, 열의 정보를 구조화하는 방식
- 서로 관련된 데이터 포인터를 저장하고 이에 대한 액세스를 제공
- 관계로 인해 두 테이블을 사용하여 데이터를 다양한 형식으로 조회할 수 있음

관계 : 여러 테이블 간의 (논리적) 연결

[관계형 데이터베이스 관련 키워드]

- Table(Relation) : 데이터를 기록하는 곳
- Field(Column, Attribute) : 각 필드에는 고유한 데이터 형식(타입)이 저장됨
- Record(Row, Tuple) : 각 레코드에는 구체적인 데이터 값이 저장됨
- Database(Schema) : 테이블의 집합
- Primary Key(기본 키, PK) : 각 레코드의 고유한 값, 레코드의 식별자로 활용
- Foreign Key(외래 키, FK) : 테이블의 필드 중 다른 레이블의 레코드를 식별할 수 있는 키, 다른 테이블의 기본 키를 참조, 각 레코드에서 서로 다른 테이블 간의 관계를 만드는 데 사용

### RDBMS

DBMS(Database Management System)

- 데이터 저장 및 관리를 용이하게 하는 시스템
- 데이터베이스와 사용자 간의 인터페이스 역할
- 사용자가 데이터 구성, 업데이트, 모니터링, 백업, 복구 등을 할 수 있도록 도움

RDBMS(Relational Database Management System)

- 관계형 데이터베이스를 관리하는 소프트웨어 프로그램
- ex) SQLite, MySQL, PostgreSQL, Oracle Database, …

### SQL(Structure Query Language)

데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어

테이블의 형태로 구조화된 관계형 데이터베이스에게 요청을 질의(요청)

[SQL Syntax]

```sql
SELECT column_name FROM table_name;
```

- SQL 키워드는 대소문자를 구분하지 않음(대문자로 작성하는 것을 권장)
- SQL Statements 끝에는 세미콜론(`’;’`)이 필요(명령어의 마침표)

### SQL Statements

SQL을 구성하는 가장 기본적인 코드 블록

```sql
SELECT column_name FROM table_name;
```

해당 예시 코드는 SELECT Statement라 부름

이 Statement에는 `SELECT`, `FROM` 2개의 keyword로 구성됨

### Querying Data

SELECT statement : 테이블에서 데이터를 조회 및 반환

```sql
SELECT
	select_list
FROM
	table_name;
```

- `SELECT` 키워드 이후 데이터를 선택하려는 필드를 하나 이상 지정
- `FROM` 키워드 이후 데이터를 선택하려는 테이블의 이름을 지정
- `‘*’` (asterisk)를 사용하여 모든 필드 선택

### Sorting Data

`ORDER BY` statement : 조회 결과의 레코드를 정렬

```sql
SELECT
	select_list
FROM
	table_name;
ORDER BY
	column1 [ASC|DESC],
	column2 [ASC|DESC],
	...;
```

- `FROM` clause 뒤에 위치
- 하나 이상의 컬럼을 기준으로 결과를 오름차순(`ASC`, 기본 값) or 내림차순(`DESC`)으로 정렬
- `NULL` 값이 존재할 경우 오름차순 정렬 시 결과에 NULL이 먼저 출력

### Filtering Data

[Clause]

`DISTINCT` : 조회 결과에서 중복된 레코드를 제거

```sql
SELECT DISTINCT
	select_list
FROM
	table_name;
```

- `SELECT` 키워드 바로 뒤에 작성해야 함
- `SELECT DISTINCT` 키워드 다음에 고유한 값을 선택하려난 하나 이상의 필드를 지정

`WHERE` : 조회 시 특정 검색 조건을 지정

```sql
SELECT
	select_list
FROM
	table_name
WHERE
	search_condition;
```

- `FROM` clause 뒤에 위치
- `search_condition`은 비교연산자 및 논리연산자(`AND`, `OR`, `NOT` 등)를 사용하는 구문이 사용됨
- Operators
    
    Comparison Operators(비교 연산자) : `=`, `≥`, `≤`, `≠`, `IS`, `LIKE`, `IN`, `BETWEEN … AND`
    
    `IN` Operator : 값이 특정 목록 안에 있는지 확인
    
    `LIKE` Operator : 값이 특정 패턴에 일치하는지 확인(Wildcards와 함께 사용)
    
    - `’%’` : 0개 이상의 문자열과 일치 하는지 확인
    - `‘_’` : 단일 문자와 일치 하는지 확인
    
    Logical Operators(논리 연산자) : `AND(&&)`, `OR(||)`, `NOT(!)`
    

`LIMIT` : 조회하는 레코드 수를 제한

```sql
SELECT
	select_list
FROM
	table_name
LIMIT [offset,] row_count;
```

- 하나 또는 두 개의 인자를 사용(0 또는 양의 정수)
- `row_count`는 조회하는 최대 레코드 수를 지정

### GROUP BY

레코드를 그룹화하여 요약본 생성(’집계 함수’와 함께 사용)

Aggregation Functions(집계 함수) : 값에 대한 계산을 수행하고 단일한 값일 반환하는 함수

ex) `SUM`, `AVG`, `MAX`, `MIN`, `COUNT`

```sql
SELECT
	c1, c2, ..., cn, aggregate_function(ci)
FROM
	table_name
GROUP BY
	c1, c2, ..., cn;
```

- `FROM` 및 `WHERE` 절 뒤에 배치
- `GROUP BY` 절 뒤에 그룹화 할 필드 목록을 작성

`HAVING` clause :

집계 항목에 대한 세부 조건을 지정

주로 `GROUP BY`와 함께 사용되며 `GROUP BY`가 없다면 `WHERE`처럼 동작

### Managing Tables

`CREATE TABLE` : 테이블 생성

```sql
CREATE TABLE table_name (
	column_1 data_type constraints,
	column_2 data_type constraints,
	...,
);
```

- 각 필드에 적용할 데이터 타입 작성
- 테이블 및 필드에 대한 제약조건(constraints) 작성

```sql
PRAGMA table_info('examples');
```

- 테이블 schema(구조) 확인
- Column ID(`”cid”`)는 각 컬럼의 고유한 식별자를 나타내는 정수 값
- `“cid”`는 직접 사용하지 않으며 PRAGMA 명령과 같은 메타데이터 조회에서 출력 값으로 활용됨

[SQLite 데이터 타입]

1. `NULL` : 아무런 값도 포함하지 않음을 나타냄
2. `INTEGER` : 정수
3. `REAL` : 부동 소수점
4. `TEXT` : 문자열
5. `BLOB` : 이미지, 동영상, 문서 등의 바이너리 데이터

Constraints(제약 조건)

- 테이블의 필드에 적용되는 규칙 또는 제한 사항
- 데이터의 무결성을 유지하고 데이터베이스의 일관성을 보장

[대표 제약 조건 3가지]

1. `PRIMARY KEY` : 해당 필드를 기본 키로 지정(`INTEGER` 타입에만 적용)
2. `NOT NULL` : 해당 필드에 NULL 값을 허용하지 않도록 지정
3. `FOREIGN KEY` : 다른 테이블과의 외래 키 관계를 정의

`AUTOINCREMENT` : 자동으로 고유한 정수 값을 생성하고 할당하는 필드 속성

- 필드의 자동 증가를 나타내는 특수한 키워드
- 주로 primary key 필드에 적용
- `INTEGER PRIMARY KEY AUTOINCREMENT`가 작성된 필드는 항상 새로운 레코드에 대해 이전 최대 값보다 큰 값을 할당
- 삭제된 값은 무시되며 재사용할 수 없게 됨

### Modifying table fields

`ALTER TABLE` : 테이블 및 필드 조작

- `ALTER TABLE ADD COLUMN` : 필드 추가
    
    ```sql
    ALTER TABLE
    	table_name
    ADD COLUMN
    	column_definition;
    ```
    
    - `ADD COLUMN` 키워드 이후 추가하고자 하는 새 필드 이름과 데이터 타입 및 제약 조건 작성
    - 단, 추가하고자 하는 필드에 `NOT NULL` 제약조건이 있을 경우 `NULL`이 아닌 기본 값 설정 필요
    - SQLite는 단일 문을 사용하여 한번에 여러 필드를 추가할 수 없음
- `ALTER TABLE RENAME COLUMN` : 필드 이름 변경
    
    ```sql
    ALTER TABLE
    	table_name
    RENAME COLUMN
    	current_name TO new_name
    ```
    
    - `RENAME COLUMN` 키워드 뒤에 이름을 바꾸려는 필드의 이름을 지정하고 `TO` 키워드 뒤에 새 이름을 지정
- `ALTER TABLE DROP COLUMN` : 필드 삭제
    
    ```sql
    ALTER TABLE
    	table_name
    DROP COLUMN
    	column_name
    ```
    
    - `DROP COLUMN` 키워드 뒤에 삭제 할 필드 이름 지정
- `ALTER TABLE RENAME TO` : 테이블 이름 변경
    
    ```sql
    ALTER TABLE
    	table_name
    RENAME TO
    	new_table_name
    ```
    
    - `RENAME TO` 키워드 뒤에 새로운 테이블 이름 지정

### Delete a table

`DROP TABLE` : 테이블 삭제

```sql
DROP TABLE
	table_name;
```

- DROP TABLE statement 이후 삭제할 테이블 이름 작성

### Modifying Data

`INSERT` : 테이블 레코드 삽입

```sql
INSERT INTO
	table_name (c1, c2, ...)
VALUES
	(v1, v2, ...);
```

- `INSERT INTO`절 다음에 테이블 이름과 괄호 안에 필드 목록 작성
- `VALUES` 키워드 다음 괄호 안에 해당 필드에 삽입할 값 목록 작성
- `DATE()` 함수를 이용해 테이블에 현재 날짜 데이터 입력 가능

### Update Data

`UPDATE` : 테이블 레코드 수정

```sql
UPDATE
	table_name
SET
	column_name = expression,
[WHERE
	condition];	
```

- `SET` 절 다음에 수정 할 필드와 새 값을 지정
- `WHERE` 절에서 수정 할 레코드를 지정하는 조건 작성
- `WHERE` 절을 작성하지 않으면 모든 레코드를 수정

### Delete Data

`DELETE` : 테이블 레코드 삭제

```sql
DELETE FROM
	table_name
[WHERE
	condition];
```

- `DELETE FROM` 절 다음에 테이블 이름 작성
- `WHERE` 절에서 삭제할 레코드를 지정하는 조건 작성
- `WHERE` 절을 작성하지 않으면 모든 레코드를 삭제

### Multi table queries

Join(결합) : 여러 테이블 간의 (논리적) 연결

`JOIN` : 둘 이상의 테이블에서 데이터를 검색하는 방법

- INNER JOIN : 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환
    
    ```sql
    SELECT
    	select_list
    FROM
    	table_a
    INNER JOIN
    	table_b
    	ON table_b.fk = table_a.pk;
    ```
    
    - `FROM` 절 이후 메인 테이블 지정 (`table_a`)
    - `INNER JOIN` 절 이후 메인 테이블과 조인할 테이블을 지정 (`table_b`)
    - `ON` 키워드 이후 조인 조건을 작성
    - 조인 조건은 `table_a`와 `table_b` 간의 레코드를 일치시키는 규칙을 지정
- LEFT JOIN : 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드 반환
    
    ```sql
    SELECT
    	select_list
    FROM
    	table_a
    LEFT JOIN
    	table_b
    	ON table_b.fk = table_a.pk;
    ```
    
    - FROM 절 이후 왼쪽 테이블 지정 (table_a)
    - LEFT JOIN 절 이후 오른쪽 테이블 지정 (table_b)
    - ON 키워드 이후 조인 조건을 작성
    - 왼쪽 테이블의 각 레코드를 오른쪽 테이블의 모든 레코드와 일치시킴
    - 오른쪽 테이블과 매칭되는 레코드가 없으면 `NULL`을 표시

---

### `SELECT` statement 실행 순서

1. FROM - 테이블에서
2. WHERE - 특정 조건에 맞추어
3. GROUP BY - 그룹화 하고
4. HAVING - 만약 그룹 중에서 조건이 있다면 맞추고
5. SELECT - 조회하여
6. ORDER BY - 정렬하고
7. LIMIT - 특정 위치의 값을 가져옴

[수행 목적에 따른 SQL Statements 유형]

- DDL(Data Definition Language)
    
    데이터의 기본 구조 및 형식 변경
    
    KEYWORD : `CREATE`, `DROP`, `ALTER`
    
- DQL(Data Query Language)
    
    데이터 검색
    
    KEYWORD : `SELECT`
    
- DML(Data Manipulation Language)
    
    데이터 조작(추가, 수정, 삭제)
    
    KEYWORD : `INSERT`, `UPDATE`, `DELETE`
    
- DCL(Data Control Language)
    
    데이터 및 작업에 대한 사용자 권한 제어
    
    KEYWORD : `COMMIT`, `ROLLBACK`, `GRANT`, `REVOKE`
    

### Query

“데이터베이스로부터 정보를 요청”하는 것

일반적으로 SQL로 작성하는 코드를 쿼리문(SQL문)이라 함

미국 국립 표준 협회(ANSI)와 국제 표준화 기구(ISO)에 의해 표준이 채택됨

### Type Affinity(타입 선호도)

컬럼에 데이터 타입이 명식적으로 지정되지 않았거나 지원하지 않을 때 SQLite가 자동으로 데이터 타입을 추론하는 것

https://www.sqlite.org/datatype3.html

[SQLite 타입 선호도의 목적]

유연한 데이터 타입 지원 :

- 데이터 타입을 명시적으로 지정하지 않고도 데이터를 저장하고 조회할 수 있음
- 컬럼에 저장되는 값의 특성을 기반으로 데이터 타입을 유추

간편한 데이터 처리 :

- `INTEGER` Type Affinity를 가진 열에 문자열 데이터를 저장해도 SQLite는 자동으로 숫자로 변환하여 처리

SQL 호환성 :

- 다른 데이터베이스 시스템과 호환성을 유지

### SQLite의 날짜와 시간

- SQLite에는 날짜 및/또는 시간을 저장하기 위한 별도 데이터 타입이 없음
- 대신 날짜 및 시간에 대한 함수를 사용해 표기 형식에 따라 `TEXT`, `REAL`, `INTEGER` 값으로 저장