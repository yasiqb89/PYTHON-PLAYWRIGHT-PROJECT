# 🎭 Playwright Python Web Testing – Swag Labs - Portfolio Demo

End-to-end UI testing project using [Playwright](https://playwright.dev/python/) with **Python**, structured for clarity, reusability, and CI integration.

This project targets the [Swag Labs](https://www.saucedemo.com/) demo app, with complete test coverage for login, cart, sorting, checkout, and edge cases. It includes GitHub Actions integration and generates test reports.

---

## 📁 Project Structure

├── .github/workflows/        # GitHub Actions CI
│   └── playwright-tests.yml
├── pages/                    # Page Object Model classes
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── checkout_page.py
│   └── navigation_page.py
├── tests/                    # Test suites grouped by feature
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_checkout.py
│   └── test_navigation.py
├── conftest.py               # Shared fixtures like Playwright setup
├── pytest.ini                # Custom markers for selective test execution
└── requirements.txt          # (Add dependencies if needed)


## ✅ Features Tested

| Area                         | Description |
|------------------------------|-------------|
| 🔐 Login & Auth              | Valid/invalid login, locked-out user |
| 🛒 Cart Behavior             | Add/remove items, cart reset, session tests |
| 📦 Inventory Sorting         | Sort A-Z, Z-A, Price Low-High, High-Low |
| ✅ Checkout Flow             | End-to-end test with form validation |
| 🧪 Edge & Error Cases        | Missing fields, invalid product ID, manipulation |
| 🔄 Data-Driven Tests         | Parametrized login/sorting/product tests |
| ⚙️ CI Integration            | GitHub Actions for test runs and reporting |

---

## 🧪 How to Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run all tests (headless)

```bash
pytest tests/
```

### 3. Run a specific test file

```bash
pytest tests/test_login.py
```

### 4. Run a specific test by name

```bash
pytest tests/test_navigation.py -k "test_invalid_product_id_manipulation"
```

---

## 🌐 Run in Headed Mode

To visually see browser interaction:

```bash
pytest --headed
```

Or set `headless=False` in your Playwright browser launch code inside `conftest.py`.

---

## 📊 Generate an HTML Report (Optional)

```bash
pip install pytest-html
pytest tests/ --html=reports/playwright-report.html --self-contained-html
```

Open the generated report at `reports/playwright-report.html`.

---

## 🤖 GitHub Actions CI

Automatically runs tests on push/pull using `playwright-tests.yml`.  
Includes:

- Install dependencies
- Run Playwright tests
- Upload HTML report as artifact

---

## 👨‍💻 Author

[Yassir](https://github.com/yasiqb89) — building QA automation skills with real-world, structured projects.

---

## 📄 License

This project is open for educational and portfolio use.