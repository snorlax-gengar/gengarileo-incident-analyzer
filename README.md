# Gengarileo Incident Analyzer

운영 중 발생하는 장애(Incident)의 원인 분석을 보조하는 AI 기반 시스템입니다.

## 현재 단계

프로젝트 기반 구조만 구성되어 있습니다. SQLite 연결, Incident 모델, Repository, 테스트 로직은 이후 단계에서 추가합니다.

## 구조

```text
gengarileo-incident-analyzer/
├── README.md
├── requirements.txt
├── pyproject.toml
├── src/gengarileo/
├── tests/
└── data/
```

## 개발 환경

```bash
pip install -r requirements.txt
pip install -e .
pytest
```

`data/` 아래의 실제 DB 파일(`.db`)은 Git에 포함하지 않습니다.
