#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Install Playwright browsers (if not already installed)
python3 -m playwright install

# Run Behave tests and generate Allure results
behave -f allure_behave.formatter:AllureFormatter -o /app/jenkins_reports/allure-results

# Generate Allure report
allure generate /app/jenkins_reports/allure-results -o /app/jenkins_reports/allure-report --clean
