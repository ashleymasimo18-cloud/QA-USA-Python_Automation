# Urban Routes Test Automation Framework

A Python test automation framework for the Urban Routes web application, built with Pytest using the Page Object Model pattern.

## What it does
Automates end-to-end checks of the routing and order workflow — trip requests, transport mode selection, and order placement — with server validation checks run before each test to confirm the environment is ready.

## Structure
- `pages.py` – page objects for the app's UI elements and actions
- `helpers.py` – reusable utility functions shared across tests
- `data.py` – test data, kept separate from test logic for easy updates
- `main.py` – test entry point / runner
- `requirements.txt` – project dependencies

## Setup
```
pip install -r requirements.txt
```

## Run
```
pytest
```

Built as part of TripleTen's QA Engineering program.

## Code style
Variables use snake_case; constants are uppercase; test functions are prefixed with `test_` and named for the scenario they cover. Code is kept modular, with reusable logic imported where needed.
