import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time

def wait_and_fill(page, selector, value):
    page.wait_for_selector(selector)
    page.fill(selector, value)


# Function to wait for an element and click it
def wait_and_click(page, selector):
    page.wait_for_selector(selector)
    page.click(selector)

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
    )
    page = context.new_page()
    page.goto("https://app.instantly.ai/auth/login")
    time.sleep(15)

    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("chetan@cleverviral.co")
    time.sleep(2)
    page.get_by_role("textbox", name="Password").click()
    time.sleep(2)
    page.get_by_role("textbox", name="Password").fill("LgS_4PnP5BZBg**")
    time.sleep(2)
    page.get_by_role("button", name="Log In").click()
    # page.wait_for_load_state("load")
    time.sleep(5)
    time.sleep(10)
    list1=['sandra@churneynetwork.pro','sandra@churneynetwork.pro','sandra@churneyImpact.pro']
    for i in list1:
        wait_and_click(page, "//button[contains(., 'Add new')]")
        time.sleep(2)
        wait_and_click(page, "(//h6[text()='Gmail / G-Suite'])[2]")
        time.sleep(2)
        page.locator("div").filter(has_text="Select another").nth(1).click(button="right")
        time.sleep(5)
        page.get_by_role("button", name="Yes, IMAP has been enabled").click()
        time.sleep(5)
        page.get_by_role("button", name="Option 1: oAuth Easier to").click()
        time.sleep(5)

        with page.expect_popup() as page2_info:
            page.get_by_role("button", name="Login").click()
        page2 = page2_info.value  # Capture the new popup window
        page2.wait_for_load_state()
        time.sleep(10)
        try:
            page2.get_by_text("Use another account").click()
        except:
            pass
        page2.get_by_role("textbox", name="Email or phone").fill(f"{i}")
        time.sleep(7)
        page2.get_by_role("button", name="Next").click()
        time.sleep(6)

        page2.get_by_role("button", name="Next").click()
        time.sleep(10)

        page2.get_by_role("textbox", name="Enter your password").click()
        page2.get_by_role("textbox", name="Enter your password").fill("sandra12345@")
        time.sleep(5)
        page2.get_by_role("button", name="Next").click()
        time.sleep(10)
        page2.get_by_role("button", name="Continue").click()
        time.sleep(10)
        page2.wait_for_load_state()
        page2.get_by_role("button", name="Allow").click()
        time.sleep(10)

        page.screenshot(path=f"{i}.png")
        page2.close()
        time.sleep(5)
        page.locator("#topnav").get_by_role("heading", name="Back").click()



        page.locator("//h6[text()='Back']").click()

    browser.close()








with sync_playwright() as playwright:
    run(playwright)