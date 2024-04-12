import pytest

"""Defines command-line options for pytest execution."""


def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default=None,
        help="Specify the browser to use (e.g., chrome, firefox)",
    )
    parser.addoption(
        "--query",
        action="store",
        default=None,
        help="Allows passing a query parameter for search tests",
    )
