# QA Automation Learning Journey 🚀

Welcome to my QA Automation portfolio repository! This project documents my hands-on practice building reliable, maintainable end-to-end UI tests using **Python**, **Playwright**, and **Pytest**.

## 🧪 Current Test Coverage

### 1. SauceDemo Standard User Login (`test_saucedemo_login.py`)
Validates the end-to-end authentication flow on [SauceDemo](https://saucedemo.com):
* **Navigation:** Launches the SauceDemo login page.
* **User Interaction:** Enters valid `standard_user` credentials using user-facing placeholder locators (`get_by_placeholder`) and clicks the login button via accessible role locators (`get_by_role`).
* **Assertions:**
  * Verifies successful redirection to the inventory page URL (`/inventory.html`).
  * Confirms the `"Products"` page heading is visible after login.

## 🛠️ Tech Stack
* **Language:** Python 3.13
* **Automation Framework:** Playwright
* **Test Runner:** Pytest
* **IDE:** PyCharm

## ⚙️ How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd qa-automation-learning-journey
   ```

2. **Install dependencies:**
   ```bash
   pip install pytest-playwright
   playwright install
   ```

3. **Run the test:**
   ```bash
   pytest
   ```
