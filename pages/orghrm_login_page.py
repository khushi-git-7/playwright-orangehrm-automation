from playwright.sync_api import Page
class LoginPage:
    def __init__(self, page:Page):
        self.page = page
        self.username = page.get_by_role("textbox", name="Username")
        self.password = page.get_by_role("textbox", name="Password")
        self.login_btn = page.get_by_role("button", name="Login")
        
    def enter_username(self, username:str):
        self.username.fill(username)
        
    def enter_password(self, password:str):
        self.password.fill(password)
        
    def click_login(self):
        self.login_btn.click()