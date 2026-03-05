# SauceDemo Playwright Automation Framework

This project automates the SauceDemo e-commerce website using **Playwright + Pytest**.

## Tech Stack
- Python
- Playwright
- Pytest
- Page Object Model (POM)
- Git / GitHub

## Project Structure

config/ → Test data and configuration  
pages/ → Page Object classes  
tests/ → Test cases  
conftest.py → Pytest fixtures and setup  

## Features Implemented

- Login automation
- Product page validation
- Add to cart functionality
- Cart validation
- Checkout process
- Screenshot on test failure
- Pytest markers (smoke tests)

## How to Run the Tests

Install dependencies:

### 1. Clone the repository

git clone https://github.com/vikassuthar33/saucedemo-playwright-automation.git

### 2. Install dependencies
pip install -r requirements.txt

### 3. Install Playwright browsers
playwright install

### 4. Run tests 
pytest