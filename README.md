## 🛒 Sauce Demo Test Automation Framework

Welcome to the **Selenium Test Automation Framework** for **SauceDemo**! This framework automates functional and UI testing for the SauceDemo website, an e-commerce platform used for test automation practice. The goal is to ensure high-quality and bug-free interactions for end users.

🔧 **Built With:**
- **Selenium** 🐍 - For automating browser actions
- **Python** 🐍 - For scripting and automation logic
- **Pytest** 🐍 - For test execution and reporting
- **Allure** 🌟 - For generating and serving interactive test reports
- **Page Object Model** (POM) 📂 - For scalable and maintainable test scripts

This framework performs automated tests on user workflows such as logging in, adding/removing items to the cart, sorting products, and validating product details.

---
![Successful Purchase](SwagLabsGIF.gif)

## 🚀 Features

- **Login Automation**: Test successful and unsuccessful login scenarios.
- **Cart Management**: Add/remove products from the shopping cart.
- **Product Sorting**: Sort products by price, name, and other parameters.
- **Error Message Validation**: Ensure proper error messages are shown for invalid login attempts.
- **API Testing**: Automate testing for the backend API, including validating the response from various endpoints such as products and carts.

## 🌟 Allure Reports

This project uses **Allure** to generate interactive and detailed test reports. After running the tests, you can view the results in a visual format by running the following command:

```bash
allure serve allure-results
```

---
## 🧑‍💻 API Tests

In addition to the UI tests, extensive API tests have been implemented to ensure the reliability and correctness of both standard and advanced backend operations. These tests cover a wide range of API endpoints and HTTP methods, including GET, POST, PUT, DELETE, and PATCH. The tests validate the expected behavior of critical API responses for various entities, such as users, products, and carts.

- **Product API Testing**: Verifies the creation, retrieval, updating, and deletion of product data. Ensures required fields (e.g., id, title, price) are correctly structured and present.
  
- **User API Testing**: Confirms the correctness of user data by validating the presence of essential fields like id, email, username, and proper user account management via POST and DELETE operations.
  
- **Cart API Testing**: Validates the functionality of cart operations, including adding/removing products, updating cart details, and checking cart contents. Ensures that all cart-related APIs perform as expected.

These API tests are part of the automated test suite and ensure comprehensive validation of both backend functionality and data integrity. Running the tests will provide valuable insights into the correctness and reliability of the API, from data creation to manipulation and deletion.
##
---
## 🔍 Summary

This project showcases my ability to build scalable and maintainable test automation frameworks using Selenium and Python for UI testing, alongside robust API testing using Pytest. It highlights my skills in automating user workflows, ensuring software quality, and validating both front-end and back-end systems with a complete range of operations.

Feel free to explore the repository, and don't hesitate to reach out if you'd like to discuss any aspects of this project or the automation practices used here. 
---
