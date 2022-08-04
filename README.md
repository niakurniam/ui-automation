# UI Automation Using Selenium and Python

This repository is my first UI automation testing project. My project implement Python 3.x code for an automated test of a website. Following UI automation best practices, Page Object Model and Page Factory design patterns were used in writing the tests. And for testing framework using unittest

## Software Tools

 * Python 3 
 * Selenium
 * ChromeDriver
 * PyCharm

## Installation

 * Download and install Python 3.x: https://www.python.org/downloads/
 * Install Selenium
 ```bash
 pip install selenium
 ```
 * Download and install WebDriver (e.g. ChromeDriver) in your desktop: https://chromedriver.chromium.org/downloads
 * Download and install PyCharm as Python IDE: https://www.jetbrains.com/pycharm/download

## Code Structure

Create 3 test suites were used to organize the code:
 * Login Test Suite 
 * Login Page Elements Suite
 * Login Page Elements Validation Suite

## How to Run Test?

To run tests, run the project in PyCharm:
 * Clone ui-automation repository to local desktop
 ```bash
  git clone https://github.com/niakurniam/ui-automation.git
 ```
 * Open ui-automation project using PyCharm IDE
 * Before running the project, make sure Python 3.x already installed successfully
 * Then, running ui-automation project by click Run > Click Run....
 * Finally, the project will run and execute the test suite in ChromeDriver