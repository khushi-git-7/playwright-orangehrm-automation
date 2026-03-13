from playwright.sync_api import Page, expect

class Homepage:
    def __init__(self, page:Page):
        self.page = page
        self.upgrade_btn = page.get_by_role("button", name="Upgrade")
        self.performance_link = page.get_by_role("link", name="Performance")
        self.dashboard_link = page.get_by_role("link", name="Dashboard")
        
    def verify_upgrade_btn_visible(self):
         expect(self.upgrade_btn).to_be_visible()
    
    def click_performance_link(self):
        self.performance_link.click()
        
    def click_dashboard_link(self):
        self.dashboard_link.click()
