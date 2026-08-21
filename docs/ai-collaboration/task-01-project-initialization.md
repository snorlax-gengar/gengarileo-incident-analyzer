# AI Collaboration Log

## Task 01 - Project Initialization

### Task Summary

Gengarileo Incident Analyzer의 초기 Python 프로젝트 구조를 생성하고,
실행 환경을 검증한 뒤 GitHub Repository에 첫 번째 baseline을 등록했다.

---

## Issue 01 — pytest 실행 환경 문제

### Symptom

`pytest` 명령을 직접 실행했을 때 실행 파일을 찾지 못하는 문제가 발생했다.

또한 Cursor가 실행한 명령 중 `&&` 구문이 Windows PowerShell 환경에서
ParserError를 발생시켰다.

### Root Cause

1. 프로젝트 의존성인 pytest가 아직 설치되지 않았다.
2. Windows PowerShell 환경과 명령어 실행 방식의 차이가 있었다.

### Resolution

프로젝트 의존성을 설치했다.

```bash
python -m pip install -r requirements.txt
```

환경에 의존하지 않고 Python 모듈 방식으로 pytest를 실행했다.

```bash
python -m pytest
```

초기 프로젝트에는 테스트 코드가 존재하지 않았기 때문에
`collected 0 items`가 출력되었으며 이는 정상적인 결과로 판단했다.

---

## Issue 02 — src Layout에서 Package Import 문제

### Symptom

프로젝트의 `gengarileo` 패키지를 Python에서 import하지 못하는 문제가 발생했다.

프로젝트는 다음과 같은 `src` layout을 사용하고 있었다.

```text
gengarileo-incident-analyzer/
└── src/
    └── gengarileo/
```

### Root Cause

`src` layout에서는 프로젝트 루트에 있는 디렉토리를 단순히 바라보는 것만으로
Python이 `gengarileo` 패키지를 항상 인식하는 것은 아니다.

현재 프로젝트는 패키지가 Python 환경에 설치되지 않은 상태였기 때문에
`gengarileo` package import 문제가 발생했다.

### Resolution

`pyproject.toml`에 setuptools 기반 build configuration을 추가했다.

```toml
[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"
```

이후 editable install을 수행했다.

```bash
pip install -e .
```

### Validation

다음과 같이 패키지가 정상적으로 설치되었다.

```text
Successfully installed gengarileo-0.1.0
gengarileo package OK
```

따라서 `gengarileo` 패키지가 Python 환경에서 정상적으로 인식되는 것을 확인했다.

---

## AI Collaboration

### AI Tool

Cursor AI

### AI가 수행한 역할

- 실행 환경 및 오류 메시지 분석
- pytest 실행 문제의 원인 파악
- Python package import 문제 분석
- `pyproject.toml` 패키징 설정 제안
- editable install 방법 제안
- 수정 후 실행 결과 검증 지원

### Developer가 수행한 역할

- 프로젝트 구조 및 기술 방향 결정
- Cursor에게 작업 범위와 제약사항 전달
- 실제 명령 실행 및 결과 확인
- 오류 발생 여부 판단
- AI가 제안한 해결 방법 검증
- GitHub Repository에 최종 결과 push

### Collaboration Flow

```text
문제 발생
    ↓
실행 결과 확인
    ↓
Cursor를 통한 원인 분석
    ↓
해결 방법 적용
    ↓
실제 실행
    ↓
결과 검증
```

이번 작업에서 AI는 단순 코드 생성 도구가 아니라
개발 환경의 문제를 분석하고 해결 방법을 제안하는 협업 도구로 활용했다.

---

## Lessons Learned

### 1. Python Module 실행

```bash
python -m pytest
```

실행 파일이 PATH에 직접 등록되어 있지 않은 환경에서도
현재 Python 환경의 pytest를 명확하게 실행할 수 있다.

### 2. Python src Layout

```text
src/
└── gengarileo/
```

형태의 프로젝트 구조에서는 Python package의 설치 및 import 설정을
함께 고려해야 한다.

### 3. Editable Install

```bash
pip install -e .
```

개발 중인 Python package를 editable mode로 설치하면
소스 코드를 수정하면서 설치된 package를 계속 사용할 수 있다.

---

## Task 01 Validation Checklist

- [x] Python 프로젝트 구조 생성
- [x] src layout 적용
- [x] pytest 의존성 설치
- [x] pytest 실행 환경 확인
- [x] `gengarileo` package import 확인
- [x] Git 초기화
- [x] 첫 번째 commit 생성
- [x] GitHub Repository 생성
- [x] GitHub에 push 완료

---

## Current Baseline

현재 프로젝트는 다음 상태에서 Task 01을 종료했다.

```text
gengarileo-incident-analyzer/
├── .gitignore
├── README.md
├── requirements.txt
├── pyproject.toml
├── src/
│   └── gengarileo/
│       └── __init__.py
├── tests/
│   └── conftest.py
└── data/
    └── .gitkeep
```

아직 구현하지 않은 기능:

- Incident Model
- SQLite DB 연결
- SQLite Schema
- Incident Repository
- INSERT
- SELECT
- Incident 분석 기능
- Attachment 처리
- AI/LLM 연동

---

## Next Task

### Task 02 — SQLite 연결 및 스키마 초기화

다음 단계에서는 범위를 SQLite 연결 및 스키마 초기화로 제한한다.

목표:

> Python에서 SQLite에 정상적으로 연결하고 `incidents` 테이블을 생성할 수 있는지 검증한다.

이번 Task에서는 다음 기능을 아직 구현하지 않는다.

- Incident dataclass
- Repository
- INSERT
- SELECT
- AI Analyzer
- Attachment
