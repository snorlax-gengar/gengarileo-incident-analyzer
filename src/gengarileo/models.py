"""Domain models for incident data."""

from dataclasses import dataclass


@dataclass
class Incident:
    """장애 정보를 표현하는 데이터 구조."""

    id: int
    title: str
    description: str
    status: str
    created_at: str
