from playwright.sync_api import Page, expect

# Practice Project: Testing the SauceDemo login page
# Goal: Check if a standard user can log in to SauceDemo successfully.

def test_saucedemo_login(page: Page):
    # Step 1: Open the SauceDemo login website
    page.goto("https://www.saucedemo.com")

    # Step 2: Type the SauceDemo username and password into the input boxes
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    # Step 3: Click the Login button
    page.get_by_role("button", name="Login").click()

    # Step 4: Verify that we landed on the SauceDemo inventory page
    expect(page).to_have_url('https://www.saucedemo.com/inventory.html')

    # Step 5: Verify that the "Products" title is visible after logging in
    expect(page.get_by_text("Products")).to_be_visible()

    print("SauceDemo login test passed!")


