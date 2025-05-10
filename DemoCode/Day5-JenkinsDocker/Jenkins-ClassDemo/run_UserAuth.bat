@echo off

cd /d D:\Anjali\CourseMaterial\Playwright\DemoCode-PlaywrightBasics\Day4\Login_Behave

python -m venv venv

call venv\Scripts\activate

pip install -r requirements.txt

python -m playwright install

C:\Users\dell\anaconda3\envs\DemoCode\Scripts\behave ./features/Login.feature -f allure_behave.formatter:AllureFormatter -o C:\jenkins_reports\allure-results

allure generate C:\jenkins_reports\allure-results -o C:\jenkins_reports\allure-report --clean

allure open C:\jenkins_reports\allure-report

deactivate
