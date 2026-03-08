from .check import Appointment

TWILIO_CHAR_LIMIT = 1600


def _format_appointment(appointment: Appointment) -> str:
    return f"{appointment.date}:\nhttps://service.berlin.de{appointment.href}"


def _format_suffix(remaining: int, url: str) -> str:
    return f"... and {remaining} more dates available. Book here: {url}"


def compose_message(
    available_appointments: list[Appointment] | None,
    url: str,
) -> str:
    if not available_appointments:
        return "No appointments available."

    header = "*Available Appointments*"
    separator = "\n\n"
    entries = [_format_appointment(a) for a in available_appointments]
    total = len(entries)

    message = header
    for i, entry in enumerate(entries):
        remaining = total - i - 1
        candidate = message + separator + entry

        if remaining > 0:
            candidate += separator + _format_suffix(remaining, url)
        if len(candidate) > TWILIO_CHAR_LIMIT:
            return message + separator + _format_suffix(total - i, url)

        message += separator + entry

    return message
