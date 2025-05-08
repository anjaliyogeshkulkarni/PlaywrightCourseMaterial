from behave.__main__ import main

if __name__ == '__main__':
    main([
        '--tags=@smoke',
        '--format=allure_behave.formatter:AllureFormatter',
        '--outfile=allure-results',
        'features/'
    ])
