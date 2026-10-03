# RKA: Replit Keep Alive

[![Tests](https://github.com/Reathe/RKA/actions/workflows/tests.yml/badge.svg)](https://github.com/Reathe/RKA/actions/workflows/tests.yml)
[![PyPI](https://img.shields.io/pypi/v/RKA)](https://pypi.org/project/RKA/)
![Python](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

> Keep a long-running Python project (Discord bot, scraper, worker…) alive on [Replit](https://replit.com)
> with **one line of code**.

Replit puts a project to sleep when nobody visits it. **RKA** starts a tiny web server in a background thread.
Point a free uptime monitor at it, the regular pings count as visits, and your project keeps running.

## Installation

```bash
pip install RKA
```

## Usage

```python
from RKA import keep_alive

keep_alive()          # starts the web server in the background and returns immediately

# ... your long-running code, e.g.
bot.run(TOKEN)
```

Then:

1. Run your project. Replit shows a web view with the URL of the server (it answers `Hello. I am alive!`).
2. Create a free HTTP monitor on [UptimeRobot](https://uptimerobot.com) (or any similar service) for that
   URL, checking every 5 minutes.

### Options

```python
keep_alive(host="0.0.0.0", port=8080)   # defaults
```

`keep_alive()` returns the `threading.Thread` running the server, in case you need to manage it.

## How it works

`keep_alive()` starts a minimal [Flask](https://flask.palletsprojects.com/) app with a single `/` route in a
separate thread, so it never blocks your main program. The whole library is
[about 15 lines](RKA/keep_alive.py).

## Development

The project uses a modern Python packaging and quality setup:

- **Packaging:** `pyproject.toml` with the [Hatchling](https://hatch.pypa.io/) backend
- **Tests:** `pytest`, with Flask's test client
- **Code quality:** `black`, `isort`, `flake8`, `mypy`
- **Automation:** `tox` runs tests on Python 3.8–3.11, plus lint and type-check environments
- **CI/CD (GitHub Actions):** tests on every push across Python versions and operating systems; the package is
  **published to PyPI automatically** when a GitHub release is created

```bash
git clone https://github.com/Reathe/RKA
cd RKA
pip install -e ".[dev]"

pytest            # run the tests
tox               # full matrix: tests (py38–py311), lint, type checks
```

## License

[MIT](LICENSE)
