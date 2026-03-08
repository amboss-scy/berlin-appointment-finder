# Berlin Appointment Finder

An app that monitors the Berlin city administration website for available appointments and sends notifications via Twilio, running online with GitHub Actions.

## Usage

### Setting up the Application

1. [Create a free GitHub account](https://github.com/signup) if you don't have one
2. [Fork this repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository)
3. [Create a free Twilio account](https://www.twilio.com/try-twilio) if you don't have one
4. Obtain your Twilio information:
    - Go to the [Twilio Console](https://console.twilio.com/) and find your account SID and authentication token under "Account Info"
    - Go to the [US](https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn) or [EU](https://console.twilio.com/eu/develop/sms/try-it-out/whatsapp-learn) WhatsApp sandbox and find your WhatsApp phone number
5. Go to the [Berlin City Administration website](https://service.berlin.de/dienstleistungen/) and note the ID of your desired appointment type, which you can find in the URL (e.g., `120703` for [this service](https://service.berlin.de/dienstleistung/120703/))
6. In your fork of this repository, go to "Settings" → "Secrets and variables" → "Actions" and add the following:
    - **Secrets:**
        - `TWILIO_AUTH_TOKEN`: Your Twilio authentication token
    - **Variables:**
        - `APPOINTMENT_ID`: The ID of your desired appointment type
        - `TWILIO_ACCOUNT_SID`: Your Twilio account SID
        - `TWILIO_FROM_NO_WHATSAPP`: Your Twilio WhatsApp phone number
        - `TWILIO_TO_NO`: Your private phone number

> _To send notifications via SMS, set the optional variable `TWILIO_FROM_NO_SMS` to your Twilio phone number (from the [Twilio Console](https://console.twilio.com/)) and `TWILIO_USE_WHATSAPP` to `False`._

### Running the Application

1. In your fork, go to "Actions" → "Berlin Appointment Finder"
2. Depending on the workflow state:
    - If the workflow is disabled, click "Enable workflow" to activate it
    - If it's enabled and you want to stop it, click "..." → "Disable workflow"
3. When enabled, the workflow automatically starts at 00:00 (12:00 AM), 6:00 (6:00 AM), 12:00 (12:00 PM), and 18:00 (6:00 PM), and checks for available appointments every 90 seconds for up to 6 hours
4. To immediately start the workflow, click "Run workflow" → "Run workflow," selecting the `master` branch

## Local Development

### Setup

1. **Install uv**: Follow the instructions [here](https://docs.astral.sh/uv/getting-started/installation/)
2. **Set up the environment**: Run `uv sync` to install the virtual Python environment and dependencies
3. **Install Playwright browser**: Run `uv run playwright install --with-deps chromium` to install the Chromium browser used by Playwright
3. **Create a `.env` file** with the following environment variables:
    - **Required:**
        - `APPOINTMENT_ID` (`int`)
        - `TWILIO_ACCOUNT_SID` (`str`)
        - `TWILIO_AUTH_TOKEN` (`str`)
        - `TWILIO_FROM_NO_WHATSAPP` (`str`)
        - `TWILIO_TO_NO` (`str`)
    - **Optional:**
        - `CHECKING_INTERVAL` (`int`, default: `90`)
        - `PLAYWRIGHT_HEADLESS` (`bool`, default: `True`)
        - `TWILIO_FROM_NO_SMS` (`str`, used if `TWILIO_USE_WHATSAPP` is `False`)
        - `TWILIO_USE_WHATSAPP` (`bool`, default: `True`)

### Utilities

The following `make` commands are available for local development:

- **Run app**: `make run`
- **Type-check code**: `make check`
- **Lint and check formatting (no fixes)**: `make lint`
- **Fix linting and formatting issues**: `make format`
- **Run tests**: `make test`
- **Clean project directory**: `make clean`

## Contributing

Feel free to fork this project, open issues, or submit pull requests to contribute.

## License

This project is licensed under the AGPL-3.0-or-later license. See the [LICENSE](./LICENSE) file for more details.
