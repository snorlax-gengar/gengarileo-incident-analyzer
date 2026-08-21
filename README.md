# Gengarileo Incident Analyzer

> **AI 협업 기반 Incident 분석 및 장애 대응 지원 시스템**

## 📌 Project Overview

Gengarileo Incident Analyzer는 개발 및 운영 환경에서 발생하는 다양한 장애와 오류를 구조화하고, 장애 원인 분석과 대응 과정에서 AI를 활용할 수 있도록 만드는 개인 프로젝트입니다.

금융권 SI/SM 업무를 수행하며 경험한 장애들은 단순한 에러 코드만으로 원인을 파악하기 어려운 경우가 많았습니다.

예를 들어:

- WebDAV 파일 부재로 인한 오류
- 제휴사 파일 수신 시점 차이로 발생하는 배치 오류
- 전문 태그 및 Collection 변환 과정에서 발생하는 오류
- JSP / JavaScript 문법 차이로 인한 운영 환경 오류
- 제휴사의 전문 또는 로직 변경으로 발생하는 연계 오류
- 동영상 업로드 과정에서 발생한 HTTP 416 오류

이러한 장애들은 **에러 메시지만 확인하는 것으로는 원인을 바로 파악하기 어렵고**, 실제 데이터, 로그, 호출 흐름 및 실행 환경을 함께 분석해야 하는 경우가 많았습니다.

Gengarileo Incident Analyzer는 이러한 경험을 바탕으로,

> **"장애가 발생했을 때 개발자가 문제를 더 빠르고 체계적으로 분석할 수 있도록 도와주는 시스템"**

을 만드는 것을 목표로 합니다.

---

## 🎯 Project Goal

단순히 에러를 검색하거나 AI에게 오류 메시지를 전달하는 것이 아니라,

```text
Incident 발생
      ↓
장애 정보 수집
      ↓
관련 데이터 / 로그 / 첨부파일 분석
      ↓
유사 장애 탐색
      ↓
원인 후보 도출
      ↓
해결 방법 및 근거 정리
      ↓
장애 지식 축적
```

이라는 흐름을 구축하는 것을 목표로 합니다.

궁극적으로는 과거의 장애 대응 경험을 개인의 기억에만 의존하지 않고 **재사용 가능한 개발 자산**으로 만드는 것을 지향합니다.

---

## 🤖 AI Collaboration

이 프로젝트는 **AI를 단순한 코드 생성 도구로 사용하는 것을 목표로 하지 않습니다.**

개발 과정에서 AI를 다음과 같이 활용합니다.

```text
Developer
    │
    ├── 요구사항 정의
    ├── 설계 의사결정
    ├── 결과 검증
    └── 코드 리뷰 및 최종 판단
    │
    ▼
AI
    │
    ├── 구현 지원
    ├── 테스트 작성
    ├── 오류 분석
    ├── 코드 리뷰
    └── 개발 문서 작성 지원
```

개발자는 **문제 정의와 의사결정**을 담당하고, AI는 구현 및 분석 과정의 생산성을 높이는 협업 파트너로 활용합니다.

---

## 🏗️ Current Architecture

현재는 프로젝트의 기반을 구축하는 단계입니다.

```text
┌──────────────────────────────┐
│       Gengarileo             │
│   Incident Analyzer          │
└──────────────┬───────────────┘
               │
               ▼
        ┌─────────────┐
        │   Incident  │
        │    Model    │
        └──────┬──────┘
               │
               ▼
        ┌─────────────┐
        │ Repository  │
        │   (예정)    │
        └──────┬──────┘
               │
               ▼
        ┌─────────────┐
        │   SQLite    │
        └─────────────┘
```

현재 구현된 영역:

- Python 프로젝트 기반 구조
- SQLite 연결
- `incidents` 테이블 스키마
- `Incident` Domain Model
- 단위 테스트

향후 다음 영역을 단계적으로 확장할 예정입니다.

- Incident 저장 / 조회
- Attachment 관리
- 로그 및 장애 데이터 분석
- 유사 Incident 탐색
- AI 기반 원인 분석
- 해결 과정 및 결과 관리
- 장애 지식 축적 및 재활용

> 위 기능들은 현재 모두 구현된 기능이 아니라 **프로젝트의 향후 개발 방향**입니다.

---

## 🧩 Technology Stack

| Category | Technology |
|---|---|
| Language | Python |
| Database | SQLite |
| Test | pytest |
| AI Development | Cursor / Claude / ChatGPT |
| Version Control | Git / GitHub |

초기 단계에서는 불필요한 프레임워크와 라이브러리를 최소화하고, **작은 단위로 구현 → 테스트 → 리뷰 → 확장**하는 방식을 사용합니다.

---

## 📂 Project Structure

```text
gengarileo-incident-analyzer/
│
├── src/
│   └── gengarileo/
│       ├── __init__.py
│       ├── database.py
│       ├── schema.py
│       └── models.py
│
├── tests/
│   ├── conftest.py
│   ├── test_database.py
│   └── test_models.py
│
├── data/
│   └── .gitkeep
│
├── docs/
│   └── ai-collaboration/
│       ├── task-01-*.md
│       ├── task-02-*.md
│       └── task-03-*.md
│
├── README.md
├── pyproject.toml
└── requirements.txt
```

---

## 📚 Development Log

이 프로젝트는 기능 구현뿐만 아니라 **설계와 AI 협업 과정 자체를 기록**합니다.

각 Task는 다음과 같은 흐름으로 진행합니다.

```text
Requirements
    ↓
Design
    ↓
AI Collaboration
    ↓
Implementation
    ↓
Test
    ↓
Code Review
    ↓
Decision
    ↓
Development Log
    ↓
Commit
```

개발 과정에서 발생한 오류, 설계 의사결정, AI와의 협업 방식 및 회고는 `docs/ai-collaboration/`에 기록합니다.

이를 통해 단순한 결과물뿐만 아니라 **문제 해결 과정과 개발 의사결정의 근거**를 확인할 수 있도록 구성합니다.

---

## 🚧 Project Status

**Current Version: v0.1 — Foundation**

### Completed

- [x] Project baseline
- [x] Git / GitHub setup
- [x] SQLite database setup
- [x] Incident Domain Model
- [x] Basic unit tests

### In Progress

- [ ] Incident Repository
- [ ] INSERT / SELECT
- [ ] Incident ↔ SQLite mapping

### Planned

- [ ] Attachment management
- [ ] Incident analysis
- [ ] Log analysis
- [ ] Similar Incident search
- [ ] AI-assisted root cause analysis
- [ ] Knowledge accumulation

---

## 💡 Why Gengarileo?

이 프로젝트는 단순히 새로운 기술을 사용해보기 위한 프로젝트가 아닙니다.

실제 개발 및 운영 과정에서 경험했던 **"원인을 찾기 어려운 장애"**를 어떻게 하면 더 체계적으로 분석하고, 동일한 문제가 발생했을 때 이전의 경험을 다시 활용할 수 있을지에 대한 고민에서 시작되었습니다.

그리고 그 과정에서 **AI를 개발자의 대체 수단이 아니라 문제 해결 능력을 확장하는 협업 도구로 활용하는 것**을 실험하고 있습니다.

---

## 📌 Project Philosophy

> **기억에 의존하는 장애 대응에서, 축적되고 재사용되는 장애 분석으로.**

> **AI에게 개발을 맡기는 것이 아니라, AI와 함께 문제를 해결한다.**
