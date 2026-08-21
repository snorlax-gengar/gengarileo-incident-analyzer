"""Tests for the Incident dataclass."""

from gengarileo.models import Incident


def test_incident_creation_preserves_field_values():
    incident = Incident(
        id=1,
        title="API timeout",
        description="The payment API did not respond within 5 seconds.",
        status="open",
        created_at="2026-08-21T15:00:00",
    )

    assert incident.id == 1
    assert incident.title == "API timeout"
    assert incident.description == "The payment API did not respond within 5 seconds."
    assert incident.status == "open"
    assert incident.created_at == "2026-08-21T15:00:00"
