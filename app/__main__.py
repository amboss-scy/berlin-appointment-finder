import asyncio
from time import sleep

from .check import check_available_appointments
from .compose import compose_message
from .config import Settings
from .send import send_message

settings = Settings()


async def main():
    if not settings.appointment_id:
        raise ValueError(
            "APPOINTMENT_ID not set. Please see README.md for instructions for setting it."
        )

    previous_message: str | None = None

    while True:
        print("Checking for available appointments...")
        url = f"https://service.berlin.de/terminvereinbarung/termin/all/{settings.appointment_id}/"
        available_appointments = await check_available_appointments(
            url=url,
            playwright_headless=settings.playwright_headless,
        )
        message = compose_message(
            available_appointments=available_appointments, url=url
        )

        if message != previous_message:
            print("News! Sending message...")
            await send_message(message)
        else:
            print("No news. Not sending message.")

        previous_message = message
        print(f"Sleeping for {settings.checking_interval} seconds.")
        sleep(settings.checking_interval)


if __name__ == "__main__":
    asyncio.run(main())
