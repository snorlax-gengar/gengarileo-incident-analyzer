# Task 02 — SQLite Setup

## 1. Task Goal

Gengarileo Incident Analyzer의 데이터 저장 기반을 준비한다.

이번 Task의 목표는 다음 두 가지로 제한했다.

1. Python에서 SQLite 데이터베이스에 정상적으로 연결한다.
2. `incidents` 테이블을 생성하고 실제 생성 여부를 검증한다.

이번 단계에서는 Incident 도메인 모델이나 Repository를 구현하지 않고,
SQLite 연결과 스키마 초기화라는 기반 기능에만 집중했다.

---

## 2. 설계 방향

Task 01에서 확정한 프로젝트 구조를 유지하면서 SQLite 관련 책임을 분리했다.

```text
src/gengarileo/
├── __init__.py
├── database.py
└── schema.py
```

### `database.py`

SQLite 연결과 DB 파일 경로를 담당한다.

- `DEFAULT_DB_PATH`
- `ensure_data_directory()`
- `connect()`

### `schema.py`

SQLite 테이블 구조와 스키마 초기화를 담당한다.

- `CREATE_INCIDENTS_TABLE_SQL`
- `init_schema()`

Repository, ORM, FastAPI 등의 상위 계층은 이번 Task에서 추가하지 않았다.

---

## 3. 주요 설계 결정

### 3.1 DB 경로

기본 개발 DB는 다음 경로를 사용한다.

```text
data/incidents.db
```

경로는 단순한 `Path("data/incidents.db")` 형태로 유지했다.

패키지 위치를 기준으로 프로젝트 루트를 복잡하게 계산하는 방식은
현재 단계에서는 필요하지 않다고 판단했다.

현재 프로젝트는 개발 단계의 Analyzer이며,
단순한 프로젝트 구조를 유지하면서 이후 요구사항이 생길 때 확장하는 방향을 선택했다.

### 3.2 SQLite 연결과 Schema 책임 분리

DB 연결과 테이블 생성 책임을 하나의 모듈에 몰아넣지 않았다.

```text
database.py
    ↓
SQLite Connection

schema.py
    ↓
incidents Table
```

`database.py`는 연결을 생성하고,
`schema.py`는 전달받은 connection을 사용하여 DDL을 실행한다.

이를 통해 각 모듈의 책임을 명확하게 유지했다.

### 3.3 Incident Schema

현재 `incidents` 테이블은 다음과 같이 정의했다.

```sql
CREATE TABLE IF NOT EXISTS incidents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    status TEXT NOT NULL,
    created_at TEXT NOT NULL
);
```

`status`나 `created_at`에 DB 기본값을 넣지 않았다.

이 결정은 이후 Incident 모델과 Repository를 구현할 때
애플리케이션에서 생성한 값을 저장하고 조회하는 흐름을
명확하게 검증하기 위한 것이다.

---

## 4. 테스트 전략

이번 Task에서는 실제 개발용 DB와 테스트 DB를 분리했다.

```text
개발 환경
    ↓
data/incidents.db

테스트 환경
    ↓
pytest tmp_path
```

이를 통해 테스트 실행이 실제 개발 DB에 영향을 주지 않도록 했다.

### Test 01 — DB 파일 생성

`connect()`를 호출했을 때 지정한 경로에 SQLite DB 파일이 생성되는지 확인했다.

### Test 02 — incidents 테이블 생성

`init_schema()` 실행 후 SQLite의 `sqlite_master`를 조회하여
`incidents` 테이블이 존재하는지 확인했다.

최종 테스트 결과:

```text
collected 2 items
tests/test_database.py ..    [100%]

2 passed
```

---

## 5. 실제 DB 검증

pytest에서는 임시 DB를 사용했기 때문에
실제 개발 환경의 `data/incidents.db`도 별도로 검증했다.

최종 확인 결과:

```text
db_file_exists = True
incidents_table = ('incidents',)
```

이를 통해 실제 개발 DB 파일과 `incidents` 테이블이
정상적으로 생성된 것을 확인했다.

---

## 6. 검증 과정에서 발생한 오류

실제 DB를 확인하기 위한 Python one-liner 실행 과정에서
두 번의 `SyntaxError`가 발생했다.

```text
SyntaxError: unterminated string literal
SyntaxError: '(' was never closed
```

### 원인

SQLite 구현 코드의 문제가 아니라,
Shell에서 Python one-liner를 실행하는 과정에서
SQL 문자열의 quote/escape가 잘못 처리된 것이 원인이었다.

### 해결

검증 명령을 수정하여 SQLite의 `sqlite_master`에서
`incidents` 테이블을 직접 조회했다.

최종 검증 결과는 정상적으로 확인되었다.

### 판단

이번 오류는 애플리케이션 구현 오류가 아니라
검증 명령 자체의 오류로 분류했다.

따라서:

```text
구현 오류       → 없음
테스트 오류     → 없음
검증 명령 오류  → 발생 후 해결
최종 검증       → 성공
```

