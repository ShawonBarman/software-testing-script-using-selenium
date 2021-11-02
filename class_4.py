# pip install pyhtmlreport
from pyhtmlreport import Report
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


report = Report()
driver = webdriver.Chrome(executable_path="F:\Python program\web drivers\chromedriver.exe") #where your chrome webdriver

report.setup(
	report_folder=r'F:\Python program\BPMS\testing\driver\reports', #where to save the report
	module_name='Report',
	release_name='Release 1',
	selenium_driver=driver
)
driver.get('http://127.0.0.1:8000/')

try:
    # Start of Test
    report.write_step(
    	'Testing Search functionality',
    	status=report.status.Start,
    	test_number=1
    )
    search_box = driver.find_element_by_css_selector('input[aria-label="Search"]')
    search_box.send_keys('UAP')
    search_box.send_keys(Keys.ENTER)

    # Test Steps
    results = driver.find_elements_by_css_selector('div[id="search"] div[class="g"]')
    assert len(results) > 1
    report.write_step(
    	'Google Search returned more than 1 results',
    	status=report.status.Pass,
    	screenshot=True
    )
except AssertionError:
    report.write_step(
        'Google Search did not return any result',
	 status=report.status.Fail,
	 screenshot=True
    )
except Exception as e:
    report.write_step(
        f'Something went wrong during execution!</br>{e}',
        status=report.status.Warn,
	screenshot=True
    )
finally:
    report.generate_report()
    driver.quit()
