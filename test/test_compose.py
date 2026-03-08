from app.check import Appointment
from app.compose import TWILIO_CHAR_LIMIT, compose_message

URL = "https://service.berlin.de/terminvereinbarung/termin/all/12345/"


def test_compose_message_no_appointments():
    result = compose_message(None, url=URL)
    assert result == "No appointments available."


def test_compose_message_empty_list():
    result = compose_message([], url=URL)
    assert result == "No appointments available."


def test_compose_message_single_appointment():
    appointment = Appointment(date="12.12.2024", href="/1")
    result = compose_message([appointment], url=URL)
    expected = "*Available Appointments*\n\n12.12.2024:\nhttps://service.berlin.de/1"
    assert result == expected


def test_compose_message_multiple_appointments():
    appointments = [
        Appointment(date="12.12.2024", href="/1"),
        Appointment(date="13.12.2024", href="/2"),
    ]
    result = compose_message(appointments, url=URL)
    expected = "*Available Appointments*\n\n12.12.2024:\nhttps://service.berlin.de/1\n\n13.12.2024:\nhttps://service.berlin.de/2"
    assert result == expected


def test_compose_message_truncates_when_over_limit():
    appointments = [
        Appointment(
            date=f"{i:02d}.01.2025",
            href=f"/terminvereinbarung/termin/time/{1000 + i}/",
        )
        for i in range(1, 51)
    ]
    result = compose_message(appointments, url=URL)

    assert len(result) <= TWILIO_CHAR_LIMIT
    assert result.startswith("*Available Appointments*")
    assert "more dates available." in result
    assert URL in result


def test_compose_message_includes_all_when_just_under_limit():
    appointments = [
        Appointment(date="12.12.2024", href="/1"),
        Appointment(date="13.12.2024", href="/2"),
        Appointment(date="14.12.2024", href="/3"),
    ]
    result = compose_message(appointments, url=URL)

    assert "more dates available." not in result
    assert "12.12.2024" in result
    assert "13.12.2024" in result
    assert "14.12.2024" in result
