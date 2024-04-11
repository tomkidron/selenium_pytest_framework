import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=None,
        help="Specify the browser (e.g., chrome, firefox)",
    )