으로 정리했다.

---

## 7. AI Collaboration

이번 Task에서는 Cursor AI를 구현 도구로 사용하고,
설계와 검증 방향은 개발자가 직접 판단하는 방식으로 진행했다.

### Cursor AI가 수행한 역할

- 현재 프로젝트 구조 분석
- SQLite 모듈 구성 제안
- `database.py` 구현
- `schema.py` 구현
- SQLite 테스트 구현
- pytest 실행 및 결과 확인
- 실제 DB 스키마 생성 검증 지원

### Developer가 수행한 역할

- Task 범위 결정
- 모듈 책임 분리 검토
- DB 경로 정책 결정
- incidents 스키마 결정
- DB 기본값 사용 여부 결정
- 테스트 포함 여부 결정
- 구현 결과 코드 리뷰
- 테스트 결과와 실제 DB 결과 검증
- 발생한 오류의 성격 판단

### Collaboration Flow

```text
Task 정의
   ↓
Cursor 설계 제안
   ↓
설계 검토
   ↓
설계 수정 및 확정
   ↓
Cursor 구현
   ↓
pytest 실행
   ↓
실제 DB 검증
   ↓
코드 리뷰
   ↓
개발 로그 작성
```

이번 Task를 통해 AI가 제안한 내용을 그대로 사용하는 것이 아니라,
개발자가 요구사항과 설계 의도를 기준으로 AI의 제안을 검토하고
최종 결정을 내리는 협업 방식을 경험했다.

---

## 8. Code Review Result

구현 완료 후 다음 파일을 리뷰했다.

```text
src/gengarileo/database.py
src/gengarileo/schema.py
tests/test_database.py
```

리뷰 결과:

| 영역 | 결과 |
|---|---|
| 요구사항 준수 | PASS |
| 책임 분리 | PASS |
| SQLite 구현 | PASS |
| Schema 구현 | PASS |
| 테스트 격리 | PASS |
| 테스트 품질 | PASS |
| 과도한 추상화 | 없음 |
| 다음 단계 확장성 | PASS |

**Task 02 구현은 수정 없이 승인했다.**

---

## 9. Lessons Learned

### 9.1 테스트 성공과 실제 환경 검증은 별개의 문제

`pytest`가 통과했다고 해서 실제 개발 DB까지
정상적으로 구성되었다고 단정하지 않았다.

따라서:

```text
자동화 테스트
+
실제 환경 검증
```

을 각각 수행했다.

### 9.2 검증 명령도 오류가 발생할 수 있다

AI가 작성하거나 실행하는 검증 명령도 항상 정상이라고 가정하지 않고,
실제 결과와 오류 메시지를 확인해야 한다는 것을 경험했다.

이번 Task에서는 구현 코드는 정상인 반면,
검증 명령에서 SyntaxError가 발생했다.

### 9.3 작은 프로젝트에서도 책임 분리가 의미가 있다

SQLite 연결과 Schema를 별도 모듈로 분리하면서
각 코드가 어떤 책임을 가지는지 명확하게 이해할 수 있었다.

```text
database.py
→ 어떻게 DB에 연결할 것인가?

schema.py
→ DB에 무엇을 만들 것인가?
```

이 구조는 이후 Repository와 Incident Model을 추가할 때
기반 역할을 할 수 있다.

---

## 10. Task 02 Retrospective

이번 Task는 기능적으로는 매우 작은 작업이었다.

하지만 단순히 SQLite 코드를 작성하는 것보다,

```text
요구사항
  ↓
설계
  ↓
AI 제안 검토
  ↓
의사결정
  ↓
구현
  ↓
테스트
  ↓
실제 환경 검증
  ↓
코드 리뷰
```

라는 개발 흐름을 직접 경험했다는 점에서 의미가 있었다.

특히 Cursor가 제안한 내용을 그대로 적용하지 않고,
DB 경로, Schema 기본값, 테스트 범위를 직접 검토하고 결정하면서
AI를 단순 코드 생성기가 아닌 개발 협업 도구로 활용하는 경험을 했다.

이번 Task의 핵심 결과는 SQLite 자체보다
**AI의 제안을 개발자가 검토하고 최종적인 기술적 결정을 내리는 과정**이었다.

---

## 11. Task 02 Completion

```text
SQLite 연결                 ✅
DB 디렉터리 생성            ✅
incidents Schema 생성      ✅
개발 DB 생성                ✅
테스트 DB 분리              ✅
pytest 2개 테스트 통과      ✅
실제 incidents 테이블 확인  ✅
코드 리뷰                   ✅
개발 로그                   ✅
```

### Status

**Task 02 — COMPLETED**

---

## Next Task

다음 단계에서는 SQLite 기반 위에
Incident 도메인 모델을 추가한다.

예정 범위:

```text
Incident dataclass
    ↓
id
title
description
status
created_at
```

이번 Task 역시 한 번에 많은 기능을 추가하지 않고,
**Incident 모델 정의와 테스트**라는 작은 단위로 진행한다.
