
import re
from playwright.sync_api import Page, expect
from pages.orghrm_login_page import LoginPage
from pages.orghrm_home_page import Homepage

def test_login_orghrm(page:Page) -> None:
    
    page.goto("https://opensource-demo.orangehrmlive.com/")

    login_page=LoginPage(page)
    homepage=Homepage(page)
    
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()

    expect(homepage.upgrade_btn).to_be_visible()
    homepage.click_performance_link()
    homepage.click_dashboard_link()