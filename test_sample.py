import pytest
from playwright.sync_api import Page

def test_google_title(page: Page):
    # Open Google
    page.goto("https://www.google.com")

    # Verify page title
    assert "Google" in page.title() 