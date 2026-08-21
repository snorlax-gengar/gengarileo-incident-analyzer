# Gengarileo Incident Analyzer — Task 03 개발 로그

## 1. Task 개요

### Task 03 — Incident Domain Model

Python에서 장애 정보를 표현할 수 있는 `Incident` dataclass를 정의한다.

### 구현 범위

- `src/gengarileo/models.py` 생성
- `Incident` dataclass 정의
- 필드: `id`, `title`, `description`, `status`, `created_at`
- Python 표준 라이브러리 `dataclasses` 사용
- `tests/test_models.py` 작성
- Incident 생성 및 필드 값 검증
- 기존 Task 02 코드 수정 금지

### 제외 범위

- SQLite 연동
- INSERT / SELECT
- Repository
- API
- AI 분석
- Attachment

---

## 2. 구현 결과

### `src/gengarileo/models.py`

`dataclass`를 사용해 `Incident` 모델을 추가했다.

현재 필드는 다음과 같다.

```python
@dataclass
class Incident:
    id: int
    title: str
    description: str
    status: str
    created_at: str
```

Domain Model은 DB 연결이나 SQL을 직접 알지 않도록 구성했다.

### `tests/test_models.py`

Incident 객체를 생성한 후 다음 다섯 필드의 값이 정상적으로 유지되는지 검증했다.

- `id`
- `title`
- `description`
- `status`
- `created_at`

---

## 3. 테스트 결과

전체 테스트를 실행한 결과:

```text
collected 3 items

tests/test_database.py ..   [ 66%]
tests/test_models.py .      [100%]

============================== 3 passed ==============================
```

- Task 02 테스트: 2 passed
- Task 03 테스트: 1 passed
- 전체: **3 passed**

기존 Task 02 테스트도 함께 통과했으므로 이번 변경으로 기존 기능에 Regression이 발생하지 않았음을 확인했다.

---

## 4. 코드 리뷰 결과

### 4.1 책임 분리

`Incident`는 장애 데이터를 표현하는 역할만 담당한다.

현재 구조는 다음과 같다.

```text
database.py
    └── SQLite 연결

schema.py
    └── incidents 테이블 스키마

models.py
    └── Incident 데이터 표현
```

Model에 DB 연결이나 SQL 로직이 들어가지 않았으므로 각 모듈의 책임이 분리되어 있다.

### 4.2 의존성

별도의 외부 라이브러리를 추가하지 않고 Python 표준 라이브러리의 `dataclasses`를 사용했다.

현재 Task의 목적에 필요한 수준으로 의존성을 최소화했다.

### 4.3 테스트 범위

테스트는 Incident 객체 생성과 필드 값 보존만 검증한다.

이번 Task에서는 DB나 Repository를 구현하지 않았으므로 테스트가 해당 계층까지 확장되지 않은 것이 적절하다.

### 4.4 Task 02 영향

다음 파일은 변경되지 않았다.

- `src/gengarileo/database.py`
- `src/gengarileo/schema.py`
- `tests/test_database.py`

Task 단위의 변경 범위를 유지했다.

---

## 5. 설계 의사결정 — `id: int`

초기 설계에서는 DB에 저장되기 전 Incident를 고려하여 `id: int | None`을 사용하는 방안도 검토했다.

현재 구현은 다음과 같다.

```python
id: int
```

이번 Task에서는 DB INSERT나 Repository를 구현하지 않았기 때문에 현재 범위에서 `id: int`를 문제로 판단하지 않았다.

따라서 이번 Task에서는 코드를 수정하지 않고, 실제 DB INSERT를 담당하는 Repository를 구현하는 단계에서 Incident의 생성 및 ID 부여 흐름을 확인한 뒤 `id: int`와 `id: int | None` 중 적절한 형태를 다시 결정하기로 했다.

이 결정은 **현재 구현을 억지로 미래 요구사항에 맞추기보다 실제 사용 흐름이 등장하는 단계에서 판단한다**는 원칙에 따른 것이다.

---

## 6. AI 협업 기록

이번 Task에서는 Cursor에 전체적인 설계 판단을 맡기기보다, 먼저 요구사항과 범위를 정의한 후 구현을 요청했다.

협업 흐름:

```text
요구사항 정의
    ↓
Cursor 구현
    ↓
테스트 실행
    ↓
현재 소스 조회
    ↓
코드 리뷰
    ↓
수정 필요 여부 판단
```

Cursor 구현 결과를 그대로 승인하지 않고 현재 소스와 테스트 결과를 확인한 후 리뷰했다.

이번 리뷰에서는 수정이 필요한 문제를 발견하지 못했으며, 현재 구현을 그대로 유지하기로 결정했다.

---

## 7. 총평

Task 03에서는 복잡한 기능을 추가하기보다 장애 정보를 표현하는 최소 Domain Model을 정의했다.

이번 단계의 핵심은 `Incident` 자체보다도 **Domain Model과 DB 접근 로직을 분리하는 구조를 실제 코드로 경험했다는 점**이다.

현재는 DB Schema와 Incident Model의 필드가 거의 동일하지만, 이는 현재 요구사항이 단순하기 때문이다. 이후 Repository와 Analyzer가 추가되면 Domain Model이 DB 구조와 반드시 동일해야 하는 것은 아니라는 점을 고려해야 한다.

또한 `id` 타입처럼 미래의 요구사항을 미리 과도하게 반영하기보다 실제 기능이 필요한 단계에서 재검토하는 방식으로 설계 판단을 남겼다.

---

## 8. Task 03 완료 상태

- [x] 요구사항 정의
- [x] Incident dataclass 구현
- [x] Incident 테스트 작성
- [x] 기존 테스트 Regression 확인
- [x] 코드 리뷰
- [x] 설계 의사결정 기록
- [x] 개발 로그 작성
- [ ] Git commit
- [ ] GitHub push

**현재 상태: 구현 및 리뷰 완료 / Commit 대기**
